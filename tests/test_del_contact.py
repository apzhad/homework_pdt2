from model.contact import Contact
import random


def test_del_first_contact(gen, check_ui, db):
    if len(db.get_contact_list()) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = db.get_contact_list(sorted=True)
    gen.contact.del_first()
    assert len(old_contact_list) - 1 == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    old_contact_list[0:1] = []
    assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_del_some_contact(gen, db, check_ui):
    if len(db.get_contact_list()) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = db.get_contact_list()
    cid = int(random.choice(old_contact_list).id)
    gen.contact.del_by_id(cid)
    assert len(old_contact_list) - 1 == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    old_contact_list[cid:cid+1] = []
    assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_cancel_del_first_contact(gen, db, check_ui):
    if len(db.get_contact_list()) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = db.get_contact_list()
    gen.contact.cancel_del_first()
    assert len(old_contact_list) == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_cancel_del_some_contact(gen, db, check_ui):
    if len(db.get_contact_list()) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = db.get_contact_list()
    cid = int(random.choice(old_contact_list).id)
    gen.contact.cancel_del_by_id(cid)
    assert len(old_contact_list) == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_del_all_contacts_select(gen, db, check_ui):
    if len(db.get_contact_list()) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="2"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="3"))
    gen.contact.del_by_select_all()
    assert 0 == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    assert [] == new_contact_list
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_del_all_contacts_click(gen, db, check_ui):
    if len(db.get_contact_list()) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="2"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="3"))
    gen.contact.del_all_by_click()
    assert 0 == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    assert [] == new_contact_list
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_del_unselected_contact(gen, db, check_ui):
    if len(db.get_contact_list()) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = db.get_contact_list()
    gen.contact.del_unselected()
    assert len(old_contact_list) == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_del_all_contacts_from_group(gen, orm, check_ui):
    group = random.choice(orm.get_group_list())
    if len(orm.get_contact_in_group(group=group)) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1", group_name=group.id))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="2", group_name=group.id))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="3", group_name=group.id))
    gen.contact.del_all_from_group(group_id=group.id)
    assert 0 == len(orm.get_contact_in_group(group=group))
    new_contact_list = orm.get_contact_in_group(group=group)
    assert [] == new_contact_list
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(
            gen.contact.get_contact_list(group_id=group.id), key=Contact.id_or_max)


def test_del_first_contact_from_group(gen, orm, check_ui):
    group = random.choice(orm.get_group_list())
    if len(orm.get_contact_in_group(group=group)) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1", group_name=group.id))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="2", group_name=group.id))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="3", group_name=group.id))
    old_contact_list = orm.get_contact_in_group(group=group, sorted=True)
    gen.contact.del_first_from_group(group_name=group.id)
    assert len(old_contact_list) - 1 == len(orm.get_contact_in_group(group=group))
    new_contact_list = orm.get_contact_in_group(group=group)
    old_contact_list[0:1] = []
    assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(
            gen.contact.get_contact_list(group_id=group.id), key=Contact.id_or_max)


def test_del_some_contact_from_group(gen, orm, check_ui):
    group = random.choice(orm.get_group_list())
    if len(orm.get_contact_in_group(group=group)) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1", group_name=group.id))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1", group_name=group.id))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1", group_name=group.id))
    old_contact_list = orm.get_contact_in_group(group=group)
    contact = random.choice(old_contact_list)
    gen.contact.del_from_group_by_id(contact_id=contact.id, group_id=group.id)
    assert len(old_contact_list) - 1 == len(orm.get_contact_in_group(group=group))
    new_contact_list = orm.get_contact_in_group(group=group)
    old_contact_list.remove(contact)
    assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(
            gen.contact.get_contact_list(group_id=group.id), key=Contact.id_or_max)


def test_del_first_contact_using_edit(gen, db, check_ui):
    if len(db.get_contact_list()) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = db.get_contact_list(sorted=True)
    gen.contact.del_first_using_edit()
    assert len(old_contact_list) - 1 == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    old_contact_list[0:1] = []
    assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_del_some_contact_using_edit(gen, db, check_ui):
    if len(db.get_contact_list()) == 0:
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
        gen.contact.create(Contact(first_name="del_contact", fax="573-092", nickname="1"))
    old_contact_list = db.get_contact_list()
    cid = int(random.choice(old_contact_list).id)
    gen.contact.del_using_edit_by_id(cid)
    assert len(old_contact_list) - 1 == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    old_contact_list[cid:cid+1] = []
    assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


"""
Commented while search method in database not found
def test_del_all_search_result(gen, db, check_ui):
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
"""
