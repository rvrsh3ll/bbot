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
                        Modules to enable. Choices: sitedossier,crt,postman,ipneighbor,bucket_amazon,baddns_direct,ipstack,extractous,bucket_google,host_header,internetdb,jadx,baddns_zone,bucket_azure,ajaxpro,skymem,censys,postman_download,dockerhub,generic_ssrf,ip2location,gitlab,url_manipulation,paramminer_getparams,builtwith,emailformat,gowitness,github_workflows,bevigil,wayback,subdomaincenter,nuclei,bucket_firebase,bucket_file_enum,badsecrets,httpx,apkpure,leakix,paramminer_headers,chaos,git,filedownload,git_clone,sslcert,virustotal,trufflehog,ffuf,pgp,shodan_dns,certspotter,ntlm,secretsdb,wappalyzer,c99,securitytrails,securitytxt,newsletters,urlscan,dnsdumpster,credshed,baddns,wafw00f,dastardly,azure_tenant,docker_pull,columbus,fullhunt,fingerprintx,hackertarget,github_codesearch,dnsbrute,zoomeye,affiliates,oauth,azure_realm,binaryedge,bufferoverrun,dehashed,dnscaa,dnscommonsrv,myssl,ffuf_shortnames,robots,rapiddns,digitorus,wpscan,hunterio,passivetotal,code_repository,bypass403,vhost,google_playstore,dnsbrute_mutations,anubisdb,viewdns,trickest,portscan,smuggler,iis_shortnames,paramminer_cookies,bucket_digitalocean,dnsbimi,social,otx,github_org,hunt,telerik,subdomainradar,dotnetnuke,asn
  -l, --list-modules    List available modules.
  -lmo, --list-module-options
                        Show all module config options
  -em MODULE [MODULE ...], --exclude-modules MODULE [MODULE ...]
                        Exclude these modules.
  -f FLAG [FLAG ...], --flags FLAG [FLAG ...]
                        Enable modules by flag. Choices: email-enum,affiliates,web-screenshots,subdomain-hijack,baddns,portscan,iis-shortnames,safe,web-thorough,active,cloud-enum,web-basic,passive,report,code-enum,subdomain-enum,slow,aggressive,social-enum,deadly,web-paramminer,service-enum
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
                        Output module(s). Choices: asset_inventory,discord,python,slack,http,json,web_report,teams,subdomains,emails,websocket,sqlite,txt,csv,stdout,neo4j,splunk
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
