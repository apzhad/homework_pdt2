import pytest
from fixture.generic import Generic
import json

fixture = None
settings = None


@pytest.fixture
def gen(request):
    global fixture
    global settings
    browser = request.config.getoption("--browser")
    if settings is None:
        with open(request.config.getoption("--settings")) as config_file:
            settings = json.load(config_file)
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
