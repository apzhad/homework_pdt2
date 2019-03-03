from model.contact import Contact
from model.group import Group
from random import randrange


def test_del_first_contact(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = gen.contact.get_contact_list()
    gen.contact.del_first()
    assert len(old_contact_list) - 1 == gen.contact.get_contact_count()
    new_contact_list = gen.contact.get_contact_list()
    old_contact_list[0:1] = []
    assert old_contact_list == new_contact_list


def test_del_some_contact(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = gen.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    gen.contact.del_by_index(index)
    assert len(old_contact_list) - 1 == gen.contact.get_contact_count()
    new_contact_list = gen.contact.get_contact_list()
    old_contact_list[index:index+1] = []
    assert old_contact_list == new_contact_list


def test_cancel_del_first_contact(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = gen.contact.get_contact_list()
    gen.contact.cancel_del_first()
    assert len(old_contact_list) == gen.contact.get_contact_count()
    new_contact_list = gen.contact.get_contact_list()
    assert old_contact_list == new_contact_list


def test_cancel_del_some_contact(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = gen.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    gen.contact.cancel_del_by_index(index)
    assert len(old_contact_list) == gen.contact.get_contact_count()
    new_contact_list = gen.contact.get_contact_list()
    assert old_contact_list == new_contact_list


def test_del_all_contacts_select(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="2"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="3"))
    gen.contact.del_by_select_all()
    assert 0 == gen.contact.get_contact_count()
    new_contact_list = gen.contact.get_contact_list()
    assert [] == new_contact_list


def test_del_all_contacts_click(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="2"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="3"))
    gen.contact.del_all_by_click()
    assert 0 == gen.contact.get_contact_count()
    new_contact_list = gen.contact.get_contact_list()
    assert [] == new_contact_list


def test_del_unselected_contact(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = gen.contact.get_contact_list()
    gen.contact.del_unselected()
    assert len(old_contact_list) == gen.contact.get_contact_count()
    new_contact_list = gen.contact.get_contact_list()
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
    assert 0 == gen.contact.get_contact_count(group)
    new_contact_list = gen.contact.get_contact_list(group_name=group)
    assert [] == new_contact_list


def test_del_first_contact_from_group(gen):
    group = "group"
    if group not in str(gen.group.get_group_list()) and group != "[all]" and group != "[none]":
        gen.group.create(group=Group(name=group))
    if gen.contact.get_contact_count(group_name=group) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1", group_name=group))
    old_contact_list = gen.contact.get_contact_list(group_name=group)
    gen.contact.del_first_from_group(group_name=group)
    assert len(old_contact_list) - 1 == gen.contact.get_contact_count(group_name=group)
    new_contact_list = gen.contact.get_contact_list(group_name=group)
    old_contact_list[0:1] = []
    assert old_contact_list == new_contact_list


def test_del_some_contact_from_group(gen):
    group = "group"
    if group not in str(gen.group.get_group_list()) and group != "[all]" and group != "[none]":
        gen.group.create(group=Group(name=group))
    if gen.contact.get_contact_count(group_name=group) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1", group_name=group))
    old_contact_list = gen.contact.get_contact_list(group_name=group)
    index = randrange(len(old_contact_list))
    gen.contact.del_from_group_by_index(index=index, group_name=group)
    assert len(old_contact_list) - 1 == gen.contact.get_contact_count(group_name=group)
    new_contact_list = gen.contact.get_contact_list(group_name=group)
    old_contact_list[index:index+1] = []
    assert old_contact_list == new_contact_list


def test_del_first_contact_using_edit(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = gen.contact.get_contact_list()
    gen.contact.del_first_using_edit()
    assert len(old_contact_list) - 1 == gen.contact.get_contact_count()
    new_contact_list = gen.contact.get_contact_list()
    old_contact_list[0:1] = []
    assert old_contact_list == new_contact_list


def test_del_some_contact_using_edit(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = gen.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    gen.contact.del_using_edit_by_index(index)
    assert len(old_contact_list) - 1 == gen.contact.get_contact_count()
    new_contact_list = gen.contact.get_contact_list()
    old_contact_list[index:index+1] = []
    assert old_contact_list == new_contact_list


def test_del_all_search_result(gen):
    search = "lastname"
    if gen.contact.get_result_count(search=search) == 0:
        gen.contact.create(Contact(first_name="lastname", fax="573-092", nickname="1"))
        gen.contact.create(Contact(first_name="test", fax="573-092", nickname="lastname"))
        gen.contact.create(Contact(middle_name="lastname", fax="573-092", nickname="1"))
        gen.contact.create(Contact(last_name="lastname", fax="573-092", nickname="1"))
    # search_count = gen.contact.get_result_count(search=search)
    # old_contact_list = gen.contact.get_contact_list()
    gen.contact.del_all_found(search)
    assert 0 == gen.contact.get_result_count(search)
    # new_contact_list = gen.contact.get_contact_list()
