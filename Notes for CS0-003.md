# Lab issues

## Exploring the lab environment

No DHCP on any virtual network other than INTERNET. IP address doesn't validate.

## Reviewing IoC and threat intelligence sources

Alienvault link returns no useable result. Try [https://otx.alienvault.com/pulse/614e0dc583aa90bf2dd4ec91](https://otx.alienvault.com/pulse/614e0dc583aa90bf2dd4ec91). Obviously the first ip address will be different. Also, no IPv6 or HASH entries - whatev's

CIS benchmarks site no longer matches instructions

## Configuring centralised logging

Couldn't see any logs from MS10 - odd error message. No idea

If bash (linux shell) gets stuck in the wrong colour -

`echo -e "\033[0m"`

## Performing passive scanning

ICMP unreachables leaked thru filter?

## Establishing context awareness

Not sure why the lab considers kali unaffected by CVE-2021-4217

Email stuff - lots of *type to active machine* buttons instead of *copy text* buttons.

No copy marker for email header - manual select and copy..

## Detecting legacy systems

.2 scan result differs from described

.9 and .14 results swapped in scan result

EOS details for Debian 12.2 are a bit messed up in the lab instructions

## IoC detection and analysis

Command to add  administrator needs /add not /all

## Performing playbook incident response

Hash will only validate if generated using openSSL - ie CLI-CP method due to case mismatch

## Using file analysis techniques

Hint:

`strings -n 21 sample.*ext*`

will only show strings 21 chars or longer

`md5sum 4-kwsrch-ext3/ext3-img-kw-1.dd >> 4-kwsrch-ext3-hash.txt`

Take care to append ie >>

`less imageout.txt`

String 'slacker' may or may not be present depending on screen resolution

In Hexedit - strange behaviour for search - full screen mode didn't change behaviour. Just pressed W ???

## Analysing potentially malicious files

In 'File analysis with virus total'

step 24 typo.. Correct validation choice is out by 1 digit - you figure it out :)

