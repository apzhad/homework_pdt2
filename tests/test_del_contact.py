from model.contact import Contact
from model.group import Group


def test_del_first_contact(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    gen.contact.del_first()


def test_cancel_del_first_contact(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    gen.contact.cancel_del_first()


def test_del_all_contacts_select(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="2"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="3"))
    gen.contact.del_by_select_all()


def test_del_all_contacts_click(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="2"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="3"))
    gen.contact.del_all_by_click()


def test_del_unselected_contact(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    gen.contact.del_unselected()


def test_del_all_contacts_from_group(gen):
    group = "new_name"
    if group not in gen.group.get_group_list() and group != "[all]" and group != "[none]":
        gen.group.create(group=Group(name=group))
    if gen.contact.get_contact_count(group_name=group) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1", group_name=group))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="2", group_name=group))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="3", group_name=group))
    gen.contact.del_all_from_group(group_name=group)


def test_del_first_contact_from_group(gen):
    group = "[none]"
    if group not in gen.group.get_group_list() and group != "[all]" and group != "[none]":
        gen.group.create(group=Group(name=group))
    if gen.contact.get_contact_count(group_name=group) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1", group_name=group))
    gen.contact.del_first_from_group(group_name=group)


def test_del_first_contact_using_edit(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    gen.contact.del_first_using_edit()


def test_del_all_search_result(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="lastname", fax="573-092", nickname="1"))
        gen.contact.create(Contact(first_name="test", fax="573-092", nickname="lastname"))
        gen.contact.create(Contact(middle_name="lastname", fax="573-092", nickname="1"))
        gen.contact.create(Contact(last_name="lastname", fax="573-092", nickname="1"))
    gen.contact.del_all_found("lastname")
