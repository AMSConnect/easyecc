import os
import sys
from setuptools import setup, Extension

BOOST_LIB = 'boost_python'
if sys.platform == 'darwin':
    BOOST_LIB = 'boost_python-mt'

base_modules = [
    Extension('_easyecc', [
        'pyeasyecc.cpp',
        ],
        libraries=['cryptopp', BOOST_LIB],
        extra_compile_args=['-fPIC'])
]


# if an extension is missing dependencies, distutils will attempt the build regardless
modules = filter(lambda m: reduce(lambda x, y: x and os.path.exists(y), m.depends, True), base_modules)
missing_modules = filter(lambda m: m not in modules, base_modules)
if missing_modules:
    print 'WARNING: Some Python modules are missing dependencies: %s' % ', '.join(map(lambda x: x.name, missing_modules))

setup(
    name='easyecc',
    description='''A simple wrapper around Crypto++ for Elliptical Curve Cryptography''',
    url='https://github.com/cureatr/easyecc',
    version='0.2',
    author='Alex Khomenko',
    author_email='khomenko@cs.stanford.edu',
    ext_modules=modules,
    py_modules=['easyecc'])
