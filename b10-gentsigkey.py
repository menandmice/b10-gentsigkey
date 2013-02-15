#!/usr/bin/env python3
# Copyright (C) 2013  Men & Mice
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND ISC DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS.  IN NO EVENT SHALL ISC BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
# OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.

"""
b10-gentsigkey is a simple tool to create TSIG keys (used to secure dynamic
updates and zone-transfers) for the BIND 10 DNS server (http://bind10.isc.org)
"""

import os
import sys
import random
import base64
from optparse import OptionParser

# Main program
if __name__ == "__main__":
    parser = OptionParser(usage="Usage: %prog [--help | options] name")
    parser.add_option("-a", "--algorithm", dest="algorithm", default="hmac-md5",
                      choices=['hmac-md5', 'hmac-sha1', 'hmac-sha224', 'hmac-sha256', 'hmac-sha384', 'hmac-sha512'],
                      help="algorithm for the TSIG key")
    parser.add_option("-b", "--bytes", dest="size", default="128", type="int", 
                      help="size of the key")
    parser.add_option("-f", action="store_true", dest="bindctlformat", default=False, help="print bindctl CLI command")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("you must supply a name for the key")
    randomtext = os.urandom(int(int(options.size)/8))
    tsigsecret = base64.b64encode(randomtext).decode("utf-8")
    keystring = (args[0].lower()+":"+tsigsecret+":"+options.algorithm)
    if (options.bindctlformat):
        print ('config add tsig_keys/keys "' + keystring + '"')
    else:
        print(keystring)
