#!/usr/bin/env python
import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
#!/usr/bin/env python
try:
    from setuptools import setup as _setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup as _setup

# setup.cfg basically installs itself!  See setup.cfg for the project metadata.
import setup.cfg


_setup(**setup.cfg.to_setup())

from distutils.core import setup
import codecs

with codecs.open('README.rst', encoding='utf-8') as file:
    long_description = file.read()

setup(name='stdeb',
      # Keep version in sync with stdeb/__init__.py and install section
      # of README.rst.
      version='0.8.5',
      author='Andrew Straw',
      author_email='strawman@astraw.com',
      description='Python to Debian source package conversion utility',
      long_description=long_description,
      license='MIT',
      url='http://github.com/astraw/stdeb',
      packages=['stdeb','stdeb.command'],
      scripts=['scripts/py2dsc',
               'scripts/py2dsc-deb',
               'scripts/pypi-download',
               'scripts/pypi-install',
               ],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)






from pkgutil import iter_modules
from subprocess import call

dependencies = {
    "Crypto": "dev-python/pycrypto",
    "dpkt": "dev-python/dpkt",
    "IPy": "dev-python/ipy",
    "pcap": "dev-python/pypcap",
    "pygeoip" : "dev-python/pygeoip",
    "pydoc":"dev-python/epydoc", 
 }

installed, missing_pkgs = [pkg[1] for pkg in iter_modules()], []

for module, pkg in dependencies.items():
    if module not in installed:
        print("dshell requires {}".format(module))
        missing_pkgs.append("python-{}".format(pkg))
    else:
        print("{} is installed".format(module))

if missing_pkgs:
    print("Hello, Calling Emerge to Build packages that are missing")
    cmd = ["emerge --sync --quiet && emerge -v",] + missing_pkgs 

    print(" ".join(cmd))
    call(cmd)

call(["make", "all"])
#Notes to DSHELL TEAM. can TRIM this DOWN if you wish. this is hear as a conveniance/reffrance to you. 
#  Emerge -av --ask --verbose else emerge foo --quiet to shut up build/emerge messages
# emerge --sync --quiet and or emerge-webrsync --quiet gets all the updates for ebuild scripts/security/metadata/etc , updates to portage spam the console, 
# --quiet or remove for the reasuring flurry of text , emerge -v (verbose) , emerge -av give promt to user.
# USE="+DOC +KDE -GTK -VLC" emerge foo-basket? some?package to enable + , DISABLE use-flag -
## Gentoo way is offer a choice make rc,init 
# then offer docs via USE="+docks in ebuilds when calling python or disutils.eclass's 
# I pruned the Do you want the docs asker below too much of a problem. 
# for Sabayon (Gentoo overlay , Binary Distro of Gentoo) USers will need (more or less Strongly recomended) to Run equo i + missing_pkgs & or allow the emerge to post
print("Emerge compleated, NOTE:if you are a Sabayon User (Gentoo-overlay/BIN-overlay) you will Likely whish to resync Portage to Entropy")
print("equo rescue spmsync, to do this , else entropy; Your binary pkg-manager may not be aware that $missing_pkgs were installed")
