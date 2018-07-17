import warnings


import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    # Workaround for https://gitlab.com/sashahart/cookies/issues/4
    # and https://github.com/getsentry/responses/issues/186
    from cookies import Cookies # noqa

# Turn deprecation warnings into errors
warnings.simplefilter('error', DeprecationWarning)

pytest_plugins = ['arctic.fixtures.arctic']
