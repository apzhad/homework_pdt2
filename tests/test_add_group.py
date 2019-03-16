# -*- coding: utf-8 -*-
from model.group import Group
import re


def delete_whitespace(s):
    if len(s) > 0:
        s = re.sub('\s+', ' ', s)
        if s[-1] == " ":
            s = s[:-1]
    return s


def normalize_name(group):
    if group.name is not None:
        group.name = delete_whitespace(group.name)
    else:
        group.name = ""
    return group


def test_add_group(gen, data_groups):
    group = data_groups
    old_group_list = gen.group.get_group_list()
    gen.group.create(group)
    assert len(old_group_list) + 1 == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list.append(normalize_name(group))
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_add_group_with_whitespace(gen):
    old_group_list = gen.group.get_group_list()
    group = Group(name="nameE7zwRa ", header="header_groupISZ", footer="footer1S tph")
    gen.group.create(group)
    assert len(old_group_list) + 1 == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list.append(normalize_name(group))
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_add_empty_v2(gen):
    old_group_list = gen.group.get_group_list()
    gen.group.create_empty()
    assert len(old_group_list) + 1 == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list.append(Group(name=""))
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
