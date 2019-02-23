# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(gen):
    gen.group.create(Group(name="new_group", header="header_group", footer="first_group"))


def test_add_empty_group(gen):
    gen.group.create(Group(name="", header="", footer=""))


def test_add_empty_v2(gen):
    gen.group.create_empty()
