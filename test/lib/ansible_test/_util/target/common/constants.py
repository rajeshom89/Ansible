"""Constants used by ansible-test. Imports should not be used in this file."""

# NOTE: This file resides in the _util/target directory to ensure compatibility with all supported Python versions.

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

# Setting a low soft RLIMIT_NOFILE value will improve the performance of subprocess.Popen on Python 2.x when close_fds=True.
# This will affect all Python subprocesses. It will also affect the current Python process if set before subprocess is imported for the first time.
SOFT_RLIMIT_NOFILE = 1024

# File used to track the ansible-test test execution timeout.
TIMEOUT_PATH = '.ansible-test-timeout.json'

REMOTE_ONLY_PYTHON_VERSIONS = (
    '2.6',
    '2.7',
    '3.5',
    '3.6',
    '3.7',
)

CONTROLLER_PYTHON_VERSIONS = (
    '3.8',
    '3.9',
    '3.10',
)

CONTROLLER_MIN_PYTHON_VERSION = CONTROLLER_PYTHON_VERSIONS[0]
SUPPORTED_PYTHON_VERSIONS = REMOTE_ONLY_PYTHON_VERSIONS + CONTROLLER_PYTHON_VERSIONS

COVERAGE_REQUIRED_VERSION = '4.5.4'

REMOTE_PROVIDERS = [
    'default',
    'aws',
    'azure',
    'ibmps',
    'parallels',
]

SECCOMP_CHOICES = [
    'default',
    'unconfined',
]

# This bin symlink map must exactly match the contents of the bin directory.
# It is necessary for payload creation to reconstruct the bin directory when running ansible-test from an installed version of ansible.
# It is also used to construct the injector directory at runtime.
ANSIBLE_BIN_SYMLINK_MAP = {
    'ansible': '../lib/ansible/cli/scripts/ansible_cli_stub.py',
    'ansible-config': 'ansible',
    'ansible-connection': '../lib/ansible/cli/scripts/ansible_connection_cli_stub.py',
    'ansible-console': 'ansible',
    'ansible-doc': 'ansible',
    'ansible-galaxy': 'ansible',
    'ansible-inventory': 'ansible',
    'ansible-playbook': 'ansible',
    'ansible-pull': 'ansible',
    'ansible-test': '../test/lib/ansible_test/_util/target/cli/ansible_test_cli_stub.py',
    'ansible-vault': 'ansible',
}