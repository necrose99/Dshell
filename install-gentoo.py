#!/usr/bin/env python

from pkgutil import iter_modules
from subprocess import call

dependencies = {
    "Crypto": "dev-python/pycrypto",
    "dpkt": "dev-python/dpkt",
    "IPy": "dev-python/ipy",
    "pcap": "dev-python/pypcap"
    "pygeoip" : "dev-python/pygeoip"
    "pydoc":"dev-python/epydoc" #Installs pydoc happydoc is the alternative. 
 }

installed, missing_pkgs = [pkg[1] for pkg in iter_modules()], []

for module, pkg in dependencies.items():
    if module not in installed:
        print("dshell requires {}".format(module))
        missing_pkgs.append("python-{}".format(pkg))
    else:
        print("{} is installed".format(module))

if missing_pkgs:
    cmd = ["emerge --sync --quiet && emerge -v",] + missing_pkgs  #  Emerge -av --ask --verbose else emerge foo --quiet to shut up build/emerge messages
# emerge --sync --quiet and or emerge-webrsync --quiet gets all the updates for ebuild scripts/security/metadata/etc 
    print(" ".join(cmd))
    call(cmd)

call(["make", "all"]) ## Gentoo way is offer a choice make rc,init 
# then offer docs via USE="+docks in ebuilds when calling python or disutils.eclass's 
# I pruned the Do you want the docs asker below too much HELL. 

