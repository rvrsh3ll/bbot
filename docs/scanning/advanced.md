# Advanced

Below you can find some advanced uses of BBOT.

## BBOT as a Python library

#### Synchronous
```python
from bbot.scanner import Scanner

if __name__ == "__main__":
    scan = Scanner("evilcorp.com", presets=["subdomain-enum"])
    for event in scan.start():
        print(event)
```

#### Asynchronous
```python
from bbot.scanner import Scanner

async def main():
    scan = Scanner("evilcorp.com", presets=["subdomain-enum"])
    async for event in scan.async_start():
        print(event.json())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

## Command-Line Help

<!-- BBOT HELP OUTPUT -->
```text
usage: bbot [-h] [-t TARGET [TARGET ...]] [-w WHITELIST [WHITELIST ...]]
               [-b BLACKLIST [BLACKLIST ...]] [--strict-scope]
               [-p [PRESET ...]] [-c [CONFIG ...]] [-lp]
               [-m MODULE [MODULE ...]] [-l] [-lmo] [-em MODULE [MODULE ...]]
               [-f FLAG [FLAG ...]] [-lf] [-rf FLAG [FLAG ...]]
               [-ef FLAG [FLAG ...]] [--allow-deadly] [-n SCAN_NAME] [-v] [-d]
               [-s] [--force] [-y] [--dry-run] [--current-preset]
               [--current-preset-full] [-o DIR] [-om MODULE [MODULE ...]]
               [--json] [--brief]
               [--event-types EVENT_TYPES [EVENT_TYPES ...]]
               [--no-deps | --force-deps | --retry-deps | --ignore-failed-deps | --install-all-deps]
               [--version] [-H CUSTOM_HEADERS [CUSTOM_HEADERS ...]]
               [--custom-yara-rules CUSTOM_YARA_RULES]

Bighuge BLS OSINT Tool

options:
  -h, --help            show this help message and exit

Target:
  -t TARGET [TARGET ...], --targets TARGET [TARGET ...]
                        Targets to seed the scan
  -w WHITELIST [WHITELIST ...], --whitelist WHITELIST [WHITELIST ...]
                        What's considered in-scope (by default it's the same as --targets)
  -b BLACKLIST [BLACKLIST ...], --blacklist BLACKLIST [BLACKLIST ...]
                        Don't touch these things
  --strict-scope        Don't consider subdomains of target/whitelist to be in-scope

Presets:
  -p [PRESET ...], --preset [PRESET ...]
                        Enable BBOT preset(s)
  -c [CONFIG ...], --config [CONFIG ...]
                        Custom config options in key=value format: e.g. 'modules.shodan.api_key=1234'
  -lp, --list-presets   List available presets.

