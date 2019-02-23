import pytest
from fixture.generic import Generic

fixture = None


@pytest.fixture
def gen():
    global fixture
    if fixture is None:
        fixture = Generic()
        fixture.session.login(username="admin", password="secret")
    elif not fixture.is_valid():
        fixture = Generic()
        fixture.session.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.finish()
    request.addfinalizer(fin)
    return fixture
