#!/usr/bin/env python
# Copyright 2025 Barsa Nayak
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup configuration for claudePlugins."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='claudePlugins',
    version='1.0.0',
    author='Barsa Nayak',
    author_email='barnayak@ebay.com',
    description='A single repository to manage all Claude Code plugins',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.corp.ebay.com/Registration/claudePlugins',
    packages=find_packages(where='plugins'),
    package_dir={'': 'plugins'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Code Generators',
    ],
    python_requires='>=3.8',
    install_requires=[
        'playsound3>=3.0.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'pylint>=2.0.0',
            'black>=22.0.0',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords='claude-code plugins development ai assistant',
    project_urls={
        'Bug Reports': 'https://github.corp.ebay.com/Registration/claudePlugins/issues',
        'Source': 'https://github.corp.ebay.com/Registration/claudePlugins',
    },
)
