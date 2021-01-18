#!/bin/sh
echo 'copy this file to the arctic project directory'
echo 'then run the script to delete the tox run cache'
echo '$ sh ./clean_after_tox.sh'

# Coverage test artifacts
rm -rf .run
rm -rf htmlcov
rm -rf .coverage
rm -rf junit.xml
rm -rf coverage.xml
rm -rf .pytest_cache

# Virtual Environments
rm -rf .tox

# Install Artifacts
rm -rf .eggs
rm -rf arctic.egg-info

# Benchmark Artifacts
rm -rf .asv

# Remove Setup Scripts
rm -rf get-pip.py
rm -rf setpath.sh
