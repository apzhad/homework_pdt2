from model.contact import Contact
from model.group import Group


def test_del_first_contact(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = gen.contact.get_contact_list()
    gen.contact.del_first()
    new_contact_list = gen.contact.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact_list)
    old_contact_list[0:1] = []
    assert old_contact_list == new_contact_list


def test_cancel_del_first_contact(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = gen.contact.get_contact_list()
    gen.contact.cancel_del_first()
    new_contact_list = gen.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)
    assert old_contact_list == new_contact_list


def test_del_all_contacts_select(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="2"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="3"))
    gen.contact.del_by_select_all()
    new_contact_list = gen.contact.get_contact_list()
    assert 0 == len(new_contact_list)
    assert [] == new_contact_list


def test_del_all_contacts_click(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="2"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="3"))
    gen.contact.del_all_by_click()
    new_contact_list = gen.contact.get_contact_list()
    assert 0 == len(new_contact_list)
    assert [] == new_contact_list


def test_del_unselected_contact(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = gen.contact.get_contact_list()
    gen.contact.del_unselected()
    new_contact_list = gen.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)
    assert old_contact_list == new_contact_list


def test_del_all_contacts_from_group(gen):
    group = "new_name"
    if group not in str(gen.group.get_group_list()) and group != "[all]" and group != "[none]":
        gen.group.create(group=Group(name=group))
    if gen.contact.get_contact_count(group_name=group) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1", group_name=group))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="2", group_name=group))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="3", group_name=group))
    gen.contact.del_all_from_group(group_name=group)
    new_contact_list = gen.contact.get_contact_list(group_name=group)
    assert 0 == len(new_contact_list)
    assert [] == new_contact_list


def test_del_first_contact_from_group(gen):
    group = "[none]"
    if group not in str(gen.group.get_group_list()) and group != "[all]" and group != "[none]":
        gen.group.create(group=Group(name=group))
    if gen.contact.get_contact_count(group_name=group) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1", group_name=group))
    old_contact_list = gen.contact.get_contact_list(group_name=group)
    gen.contact.del_first_from_group(group_name=group)
    new_contact_list = gen.contact.get_contact_list(group_name=group)
    assert len(old_contact_list) - 1 == len(new_contact_list)
    old_contact_list[0:1] = []
    assert old_contact_list == new_contact_list


def test_del_first_contact_using_edit(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = gen.contact.get_contact_list()
    gen.contact.del_first_using_edit()
    new_contact_list = gen.contact.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact_list)
    old_contact_list[0:1] = []
    assert old_contact_list == new_contact_list


def test_del_all_search_result(gen):
    search = "lastname"
    if gen.contact.get_result_count(search=search) == 0:
        gen.contact.create(Contact(first_name="lastname", fax="573-092", nickname="1"))
        gen.contact.create(Contact(first_name="test", fax="573-092", nickname="lastname"))
        gen.contact.create(Contact(middle_name="lastname", fax="573-092", nickname="1"))
        gen.contact.create(Contact(last_name="lastname", fax="573-092", nickname="1"))
    search_count = gen.contact.get_result_count(search=search)
    old_contact_list = gen.contact.get_contact_list()
    gen.contact.del_all_found(search)
    new_contact_list = gen.contact.get_contact_list()
    assert len(old_contact_list) - search_count == len(new_contact_list)
