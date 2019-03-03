from model.group import Group
from random import randrange


def test_edit_first_group(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit"))
    old_group_list = gen.group.get_group_list()
    group = Group(name="new_name", header="new_header_group", footer="changed_group")
    group.id = old_group_list[0].id
    gen.group.edit_first(group)
    assert len(old_group_list) == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list[0] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_edit_some_group(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit"))
    old_group_list = gen.group.get_group_list()
    group = Group(name="new_name", header="new_header_group", footer="changed_group")
    index = randrange(len(old_group_list))
    group.id = old_group_list[index].id
    gen.group.edit_by_index(index, group)
    assert len(old_group_list) == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list[index] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_clear_first_group_params(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
    old_group_list = gen.group.get_group_list()
    group = Group(name="", header="", footer="")
    group.id = old_group_list[0].id
    gen.group.edit_first(group)
    assert len(old_group_list) == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list[0] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_clear_some_group_params(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
    old_group_list = gen.group.get_group_list()
    group = Group(name="", header="", footer="")
    index = randrange(len(old_group_list))
    group.id = old_group_list[index].id
    gen.group.edit_by_index(index=index, group=group)
    assert len(old_group_list) == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list[index] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_update_first_group_without_changes(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
    old_group_list = gen.group.get_group_list()
    gen.group.update_first_wo_change()
    assert len(old_group_list) == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_update_some_group_without_changes(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
    old_group_list = gen.group.get_group_list()
    index = randrange(len(old_group_list))
    gen.group.update_wo_change_by_index(index)
    assert len(old_group_list) == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_update_all_groups(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
        gen.group.create(Group(name="for_edit_1", header="header_1", footer="footer_1"))
        gen.group.create(Group(name="for_edit_2", header="header_2", footer="footer_2"))
    old_group_list = gen.group.get_group_list()
    group = Group(name="some_name", header="some_header_group", footer="changed_group")
    group.id = old_group_list[0].id
    gen.group.edit_all(group)
    assert len(old_group_list) == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list[0] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_update_all_groups_without_changes(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
        gen.group.create(Group(name="for_edit_1", header="header_1", footer="footer_1"))
        gen.group.create(Group(name="for_edit_2", header="header_2", footer="footer_2"))
    old_group_list = gen.group.get_group_list()
    gen.group.edit_all_wo_change()
    assert len(old_group_list) == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_update_last_group(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
        gen.group.create(Group(name="for_edit_1", header="header_1", footer="footer_1"))
    old_group_list = gen.group.get_group_list()
    group = Group(name="last_name", header="last_header_group", footer="last_group")
    group.id = old_group_list[-1].id
    gen.group.edit_last(group)
    assert len(old_group_list) == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list[-1] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_update_last_group_without_changes(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
        gen.group.create(Group(name="for_edit_1", header="header_1", footer="footer_1"))
    old_group_list = gen.group.get_group_list()
    gen.group.update_last_wo_change()
    assert len(old_group_list) == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_edit_first_group_name(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
    old_group_list = gen.group.get_group_list()
    group = Group(name="only_name")
    group.id = old_group_list[0].id
    gen.group.edit_first(group)
    assert len(old_group_list) == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list[0] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_edit_some_group_name(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
    old_group_list = gen.group.get_group_list()
    group = Group(name="only_name")
    index = randrange(len(old_group_list))
    group.id = old_group_list[index].id
    gen.group.edit_by_index(index, group)
    assert len(old_group_list) == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list[index] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
