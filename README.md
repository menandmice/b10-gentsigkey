b10-gentsigkey
==============

tool to create BIND 10 TSIG keys

The tool creates by default an HMAC-MD5 key with 128bits size and
prints the key on the screen: 
```
# b10-gentsigkey.py example.com example.com:rc4VdlEPMFan4D+9icDEkg==:hmac-md5
```

b10-gentsigkey options:
```
Usage: b10-gentsigkey.py [--help | options] name
Options:
 -h, --help              show this help message and exit
 -a ALGORITHM, --algorithm=ALGORITHM
                         algorithm for the TSIG key
 -b SIZE, --bits=SIZE
                         size of the key
 -f                      print bindctl CLI command
```
b10-gentsigkey supports all the TSIG algorithms that are also
supported by BIND 10 ('hmac-md5', 'hmac-sha1', 'hmac-sha224',
'hmac-sha256', 'hmac-sha384', 'hmac-sha512').

Using the "-f" (Format) switch, the tool will print the bindctl
command to enter the TSIG key into the BIND 10 configuration. That
command can be copy-n-paste into the bindctl command line:
```
# b10-gentsigkey.py -a hmac-sha256 -b 256 -f example.de
config add tsig_keys/keys "example.de:M2nrsQWVEAuAfm67U2Gdfj2dFfJIPay9ZFMukXSSCiY=:hmac-sha256"
config commit
```
this output can be directly piped into bindctl:
```
# b10-gentsigkey.py -a hmac-sha1 -b 256 -f example.com | bindctl
```