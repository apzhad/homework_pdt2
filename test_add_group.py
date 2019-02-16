# -*- coding: utf-8 -*-
import pytest
from group import Group
from generic import Generic


@pytest.fixture
def gen(request):
    fixture = Generic()
    request.addfinalizer(fixture.finish)
    return fixture


def test_add_group(gen):
    gen.login(username="admin", password="secret")
    gen.create_new_group(Group(name="new_group", header="header_group", footer="first_group"))
    gen.logout()


def test_add_empty_group(gen):
    gen.login(username="admin", password="secret")
    gen.create_new_group(Group(name="", header="", footer=""))
    gen.logout()
