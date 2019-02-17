from model.contact import Contact


def test_edit_first_contact(gen):
    gen.session.login(username="admin", password="secret")
    gen.contact.edit_first(Contact(first_name="new_name", middle_name="new_middle_name", last_name="lastname",
                                   nickname="nick", title="title234", company="company2", address="address12",
                                   home_phone="home", mobile_phone="mobile", work_phone="work",
                                   fax="fax123", primary_email="email_pri", secondary_email="",
                                   third_email="", homepage="home", birth_day="4",
                                   birth_month="July", birth_year="1978", anniversary_day="9",
                                   anniversary_month="May", anniversary_year="2008", group_name="",
                                   secondary_address="sec_addr", secondary_home_phone="",
                                   notes="s jv s\njsbej", photo_path="\\tests\\test_data\\3.png"))
    gen.session.logout()


def test_edit_first_contact_without_change(gen):
    gen.session.login(username="admin", password="secret")
    gen.contact.edit_first_wo_change()
    gen.session.logout()


def test_edit_first_contact_from_details(gen):
    gen.session.login(username="admin", password="secret")
    gen.contact.edit_first_from_details(Contact(first_name="name", middle_name="middle", last_name="last",
                                                nickname="", title="", company="cmp", address="none",
                                                home_phone="32445", mobile_phone="", work_phone="763728",
                                                fax="", primary_email="", secondary_email="", third_email="",
                                                homepage="", birth_day="-", birth_month="-", birth_year="",
                                                anniversary_day="-", anniversary_month="-", anniversary_year="",
                                                group_name="", secondary_address="", secondary_home_phone="",
                                                notes="", photo_path="\\tests\\test_data\\3.png"))
    gen.session.logout()