Modules:
  -m MODULE [MODULE ...], --modules MODULE [MODULE ...]
                        Modules to enable. Choices: emailformat,ntlm,hunt,bucket_digitalocean,bucket_google,columbus,portscan,ffuf,paramminer_getparams,wappalyzer,affiliates,censys,azure_tenant,dockerhub,bucket_amazon,ipneighbor,anubisdb,dastardly,viewdns,builtwith,trufflehog,bevigil,dnscaa,baddns_direct,vhost,docker_pull,ip2location,shodan_dns,wafw00f,bucket_firebase,digitorus,trickest,hackertarget,subdomainradar,ffuf_shortnames,dotnetnuke,smuggler,iis_shortnames,gowitness,dnsbrute_mutations,dnsbrute,paramminer_cookies,fingerprintx,baddns_zone,hunterio,github_workflows,github_org,httpx,bufferoverrun,wpscan,securitytxt,sslcert,wayback,asn,github_codesearch,nuclei,virustotal,dnscommonsrv,otx,credshed,bucket_azure,ipstack,code_repository,sitedossier,git_clone,skymem,google_playstore,zoomeye,url_manipulation,apkpure,bypass403,internetdb,leakix,paramminer_headers,urlscan,gitlab,git,baddns,rapiddns,subdomaincenter,oauth,azure_realm,chaos,myssl,host_header,securitytrails,passivetotal,filedownload,postman_download,c99,telerik,fullhunt,crt,secretsdb,binaryedge,ajaxpro,certspotter,dnsdumpster,generic_ssrf,bucket_file_enum,dehashed,unstructured,postman,pgp,badsecrets,social,newsletters,robots
  -l, --list-modules    List available modules.
  -lmo, --list-module-options
                        Show all module config options
  -em MODULE [MODULE ...], --exclude-modules MODULE [MODULE ...]
                        Exclude these modules.
  -f FLAG [FLAG ...], --flags FLAG [FLAG ...]
                        Enable modules by flag. Choices: email-enum,affiliates,web-screenshots,code-enum,passive,web-thorough,portscan,baddns,subdomain-enum,safe,service-enum,deadly,aggressive,iis-shortnames,slow,active,report,subdomain-hijack,social-enum,web-basic,web-paramminer,cloud-enum
  -lf, --list-flags     List available flags.
  -rf FLAG [FLAG ...], --require-flags FLAG [FLAG ...]
                        Only enable modules with these flags (e.g. -rf passive)
  -ef FLAG [FLAG ...], --exclude-flags FLAG [FLAG ...]
                        Disable modules with these flags. (e.g. -ef aggressive)
  --allow-deadly        Enable the use of highly aggressive modules

Scan:
  -n SCAN_NAME, --name SCAN_NAME
                        Name of scan (default: random)
  -v, --verbose         Be more verbose
  -d, --debug           Enable debugging
  -s, --silent          Be quiet
  --force               Run scan even in the case of condition violations or failed module setups
  -y, --yes             Skip scan confirmation prompt
  --dry-run             Abort before executing scan
  --current-preset      Show the current preset in YAML format
  --current-preset-full
                        Show the current preset in its full form, including defaults

Output:
  -o DIR, --output-dir DIR
                        Directory to output scan results
  -om MODULE [MODULE ...], --output-modules MODULE [MODULE ...]
                        Output module(s). Choices: slack,emails,splunk,web_report,txt,json,discord,stdout,subdomains,http,neo4j,csv,websocket,python,teams,asset_inventory
  --json, -j            Output scan data in JSON format
  --brief, -br          Output only the data itself
  --event-types EVENT_TYPES [EVENT_TYPES ...]
                        Choose which event types to display

Module dependencies:
  Control how modules install their dependencies

  --no-deps             Don't install module dependencies
  --force-deps          Force install all module dependencies
  --retry-deps          Try again to install failed module dependencies
  --ignore-failed-deps  Run modules even if they have failed dependencies
  --install-all-deps    Install dependencies for all modules

Misc:
  --version             show BBOT version and exit
  -H CUSTOM_HEADERS [CUSTOM_HEADERS ...], --custom-headers CUSTOM_HEADERS [CUSTOM_HEADERS ...]
                        List of custom headers as key value pairs (header=value).
  --custom-yara-rules CUSTOM_YARA_RULES, -cy CUSTOM_YARA_RULES
                        Add custom yara rules to excavate

EXAMPLES

    Subdomains:
        bbot -t evilcorp.com -p subdomain-enum

    Subdomains (passive only):
        bbot -t evilcorp.com -p subdomain-enum -rf passive

    Subdomains + port scan + web screenshots:
        bbot -t evilcorp.com -p subdomain-enum -m portscan gowitness -n my_scan -o .

    Subdomains + basic web scan:
        bbot -t evilcorp.com -p subdomain-enum web-basic

    Web spider:
        bbot -t www.evilcorp.com -p spider -c web.spider_distance=2 web.spider_depth=2

    Everything everywhere all at once:
        bbot -t evilcorp.com -p kitchen-sink

    List modules:
        bbot -l

    List presets:
        bbot -lp

    List flags:
        bbot -lf

```
<!-- END BBOT HELP OUTPUT -->
