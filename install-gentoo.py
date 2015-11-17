#!/usr/bin/env python

from pkgutil import iter_modules
from subprocess import call

dependencies = {
    "Crypto": "dev-python/pycrypto",
    "dpkt": "dev-python/dpkt",
    "IPy": "dev-python/ipy",
    "pcap": "dev-python/pypcap"
    "pygeoip" : "dev-python/pygeoip"
 
 

  
 doc? (dev-python/epydoc)"
}

installed, missing_pkgs = [pkg[1] for pkg in iter_modules()], []

for module, pkg in dependencies.items():
    if module not in installed:
        print("dshell requires {}".format(module))
        missing_pkgs.append("python-{}".format(pkg))
    else:
        print("{} is installed".format(module))

if missing_pkgs:
    cmd = ["emerge-sync emerge -v",] + missing_pkgs  # -av

    print(" ".join(cmd))
    call(cmd)

call(["make", "rc"]) ## Gentoo way is hell NO! , make all but docs, 
call(["make", "initpy"]) ## Gentoo way is hell NO! , make all but docs, 
 = input('Would You Like DSHELL DOCS?')
if Docs == 'yes' or 'Yes':
    dependencies = {
        "pydoc":"dev-python/epydoc"
        }
 call(["make", "pydoc"])
else:
  print ("Sorry for asking...")
