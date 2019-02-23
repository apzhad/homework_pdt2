import pytest
from fixture.generic import Generic

fixture = None


@pytest.fixture
def gen():
    global fixture
    if fixture is None:
        fixture = Generic()
    elif not fixture.is_valid():
        fixture = Generic()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.finish()
    request.addfinalizer(fin)
    return fixture
