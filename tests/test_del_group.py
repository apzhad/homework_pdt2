
def test_del_first_group(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.del_first()
    gen.session.logout()


def test_del_all_group(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.del_all()
    gen.session.logout()


def test_del_last_group(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.del_last()
    gen.session.logout()


def test_del_without_choice_group(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.del_not_choose()
    gen.session.logout()
