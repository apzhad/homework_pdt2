import pytest
from fixture.generic import Generic


@pytest.fixture
def gen(request):
    fixture = Generic()
    request.addfinalizer(fixture.finish)
    return fixture
