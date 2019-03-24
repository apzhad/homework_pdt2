from model.contact import Contact
from model.group import Group
import random


def find_index(contacts, id):
    index = 0
    for c in contacts:
        if c.id == id:
            break
        index += 1
    return index


def test_edit_first_contact(gen, check_ui, db):
    if len(db.get_contact_list()) == 0:
        gen.contact.create(Contact(first_name="modify"))
    old_contact_list = db.get_contact_list(sorted=True)
    cont = Contact(first_name="new_name", middle_name="new_middle_name", last_name="lastname",
                   nickname="nick", title="title234", company="company2", address="address12",
                   home_phone="home", mobile_phone="mobile", work_phone="work",
                   fax="fax123", primary_email="email_pri", secondary_email="",
                   third_email="", homepage="home", birth_day="4",
                   birth_month="July", birth_year="1978", anniversary_day="9",
                   anniversary_month="May", anniversary_year="2008",
                   secondary_address="sec_addr", secondary_home_phone="",
                   notes="s jv s\njsbej", photo_path="3.png")
    cont.id = old_contact_list[0].id
    gen.contact.edit_first(cont)
    assert len(old_contact_list) == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    old_contact_list[0] = cont
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_edit_some_contact(gen, check_ui, db):
    if len(db.get_contact_list()) == 0:
        gen.contact.create(Contact(first_name="modify"))
    old_contact_list = db.get_contact_list()
    cid = random.choice(old_contact_list).id
    cont = Contact(first_name="new_name", middle_name="new_middle_name", last_name="lastname",
                   nickname="nick", title="title234", company="company2", address="address12",
                   home_phone="home", mobile_phone="mobile", work_phone="work",
                   fax="fax123", primary_email="email_pri", secondary_email="",
                   third_email="", homepage="home", birth_day="4",
                   birth_month="July", birth_year="1978", anniversary_day="9",
                   anniversary_month="May", anniversary_year="2008",
                   secondary_address="sec_addr", secondary_home_phone="",
                   notes="s jv s\njsbej", photo_path="3.png", id=cid)
    gen.contact.edit_by_id(cid, cont)
    index = find_index(old_contact_list, cid)
    assert len(old_contact_list) == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    old_contact_list[index] = cont
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_edit_first_contact_without_change(gen, check_ui, db):
    if len(db.get_contact_list()) == 0:
        gen.contact.create(Contact(first_name="modify", last_name="status"))
    old_contact_list = db.get_contact_list(sorted=True)
    gen.contact.edit_first_wo_change()
    assert len(old_contact_list) == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_edit_some_contact_without_change(gen, check_ui, db):
    if len(db.get_contact_list()) == 0:
        gen.contact.create(Contact(first_name="modify", last_name="status"))
    old_contact_list = db.get_contact_list()
    cid = random.choice(old_contact_list).id
    gen.contact.edit_wo_change_by_id(cid)
    assert len(old_contact_list) == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_edit_first_contact_in_group(gen, check_ui, orm):
    group = orm.get_group_list()
    group = random.choice(group)
    if len(orm.get_contact_in_group(group=group)) == 0:
        gen.contact.create(Contact(first_name="modify", last_name="status", group_name=group.id))
    old_contact_list = orm.get_contact_in_group(group=group, sorted=True)
    cont = Contact(first_name="first", last_name="last", address="gjh")
    gen.contact.edit_first_in_group(group_name=group.id, contact=cont)
    assert len(old_contact_list) == len(orm.get_contact_in_group(group=group))
    new_contact_list = orm.get_contact_in_group(group=group)
    cont.id = old_contact_list[0].id
    old_contact_list[0] = cont
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_edit_some_contact_in_group(gen, check_ui, orm):
    group = random.choice(orm.get_group_list())
    if len(orm.get_contact_in_group(group=group)) == 0:
        gen.contact.create(Contact(first_name="modify", last_name="status", group_name=group.id))
    old_contact_list = orm.get_contact_in_group(group=group)
    cid = random.choice(old_contact_list).id
    cont = Contact(first_name="first", last_name="last", address="gjh", id=cid)
    gen.contact.edit_in_group_by_id(id=cid, group_id=group.id, contact=cont)
    assert len(old_contact_list) == len(orm.get_contact_in_group(group=group))
    index = find_index(old_contact_list, cid)
    new_contact_list = orm.get_contact_in_group(group=group)
    old_contact_list[index] = cont
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_edit_first_contact_from_details(gen, check_ui, db):
    if len(db.get_contact_list()) == 0:
        gen.contact.create(Contact(first_name="modify", last_name="status"))
    old_contact_list = db.get_contact_list(sorted=True)
    cont = Contact(first_name="name", middle_name="middle", last_name="last",
                   nickname="", title="", company="cmp", address="none",
                   home_phone="32445", mobile_phone="", work_phone="763728",
                   homepage="", birth_day="-", birth_month="-", birth_year="",
                   anniversary_day="-", anniversary_month="-", anniversary_year="",
                   group_name="", secondary_address="", secondary_home_phone="",
                   notes="", del_foto=True)
    cont.id = old_contact_list[0].id
    gen.contact.edit_first_from_details(cont)
    assert len(old_contact_list) == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    old_contact_list[0] = cont
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_edit_some_contact_from_details(gen, check_ui, db):
    if len(db.get_contact_list()) == 0:
        gen.contact.create(Contact(first_name="modify", last_name="status"))
    old_contact_list = db.get_contact_list()
    cid = random.choice(old_contact_list).id
    index = find_index(old_contact_list, cid)
    cont = Contact(first_name="name", middle_name="middle", last_name="last",
                   nickname="", title="", company="cmp", address="none",
                   home_phone="32445", mobile_phone="", work_phone="763728",
                   homepage="", birth_day="-", birth_month="-", birth_year="",
                   anniversary_day="-", anniversary_month="-", anniversary_year="",
                   group_name="", secondary_address="", secondary_home_phone="",
                   notes="", del_foto=True, id=cid)
    gen.contact.edit_from_details_by_id(cid, cont)
    assert len(old_contact_list) == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    old_contact_list[index] = cont
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)


