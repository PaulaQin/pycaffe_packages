from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from codecs import open

import fnmatch
import os
from os import path
import sys
from glob import glob

from setuptools import find_packages, setup, Command

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

_VERSION = '1.0'

REQUIRED_PACKAGES = [
    'Cython>=0.19.2',
    'numpy>=1.11.0',
    'scipy>=1.0.0',
    'scikit-image>=0.9.3',
    'h5py>=2.2.0',
    'networkx>=1.8.1',
    'nose>=1.3.0',
    'pandas>=0.12.0',
    'protobuf>=3.1.0',
    'pyyaml>=3.10',
    'pillow>=2.3.0',
    'six>=1.1.0',
]
project_name = 'caffe'

# python3 requires wheel 0.26
if sys.version_info.major == 3:
  REQUIRED_PACKAGES.append('wheel >= 0.26')
else:
  REQUIRED_PACKAGES.append('wheel')
  # mock comes with unittest.mock for python3, need to install for python2
  REQUIRED_PACKAGES.append('mock >= 2.0.0')


# get lib files
CAFFE_LIB_PATH = os.path.join(os.path.dirname(__file__), "caffe", "libs")
libs_all = [os.path.split(fn)[1] for fn in glob(os.path.join(CAFFE_LIB_PATH, '*'))]
libs = [os.path.join('libs', fn) for fn in libs_all]

package_data = { 'caffe': ['_caffe.so', os.path.join('imagenet','ilsvrc_2012_mean.npy')]}
package_data['caffe'] += libs
kwargs = dict(package_data = package_data)
print(package_data)

setup(
    name=project_name,
    version=_VERSION.replace('-', ''),

    description='caffe python3 binding',
    long_description=long_description,

    # Project's url
    url='https://github.com/PaulaQin/pycaffe_packages',

    # Author
    author = 'Paula Qin',
    author_email = 'paulaqin@gmail.com',
    # License
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Enginnering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    keywords='pycaffe python3',

    packages=find_packages(),

    install_requires=REQUIRED_PACKAGES,

    **kwargs
)
