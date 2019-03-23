from model.group import Group
import random


def test_del_first_group(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_del"))
    old_group_list = db.get_group_list(sorted=True)
    gen.group.del_first()
    assert len(old_group_list) - 1 == len(db.get_group_list())
    new_group_list = db.get_group_list()
    old_group_list[0:1] = []
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)


def test_del_all_group(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_del_1"))
        gen.group.create(Group(name="for_del_2"))
        gen.group.create(Group(name="for_del_3"))
    gen.group.del_all()
    new_group_list = db.get_group_list()
    assert [] == new_group_list
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)


def test_del_last_group(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_del_1"))
        gen.group.create(Group(name="for_del_2"))
        gen.group.create(Group(name="for_del_3"))
    old_group_list = db.get_group_list(sorted=True)
    gen.group.del_last()
    assert len(old_group_list) - 1 == len(db.get_group_list())
    new_group_list = db.get_group_list()
    old_group_list[-1:] = []
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)


def test_del_without_choice_group(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_del_1"))
        gen.group.create(Group(name="for_del_2"))
    old_group_list = db.get_group_list()
    gen.group.del_not_choose()
    new_group_list = db.get_group_list()
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)


def test_del_some_group(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_del"))
    old_group_list = db.get_group_list()
    group = random.choice(old_group_list)
    gen.group.del_by_id(group.id)
    new_group_list = db.get_group_list()
    assert len(old_group_list) - 1 == len(new_group_list)
    old_group_list.remove(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)
