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
 distutils.dir_util.mkpath(name[, mode=0777, verbose=0, dry_run=0])
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

