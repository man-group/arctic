#
# Copyright (C) 2015 Man AHL
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
# USA

import logging
from setuptools import setup
from setuptools.extension import Extension
from setuptools import find_packages
from setuptools.command.test import test as TestCommand
import sys
import os
import subprocess
import platform

link_args = ['-fopenmp']
# Avoid compiling error with prange. Similar to http://stackoverflow.com/questions/36577182/unable-to-assign-value-to-array-in-prange
compile_args = ['-fopenmp', '-fpermissive']

if platform.system().lower() == 'darwin':
    # if a recent compiler on PATH (e.g. from anaconda) then let's use that
    gcc_out = subprocess.check_output(['gcc', '-v'], stderr=subprocess.STDOUT)
    if b'LLVM' in gcc_out:    
        # clang on macOS does not work with OpenMP
        ccs = ["/usr/local/bin/g++-5",
               "/usr/local/bin/g++-6",
               "/usr/local/bin/g++-7",
               "/usr/local/opt/llvm/bin/clang"]
        cc = None
        for compiler in ccs:
            if os.path.isfile(compiler):
                cc = compiler
        if cc is None:
            raise ValueError("You must install clang-6.0 or gcc/g++. You can install with homebrew: brew install gcc or brew install llvm")
        if 'clang' in cc and os.path.isdir("/usr/local/opt/libomp")==False:
            raise ValueError("You must also install libomp.  You can install with homebrew: brew install libomp")
        os.environ["CC"] = cc if 'clang' in cc else cc.replace("g++", "gcc")
        os.environ["CXX"] = cc
        if 'clang' in cc:
            link_args = ['-fopenmp=libomp']
    
    # not all OSX/clang compiler flags supported by GCC. For some reason
    # these sometimes are generated and used. Cython will still add more flags.
    os.environ["CFLAGS"] = "-fno-common -fno-strict-aliasing -DENABLE_DTRACE -DMACOSX -DNDEBUG -Wall -g -fwrapv -Os"

elif platform.system().lower() == 'windows':
    compile_args = ['/openmp']
    link_args = []

# Convert Markdown to RST for PyPI
# http://stackoverflow.com/a/26737672
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    changelog = pypandoc.convert('CHANGES.md', 'rst')
except (IOError, ImportError, OSError):
    long_description = open('README.md').read()
    changelog = open('CHANGES.md').read()


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level='DEBUG')

        # import here, cause outside the eggs aren't loaded
        import pytest
        import six

        args = [self.pytest_args] if isinstance(self.pytest_args, six.string_types) else list(self.pytest_args)
        args.extend(['--cov', 'arctic',
                     '--cov-report', 'xml',
                     '--cov-report', 'html',
                     '--junitxml', 'junit.xml',
                    ])
        errno = pytest.main(args)
        sys.exit(errno)


class defer_cythonize(list):
    def __init__(self, callback):
        self._list, self.callback = None, callback

    def c_list(self):
        if self._list is None:
            self._list = self.callback()
        return self._list

    def __iter__(self):
        for elem in self.c_list():
            yield elem

    def __getitem__(self, ii):
        return self.c_list()[ii]

    def __len__(self):
        return len(self.c_list())


def extensions():
    from Cython.Build import cythonize
    return cythonize(Extension('arctic._compress',
                               sources=["src/_compress.pyx", "src/lz4.c", "src/lz4hc.c"],
                               extra_compile_args=compile_args,
                               extra_link_args=link_args))


setup(
    name="arctic",
    version="1.66.0",
    author="Man AHL Technology",
    author_email="ManAHLTech@ahl.com",
    description=("AHL Research Versioned TimeSeries and Tick store"),
    license="GPL",
    keywords=["ahl", "keyvalue", "tickstore", "mongo", "timeseries", ],
    url="https://github.com/manahl/arctic",
    packages=find_packages(exclude=['tests', 'tests.*', 'benchmarks']),
    long_description='\n'.join((long_description, changelog)),
    cmdclass={'test': PyTest},
    ext_modules=defer_cythonize(extensions),
    setup_requires=["six",
                    "cython",
                    "numpy",
                    "setuptools-git",
                   ],
    install_requires=["cython",
                      "decorator",
                      "enum34",
                      "mockextras",
                      "pandas",
                      "pymongo",
                      "python-dateutil",
                      "pytz",
                      "tzlocal",
                     ],
    tests_require=["mock",
                   "mockextras",
                   "pytest",
                   "pytest-cov",
                   "pytest-server-fixtures",
                   "pytest-timeout",
                   "pytest-xdist",
                   "lz4"
                  ],
    entry_points={'console_scripts': [
                                        'arctic_init_library = arctic.scripts.arctic_init_library:main',
                                        'arctic_list_libraries = arctic.scripts.arctic_list_libraries:main',
                                        'arctic_delete_library = arctic.scripts.arctic_delete_library:main',
                                        'arctic_enable_sharding = arctic.scripts.arctic_enable_sharding:main',
                                        'arctic_copy_data = arctic.scripts.arctic_copy_data:main',
                                        'arctic_create_user = arctic.scripts.arctic_create_user:main',
                                        'arctic_prune_versions = arctic.scripts.arctic_prune_versions:main',
                                        'arctic_fsck = arctic.scripts.arctic_fsck:main',
                                        ]
                  },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Cython",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Database",
        "Topic :: Database :: Front-Ends",
        "Topic :: Software Development :: Libraries",
    ],
)
