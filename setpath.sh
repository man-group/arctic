#!/bin/sh
export TOX_HOME=.venv/bin
export PATH=$TOX_HOME:$PATH

echo "Display executable path and version"
echo "~~~~~ pip ~~~~~~~"
which pip
pip --version
echo "~~~~~ python ~~~~"
which python
python --version
echo "~~~~~ tox ~~~~~~~"
which tox
tox --version
