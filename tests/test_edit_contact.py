from model.contact import Contact


def test_edit_first_contact(gen):
    gen.session.login(username="admin", password="secret")
    gen.contact.edit_first_contact(Contact(first_name="new_name", middle_name="new_middle_name", last_name="lastname",
                                           nickname="nick", title="title234", company="company2", address="address12",
                                           home_phone="home", mobile_phone="mobile", work_phone="work",
                                           fax="fax123", primary_email="email_pri", secondary_email="",
                                           third_email="", homepage="home", birth_day="4",
                                           birth_month="July", birth_year="1978", anniversary_day="9",
                                           anniversary_month="May", anniversary_year="2008", group_name="new_name",
                                           secondary_address="sec_addr", secondary_home_phone="",
                                           notes="s jv s\njsbej", photo_path="\\tests\\test_data\\3.png"))
    gen.session.logout()
