
def test_del_first_contact(gen):
    gen.contact.del_first()


def test_cancel_del_first_contact(gen):
    gen.contact.cancel_del_first()


def test_del_all_contacts_select(gen):
    gen.contact.del_by_select_all()


def test_del_all_contacts_click(gen):
    gen.contact.del_all_by_click()


def test_del_unselected_contact(gen):
    gen.contact.del_unselected()


def test_del_all_contacts_from_group(gen):
    gen.contact.del_all_from_group(group_name="new_name")


def test_del_first_contact_from_group(gen):
    gen.contact.del_first_from_group(group_name="[none]")


def test_del_first_contact_using_edit(gen):
    gen.contact.del_first_using_edit()


def test_del_all_search_result(gen):
    gen.contact.del_all_found("lastname")
