# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group_using_json(gen, json_group):
    group = json_group
    old_group_list = gen.group.get_group_list()
    gen.group.create(group)
    assert len(old_group_list) + 1 == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_add_group_using_module(gen, data_groups):
    group = data_groups
    old_group_list = gen.group.get_group_list()
    gen.group.create(group)
    assert len(old_group_list) + 1 == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_add_group_with_whitespace(gen):
    old_group_list = gen.group.get_group_list()
    group = Group(name="name  E7zwRa ", header="header_groupISZ", footer="footer1S tph")
    gen.group.create(group)
    assert len(old_group_list) + 1 == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_add_empty_v2(gen):
    old_group_list = gen.group.get_group_list()
    gen.group.create_empty()
    assert len(old_group_list) + 1 == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list.append(Group(name=""))
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
