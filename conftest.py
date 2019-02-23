import pytest
from fixture.generic import Generic


@pytest.fixture(scope="session")
def gen(request):
    fixture = Generic()
    fixture.session.login(username="admin", password="secret")

    def fin():
        fixture.session.logout()
        fixture.finish()
    request.addfinalizer(fin)
    return fixture
