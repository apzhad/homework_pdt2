# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(gen):
    old_group_list = gen.group.get_group_list()
    gen.group.create(Group(name="new_group", header="header_group", footer="first_group"))
    new_group_list = gen.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)


def test_add_empty_group(gen):
    old_group_list = gen.group.get_group_list()
    gen.group.create(Group(name="", header="", footer=""))
    new_group_list = gen.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)


def test_add_empty_v2(gen):
    old_group_list = gen.group.get_group_list()
    gen.group.create_empty()
    new_group_list = gen.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)
