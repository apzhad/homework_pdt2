from model.contact import Contact
from model.group import Group


def test_edit_first_contact(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="modify"))
    gen.contact.edit_first(Contact(first_name="new_name", middle_name="new_middle_name", last_name="lastname",
                                   nickname="nick", title="title234", company="company2", address="address12",
                                   home_phone="home", mobile_phone="mobile", work_phone="work",
                                   fax="fax123", primary_email="email_pri", secondary_email="",
                                   third_email="", homepage="home", birth_day="4",
                                   birth_month="July", birth_year="1978", anniversary_day="9",
                                   anniversary_month="May", anniversary_year="2008",
                                   secondary_address="sec_addr", secondary_home_phone="",
                                   notes="s jv s\njsbej", photo_path="\\tests\\test_data\\3.png"))


def test_edit_first_contact_without_change(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="modify", last_name="status"))
    gen.contact.edit_first_wo_change()


def test_edit_first_contact_in_group(gen):
    group = "new_name"
    if group not in gen.group.get_group_list() and group != "[all]" and group != "[none]":
        gen.group.create(group=Group(name=group))
    if gen.contact.get_contact_count(group_name=group) == 0:
        gen.contact.create(Contact(first_name="modify", last_name="status", group_name=group))
    gen.contact.add_to_group(group_name=group)


def test_edit_first_contact_from_details(gen):
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="modify", last_name="status"))
    gen.contact.edit_first_from_details(Contact(first_name="name", middle_name="middle", last_name="last",
                                                nickname="", title="", company="cmp", address="none",
                                                home_phone="32445", mobile_phone="", work_phone="763728",
                                                fax="", primary_email="", secondary_email="", third_email="",
                                                homepage="", birth_day="-", birth_month="-", birth_year="",
                                                anniversary_day="-", anniversary_month="-", anniversary_year="",
                                                group_name="", secondary_address="", secondary_home_phone="",
                                                notes="", del_foto=True))


def test_add_all_contacts_to_group(gen):
    group = "new_name"
    if group not in gen.group.get_group_list() and group != "[all]" and group != "[none]":
        gen.group.create(group=Group(name=group))
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="modify", last_name="change_group", group_name=group))
        gen.contact.create(Contact(first_name="modify_1", last_name="change_group_1", group_name="[none]"))
        gen.contact.create(Contact(first_name="modify_2", last_name="change_group_2"))
    gen.contact.add_to_group(group_name=group)


def test_add_to_group_without_select_contact(gen):
    group = "new_name"
    if group not in gen.group.get_group_list() and group != "[all]" and group != "[none]":
        gen.group.create(group=Group(name=group))
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="modify", last_name="change_group"))
    gen.contact.add_to_group(group_name=group)


def test_add_contacts_to_group_from_another_group(gen):
    group_from = "new_name"
    group_to = "last_name"
    if group_from not in gen.group.get_group_list() and group_from != "[all]" and group_from != "[none]":
        gen.group.create(group=Group(name=group_from))
    if group_to not in gen.group.get_group_list() and group_to != "[all]" and group_to != "[none]":
        gen.group.create(group=Group(name=group_to))
    if gen.contact.get_contact_count() == 0:
        gen.contact.create(Contact(first_name="modify", last_name="change_group", group_name=group_from))
    gen.contact.add_to_group_from_another(group_from=group_from, group_to=group_to)


def test_remove_contact_from_group(gen):
    group = "last_name"
    if group not in gen.group.get_group_list() and group != "[all]" and group != "[none]":
        gen.group.create(group=Group(name=group))
    if gen.contact.get_contact_count(group_name=group) == 0:
        gen.contact.create(Contact(first_name="modify", last_name="change_group", group_name=group))
    gen.contact.remove_from_group(group_name=group)


def test_edit_first_found_contact(gen):
    search = "modify"
    if gen.contact.get_result_count(search) == 0:
        gen.contact.create(Contact(first_name=search, fax="573-092", nickname="1"))

    gen.contact.edit_first_found(search=search,
                                 contact=Contact(first_name="sbcghdhj", middle_name="j,lk", last_name="cgxh",
                                                 nickname="", title="dfg", company="lkg", address="",
                                                 home_phone="", work_phone="", fax="", homepage="", birth_day="22",
                                                 birth_month="April", birth_year="1234", anniversary_day="3",
                                                 anniversary_month="May", anniversary_year="77",
                                                 group_name="", secondary_address="dfg", secondary_home_phone="55",
                                                 notes="group"))
