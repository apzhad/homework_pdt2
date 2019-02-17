# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.create(Group(name="new_group", header="header_group", footer="first_group"))
    gen.session.logout()


def test_add_empty_group(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.create(Group(name="", header="", footer=""))
    gen.session.logout()


def test_add_empty_v2(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.create_empty()
    gen.session.logout()
