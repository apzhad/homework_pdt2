
def test_del_first_group(gen):
    gen.session.login(username="admin", password="secret")
    gen.group.del_first()
    gen.session.logout()
