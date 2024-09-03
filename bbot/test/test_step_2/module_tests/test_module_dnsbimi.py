from .base import ModuleTestBase

raw_bimi_txt_default = (
    '"v=BIMI1;l=https://default.thirdparty.tld/brand/logo.svg; a=https://default.thirdparty.tld/brand/certificate.pem"'
)
raw_bimi_txt_nondefault = '"v=BIMI1; l=https://nondefault.thirdparty.tld/brand/logo.svg;a=https://nondefault.thirdparty.tld/brand/certificate.pem;"'


class TestBIMI(ModuleTestBase):
    targets = ["test.localdomain"]
    modules_overrides = ["dnsbimi", "speculate"]
    config_overrides = {
        "modules": {"dnsbimi": {"emit_raw_dns_records": True, "selectors": "default,nondefault"}},
    }

    async def setup_after_prep(self, module_test):
        await module_test.mock_dns(
            {
                "test.localdomain": {
                    "A": ["127.0.0.11"],
                },
                "bimi.test.localdomain": {
                    "A": ["127.0.0.22"],
                },
                "_bimi.test.localdomain": {
                    "A": ["127.0.0.33"],
                },
                "default._bimi.test.localdomain": {
                    "A": ["127.0.0.44"],
                    "TXT": [raw_bimi_txt_default],
                },
                "nondefault._bimi.test.localdomain": {
                    "A": ["127.0.0.44"],
                    "TXT": [raw_bimi_txt_nondefault],
                },
                "_bimi.default._bimi.test.localdomain": {
                    "A": ["127.0.0.44"],
                    "TXT": [raw_bimi_txt_default],
                },
                "_bimi.nondefault._bimi.test.localdomain": {
                    "A": ["127.0.0.44"],
                    "TXT": [raw_bimi_txt_default],
                },
                "default._bimi.default._bimi.test.localdomain": {
                    "A": ["127.0.0.44"],
                    "TXT": [raw_bimi_txt_default],
                },
                "nondefault._bimi.nondefault._bimi.test.localdomain": {
                    "A": ["127.0.0.44"],
                    "TXT": [raw_bimi_txt_nondefault],
                },
            }
        )

    def check(self, module_test, events):
        assert any(
            e.type == "RAW_DNS_RECORD"
            and e.data["host"] == "default._bimi.test.localdomain"
            and e.data["type"] == "TXT"
            and e.data["answer"] == raw_bimi_txt_default
            for e in events
        ), "Failed to emit RAW_DNS_RECORD"
        assert any(
            e.type == "RAW_DNS_RECORD"
            and e.data["host"] == "nondefault._bimi.test.localdomain"
            and e.data["type"] == "TXT"
            and e.data["answer"] == raw_bimi_txt_nondefault
            for e in events
        ), "Failed to emit RAW_DNS_RECORD"
        assert not any(str(e.data) == "https://default.thirdparty.tld/brand/logo.svg" for e in events)
        assert not any(str(e.data) == "https://default.thirdparty.tld/brand/certificate.pem" for e in events)
        assert not any(str(e.data) == "https://nondefault.thirdparty.tld/brand/logo.svg" for e in events)
        assert not any(str(e.data) == "https://nondefault.thirdparty.tld/brand/certificate.pem" for e in events)


class TestBIMIRecursiveRecursion(TestBIMI):
    config_overrides = {
        "modules": {"dnsbimi": {"emit_raw_dns_records": True, "selectors": "default, nondefault"}},
    }

    def check(self, module_test, events):
        assert not any(
            e.type == "RAW_DNS_RECORD" and e.data["host"] == "default._bimi.default._bimi.test.localdomain"
            for e in events
        ), "Unwanted recursion occurring"
        assert not any(
            e.type == "RAW_DNS_RECORD" and e.data["host"] == "nondefault._bimi.nondefault._bimi.test.localdomain"
            for e in events
        ), "Unwanted recursion occurring"
        assert not any(
            e.type == "RAW_DNS_RECORD" and e.data["host"] == "nondefault._bimi.default._bimi.test.localdomain"
            for e in events
        ), "Unwanted recursion occurring"
        assert not any(
            e.type == "RAW_DNS_RECORD" and e.data["host"] == "default._bimi.nondefault._bimi.test.localdomain"
            for e in events
        ), "Unwanted recursion occurring"
