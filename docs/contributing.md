## Contributing to Arctic Development

* Feel free to pick up an issue from the bug tracker: https://github.com/manahl/arctic/issues or add an issue in general and assign it to yourself so we don't duplicate the work on the same issue.

* Local installation   
    * Clone the repo locally
    * Create a virtualenv eg. `virtualenv .venv -p python3`
    * Activate the virtualenv eg. `source .venv/bin/activate`
    * Run `python setup.py install` to install dependencies in your virtualenv.
    * Arctic should be ready to use locally, you can test it by importing it in your python interpreter
    
* After you have made changes, you can run tests with `python setup.py test`. You can also do something like: `python setup.py test -a tests/integration/<test_name>` to run a specific test.

* Run pycodestyle locally to make sure it passes the coding style checks. 
 