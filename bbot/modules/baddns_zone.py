from .baddns import baddns as baddns_module


class baddns_zone(baddns_module):
    watched_events = ["DNS_NAME"]
    produced_events = ["FINDING", "VULNERABILITY"]
    flags = ["active", "safe", "subdomain-enum", "baddns", "cloud-enum"]
    meta = {
        "description": "Check hosts for DNS zone transfers and NSEC walks",
        "created_date": "2024-01-29",
        "author": "@liquidsec",
    }
    options = {"custom_nameservers": [], "only_high_confidence": False}
    options_desc = {
        "custom_nameservers": "Force BadDNS to use a list of custom nameservers",
        "only_high_confidence": "Do not emit low-confidence or generic detections",
    }
    module_threads = 8
    deps_pip = ["baddns~=1.4.13"]

    def set_modules(self):
        self.enabled_submodules = ["NSEC", "zonetransfer"]

    # minimize nsec records feeding back into themselves
    async def filter_event(self, event):
        if "baddns-nsec" in event.tags or "baddns-nsec" in event.parent.tags:
            return False
        return True
