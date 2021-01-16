#!/bin/sh
echo 'copy this file to the arctic project directory'
echo 'then run the script to delete the tox run cache'
echo '$ sh ./clean_after_tox.sh'
rm -rf .eggs
rm -rf .tox
rm -rf arctic.egg-info
rm -rf htmlcov
rm -rf .coverage
