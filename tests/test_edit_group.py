from model.group import Group


def test_edit_first_group(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.edit_first(Group(name="new_name", header="new_header_group", footer="changed_group"))
    gen.session.logout()
