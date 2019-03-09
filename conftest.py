import pytest
from fixture.generic import Generic

fixture = None


@pytest.fixture
def gen(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    if fixture is None:
        fixture = Generic(browser=browser, base_url=base_url)
    elif not fixture.is_valid():
        fixture = Generic(browser=browser, base_url=base_url)
    fixture.session.ensure_login(username="admin", password="secret")
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
    parser.addoption("--base_url", action="store", default="http://localhost/addressbook/")
