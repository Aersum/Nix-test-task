import pytest


def pytest_addoption(parser):
    parser.addoption("--rounding_index", action="store")


@pytest.fixture(scope='session')
def rounding_index(request):
    rounding_index_value = request.config.option.rounding_index
    if rounding_index_value is None:
        pytest.skip()
    return rounding_index_value