def test_add_all_contacts_to_group(gen, check_ui, db):
    group = "new_name"
    if group not in gen.group.get_groups_names() and group != "[all]" and group != "[none]":
        gen.group.create(group=Group(name=group))
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="modify", last_name="change_group", group_name=group))
        gen.contact.create(Contact(first_name="modify_1", last_name="change_group_1", group_name="[none]"))
        gen.contact.create(Contact(first_name="modify_2", last_name="change_group_2"))
    old_contact_list = gen.contact.get_contact_list()
    gen.contact.add_all_to_group(group_name=group)
    assert len(old_contact_list) == gen.contact.get_contact_count()
    new_contact_list = gen.contact.get_contact_list(group_name=group)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


def test_add_to_group_without_select_contact(gen, check_ui, db):
    group = "new_name"
    if group not in gen.group.get_groups_names() and group != "[all]" and group != "[none]":
        gen.group.create(group=Group(name=group))
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="modify", last_name="change_group"))
    old_contact_list = gen.contact.get_contact_list(group_name=group)
    gen.contact.add_to_group_unselected(group_name=group)
    assert len(old_contact_list) == gen.contact.get_contact_count()
    new_contact_list = gen.contact.get_contact_list(group_name=group)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


def test_add_contacts_to_group_from_another_group(gen, check_ui, db):
    group_from = "new_name"
    group_to = "last_name"
    if group_from not in gen.group.get_groups_names() and group_from != "[all]" and group_from != "[none]":
        gen.group.create(group=Group(name=group_from))
    if group_to not in gen.group.get_groups_names() and group_to != "[all]" and group_to != "[none]":
        gen.group.create(group=Group(name=group_to))
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="modify", last_name="change_group", group_name=group_from))
    from_list = gen.contact.get_contact_list(group_name=group_from)
    old_to_list = gen.contact.get_contact_list(group_name=group_to)
    gen.contact.add_to_group_from_another(group_from=group_from, group_to=group_to)
    assert len(from_list) + len(old_to_list) == gen.contact.get_contact_count(group_name=group_to) or len(
        from_list) == gen.contact.get_contact_count(group_name=group_to)
    new_to_list = gen.contact.get_contact_list(group_name=group_to)
    if sorted(old_to_list, key=Contact.id_or_max) != sorted(new_to_list, key=Contact.id_or_max):
        old_to_list = old_to_list + from_list
        assert sorted(old_to_list, key=Contact.id_or_max) == sorted(new_to_list, key=Contact.id_or_max)


def test_remove_contact_from_group(gen, check_ui, db):
    group = "last_name"
    if group not in gen.group.get_groups_names() and group != "[all]" and group != "[none]":
        gen.group.create(group=Group(name=group))
    if gen.contact.get_contact_count(group_name=group) == 0:
        gen.contact.create(Contact(first_name="modify", last_name="change_group", group_name=group))
    gen.contact.remove_from_group(group_name=group)
    assert 0 == gen.contact.get_contact_count(group_name=group)
    cont_group_list = gen.contact.get_contact_list(group_name=group)
    assert [] == cont_group_list


def test_edit_first_found_contact(gen, check_ui, db):
    search = "modify"
    if gen.contact.get_result_count(search) == 0:
        gen.contact.create(Contact(first_name=search, fax="573-092", nickname="1"))
    old_contact_list = gen.contact.get_contact_list(search=search)
    cont = Contact(first_name="sbcghdhj", middle_name="j,lk", last_name="cgxh",
                   nickname="", title="dfg", company="lkg", address="",
                   home_phone="", work_phone="", fax="", homepage="", birth_day="22",
                   birth_month="April", birth_year="1234", anniversary_day="3",
                   anniversary_month="May", anniversary_year="77",
                   group_name="", secondary_address="dfg", secondary_home_phone="55",
                   notes="group")
    gen.contact.edit_first_found(search=search, contact=cont)
    cont.id = old_contact_list[0].id
    assert len(old_contact_list) == gen.contact.get_contact_count()
    new_contact_list = gen.contact.get_contact_list(search=cont.first_name)
    old_contact_list[0] = cont
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
