
def test_del_first_contact(gen):
    gen.session.login(username="admin", password="secret")
    gen.contact.del_first()
    gen.session.logout()


def test_cancel_del_first_contact(gen):
    gen.session.login(username="admin", password="secret")
    gen.contact.cancel_del_first()
    gen.session.logout()


def test_del_all_contacts_select(gen):
    gen.session.login(username="admin", password="secret")
    gen.contact.del_by_select_all()
    gen.session.logout()


def test_del_all_contacts_click(gen):
    gen.session.login(username="admin", password="secret")
    gen.contact.del_all_by_click()
    gen.session.logout()


def test_del_unselected_contact(gen):
    gen.session.login(username="admin", password="secret")
    gen.contact.del_unselected()
    gen.session.logout()
