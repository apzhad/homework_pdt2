import pytest
from fixture.generic import Generic
import json
import os.path

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
