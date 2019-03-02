# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(gen):
    old_group_list = gen.group.get_group_list()
    group = Group(name="new_group", header="header_group", footer="first_group")
    gen.group.create(group)
    new_group_list = gen.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_add_empty_group(gen):
    old_group_list = gen.group.get_group_list()
    group = Group(name="", header="", footer="")
    gen.group.create(group)
    new_group_list = gen.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_add_empty_v2(gen):
    old_group_list = gen.group.get_group_list()
    gen.group.create_empty()
    new_group_list = gen.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)
    old_group_list.append(Group(name=""))
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
