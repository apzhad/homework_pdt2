
def test_del_first_contact(gen):
    gen.session.login(username="admin", password="secret")
    gen.contact.del_first()
    gen.session.logout()
