from model.group import Group


def test_edit_first_group(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.edit_first(Group(name="new_name", header="new_header_group", footer="changed_group"))
    gen.session.logout()


def test_clear_first_group_params(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.edit_first(Group(name="", header="", footer=""))
    gen.session.logout()


def test_update_first_group_without_changes(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.update_first_wo_change()
    gen.session.logout()


def test_update_all_groups(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.edit_all(Group(name="some_name", header="some_header_group", footer="changed_group"))
    gen.session.logout()


def test_update_all_groups_without_changes(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.edit_all_wo_change()
    gen.session.logout()


def test_update_last_group(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.edit_last(Group(name="last_name", header="last_header_group", footer="last_group"))
    gen.session.logout()


def test_update_last_group_without_changes(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.update_last_wo_change()
    gen.session.logout()
