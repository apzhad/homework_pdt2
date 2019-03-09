# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string
import re


def random_string(prefix, max_length):
    symbols = string.ascii_letters + string.digits + ' '*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header_group", 20), footer=random_string("footer", 20))
    for i in range(5)
]


def delete_whitespace(s):
    if len(s) > 0:
        s = re.sub('\s+', ' ', s)
        if s[-1] == " ":
            s = s[:-1]
    return s


def normalize_name(group):
    group.name = delete_whitespace(group.name)
    return group


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(gen, group):
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
