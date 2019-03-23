from model.group import Group
import random


def find_index(group, id):
    index = 0
    for gr in group:
        if gr.id == id:
            break
        index += 1
    return index


def test_edit_first_group(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_edit"))
    old_group_list = db.get_group_list(sorted=True)
    group = Group(name="new_name", header="new_header_group", footer="changed_group")
    group.id = old_group_list[0].id
    gen.group.edit_first(group)
    assert len(old_group_list) == len(db.get_group_list())
    new_group_list = db.get_group_list()
    old_group_list[0] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)


def test_edit_some_group(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_edit"))
    old_group_list = db.get_group_list()
    gid = random.choice(old_group_list).id
    index = find_index(group=old_group_list, id=gid)
    group = Group(id=gid, name="edit_some", header="group")
    gen.group.edit_by_id(gid, group)
    assert len(old_group_list) == len(db.get_group_list())
    new_group_list = db.get_group_list()
    old_group_list[index] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)


def test_clear_first_group_params(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
    old_group_list = db.get_group_list(sorted=True)
    group = Group(name="", header="", footer="")
    group.id = old_group_list[0].id
    gen.group.edit_first(group)
    assert len(old_group_list) == len(db.get_group_list())
    new_group_list = db.get_group_list()
    old_group_list[0] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)


def test_clear_some_group_params(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
    old_group_list = db.get_group_list()
    gid = random.choice(old_group_list).id
    group = Group(id=gid, name="", header="", footer="")
    index = find_index(old_group_list, gid)
    gen.group.edit_by_id(id=gid, group=group)
    assert len(old_group_list) == len(db.get_group_list())
    new_group_list = db.get_group_list()
    old_group_list[index] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)


def test_update_first_group_without_changes(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
    old_group_list = db.get_group_list()
    gen.group.update_first_wo_change()
    assert len(old_group_list) == len(db.get_group_list())
    new_group_list = db.get_group_list()
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)


def test_update_some_group_without_changes(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
    old_group_list = db.get_group_list()
    group = random.choice(old_group_list)
    gen.group.update_wo_change_by_id(group.id)
    assert len(old_group_list) == len(db.get_group_list())
    new_group_list = db.get_group_list()
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)


def test_update_all_groups(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
        gen.group.create(Group(name="for_edit_1", header="header_1", footer="footer_1"))
        gen.group.create(Group(name="for_edit_2", header="header_2", footer="footer_2"))
    old_group_list = db.get_group_list(sorted=True)
    group = Group(name="some_name", header="some_header_group", footer="changed_group")
    group.id = old_group_list[0].id
    gen.group.edit_all(group)
    assert len(old_group_list) == len(db.get_group_list())
    new_group_list = db.get_group_list()
    old_group_list[0] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)


def test_update_all_groups_without_changes(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
        gen.group.create(Group(name="for_edit_1", header="header_1", footer="footer_1"))
        gen.group.create(Group(name="for_edit_2", header="header_2", footer="footer_2"))
    old_group_list = db.get_group_list()
    gen.group.edit_all_wo_change()
    assert len(old_group_list) == len(db.get_group_list())
    new_group_list = db.get_group_list()
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)


def test_update_last_group(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
        gen.group.create(Group(name="for_edit_1", header="header_1", footer="footer_1"))
    old_group_list = db.get_group_list(sorted=True)
    group = Group(name="last_name", header="last_header_group", footer="last_group")
    group.id = old_group_list[-1].id
    gen.group.edit_last(group)
    assert len(old_group_list) == len(db.get_group_list())
    new_group_list = db.get_group_list()
    old_group_list[-1] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)


def test_update_last_group_without_changes(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
        gen.group.create(Group(name="for_edit_1", header="header_1", footer="footer_1"))
    old_group_list = db.get_group_list(sorted=True)
    gen.group.update_last_wo_change()
    assert len(old_group_list) == len(db.get_group_list())
    new_group_list = db.get_group_list()
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)


def test_edit_first_group_name(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
    old_group_list = db.get_group_list(sorted=True)
    group = Group(name="only_name")
    group.id = old_group_list[0].id
    gen.group.edit_first(group)
    assert len(old_group_list) == len(db.get_group_list())
    new_group_list = db.get_group_list()
    old_group_list[0] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)


def test_edit_some_group_name(gen, db, check_ui):
    if len(db.get_group_list()) == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
    old_group_list = db.get_group_list()
    gid = random.choice(old_group_list).id
    group = Group(id=gid, name="only_name")
    index = find_index(old_group_list, gid)
    gen.group.edit_by_id(gid, group)
    assert len(old_group_list) == len(db.get_group_list())
    new_group_list = db.get_group_list()
    old_group_list[index] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max) == sorted(gen.group.get_group_list(), key=Group.id_or_max)
