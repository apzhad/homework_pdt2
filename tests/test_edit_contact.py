from model.contact import Contact


def test_edit_first_contact(gen):
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
    gen.contact.edit_first_wo_change()


def test_edit_first_contact_in_group(gen):
    gen.contact.add_to_group(group_name="new_name")


def test_edit_first_contact_from_details(gen):
    gen.contact.edit_first_from_details(Contact(first_name="name", middle_name="middle", last_name="last",
                                                nickname="", title="", company="cmp", address="none",
                                                home_phone="32445", mobile_phone="", work_phone="763728",
                                                fax="", primary_email="", secondary_email="", third_email="",
                                                homepage="", birth_day="-", birth_month="-", birth_year="",
                                                anniversary_day="-", anniversary_month="-", anniversary_year="",
                                                group_name="", secondary_address="", secondary_home_phone="",
                                                notes="", del_foto=True))


def test_add_all_contacts_to_group(gen):
    gen.contact.add_to_group(group_name="new_name")


def test_add_to_group_without_select_contact(gen):
    gen.contact.add_to_group(group_name="new_name")


def test_add_contacts_to_group_from_another_group(gen):
    gen.contact.add_to_group_from_another(group_from="new_name", group_to="last_name")


def test_remove_contact_from_group(gen):
    gen.contact.remove_from_group(group_name="last_name")


def test_edit_first_found_contact(gen):
    gen.contact.edit_first_found(search="name",
                                 contact=Contact(first_name="sbcghdhj", middle_name="j,lk", last_name="cgxh",
                                                 nickname="", title="dfg", company="lkg", address="",
                                                 home_phone="", mobile_phone="", work_phone="",
                                                 fax="", primary_email="", secondary_email="", third_email="",
                                                 homepage="", birth_day="22", birth_month="April", birth_year="1234",
                                                 anniversary_day="3", anniversary_month="May", anniversary_year="77",
                                                 group_name="", secondary_address="dfg", secondary_home_phone="55",
                                                 notes="group", photo_path=""))
