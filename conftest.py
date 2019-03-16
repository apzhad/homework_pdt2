import pytest
from fixture.generic import Generic
import json
import os.path
import importlib
import jsonpickle

fixture = None
settings = None


@pytest.fixture
def gen(request):
    global fixture
    global settings
    browser = request.config.getoption("--browser")
    if settings is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--settings"))
        with open(config_file) as f:
            settings = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Generic(browser=browser, base_url=settings["base_url"])
    fixture.session.ensure_login(username=settings["username"], password=settings["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.finish()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--settings", action="store", default="settings.json")


def pytest_generate_tests(metafunc):
    """
    This allows us to load tests from external files by
    parametrizing tests with each test case found in a data_X
    file
    https://remusao.github.io/posts/pytest-param.html
    """
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):
            # Load associated test data
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith('json_'):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).test_data


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
