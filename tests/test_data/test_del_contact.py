
def test_del_first_contact(gen):
    gen.session.login(username="admin", password="secret")
    gen.contact.del_first()
    gen.session.logout()


def test_cancel_del_first_contact(gen):
    gen.session.login(username="admin", password="secret")
    gen.contact.cancel_del_first()
    gen.session.logout()


def test_del_all_contacts(gen):
    gen.session.login(username="admin", password="secret")
    gen.contact.del_all()
    gen.session.logout()
