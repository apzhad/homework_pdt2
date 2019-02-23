from model.group import Group


def test_edit_first_group(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit"))
    gen.group.edit_first(Group(name="new_name", header="new_header_group", footer="changed_group"))


def test_clear_first_group_params(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
    gen.group.edit_first(Group(name="", header="", footer=""))


def test_update_first_group_without_changes(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
    gen.group.update_first_wo_change()


def test_update_all_groups(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
        gen.group.create(Group(name="for_edit_1", header="header_1", footer="footer_1"))
        gen.group.create(Group(name="for_edit_2", header="header_2", footer="footer_2"))
    gen.group.edit_all(Group(name="some_name", header="some_header_group", footer="changed_group"))


def test_update_all_groups_without_changes(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
        gen.group.create(Group(name="for_edit_1", header="header_1", footer="footer_1"))
        gen.group.create(Group(name="for_edit_2", header="header_2", footer="footer_2"))
    gen.group.edit_all_wo_change()


def test_update_last_group(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
        gen.group.create(Group(name="for_edit_1", header="header_1", footer="footer_1"))
    gen.group.edit_last(Group(name="last_name", header="last_header_group", footer="last_group"))


def test_update_last_group_without_changes(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
        gen.group.create(Group(name="for_edit_1", header="header_1", footer="footer_1"))
    gen.group.update_last_wo_change()


def test_edit_first_group_name(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_edit", header="header", footer="footer"))
    gen.group.edit_first(Group(name="only_name"))
