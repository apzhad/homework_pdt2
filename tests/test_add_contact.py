# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(gen):
    old_contact_list = gen.contact.get_contact_list()
    cont = Contact(first_name="first_name", middle_name="middle_name", last_name="last_name", nickname="nickname",
                   title="title", company="company", address="address", home_phone="homephone",
                   mobile_phone="mobilephone", work_phone="workphone", fax="fax", primary_email="email",
                   secondary_email="email2", third_email="email3", homepage="homepage", birth_day="5",
                   birth_month="January", birth_year="1950", anniversary_day="15", anniversary_month="June",
                   anniversary_year="2000", group_name="[none]",
                   secondary_address="address secondary", secondary_home_phone="home secondary",
                   notes="notes", photo_path="\\tests\\test_data\\cat.jpg")
    gen.contact.create(cont)
    new_contact_list = gen.contact.get_contact_list()
    assert len(old_contact_list) + 1 == len(new_contact_list)
    old_contact_list.append(cont)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


def test_add_contact_into_group(gen):
    old_contact_list = gen.contact.get_contact_list()
    cont = Contact(first_name="first_name", middle_name="middle_name", last_name="last_name", nickname="nickname",
                   title="title", company="company", address="address", home_phone="homephone",
                   mobile_phone="mobilephone", work_phone="workphone", fax="fax", primary_email="email",
                   secondary_email="email2", third_email="email3", homepage="homepage", birth_day="5",
                   birth_month="January", birth_year="1950", anniversary_day="15", anniversary_month="June",
                   anniversary_year="2000", group_name="new_name", secondary_address="address secondary",
                   secondary_home_phone="home secondary", notes="notes", photo_path="\\tests\\test_data\\cat.jpg")
    gen.contact.create(cont)
    new_contact_list = gen.contact.get_contact_list()
    assert len(old_contact_list) + 1 == len(new_contact_list)
    old_contact_list.append(cont)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


def test_add_empty_contact(gen):
    old_contact_list = gen.contact.get_contact_list()
    gen.contact.create_empty()
    new_contact_list = gen.contact.get_contact_list()
    assert len(old_contact_list) + 1 == len(new_contact_list)
    old_contact_list.append(Contact(first_name="", last_name=""))
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
