# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import re


month = ("January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December")


def delete_whitespace(s):
    if len(s) > 0:
        s = re.sub('\s+', ' ', s)
        if s[-1] == " ":
            s = s[:-1]
    return s


def normalize_contact_for_check(contact):
    if contact.first_name is not None:
        contact.first_name = delete_whitespace(contact.first_name)
    else:
        contact.first_name = ""
    if contact.last_name is not None:
        contact.last_name = delete_whitespace(contact.last_name)
    else:
        contact.last_name = ""
    return contact


def test_add_contact_using_module(gen, data_contacts):
    contact = data_contacts
    old_contact_list = gen.contact.get_contact_list()
    group = gen.group.get_groups_names() + ["[none]"]
    contact.group_name = random.choice(group)
    gen.contact.create(contact)
    assert len(old_contact_list) + 1 == gen.contact.get_contact_count()
    new_contact_list = gen.contact.get_contact_list()
    old_contact_list.append(normalize_contact_for_check(contact))
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


def test_add_contact_into_group(gen):
    group = gen.group.get_groups_names() + ["[none]"]
    old_contact_list = gen.contact.get_contact_list()
    cont = Contact(first_name="first_name ", middle_name="middle_name", last_name="last_name", nickname="nickname",
                   title="title", company="company", address="address", home_phone="homephone",
                   mobile_phone="mobilephone", work_phone="workphone", fax="fax", primary_email="email",
                   secondary_email="email2", third_email="email3", homepage="homepage", birth_day="1",
                   birth_month=random.choice(month), birth_year="1950", anniversary_day="15", anniversary_month="June",
                   anniversary_year="2000", secondary_address="address secondary",
                   secondary_home_phone="home secondary", notes="notes", photo_path="cat.jpg")
    cont.group_name = random.choice(group)
    gen.contact.create(cont)
    assert len(old_contact_list) + 1 == gen.contact.get_contact_count()
    new_contact_list = gen.contact.get_contact_list()
    old_contact_list.append(normalize_contact_for_check(cont))
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


def test_add_empty_contact(gen):
    old_contact_list = gen.contact.get_contact_list()
    gen.contact.create_empty()
    assert len(old_contact_list) + 1 == gen.contact.get_contact_count()
    new_contact_list = gen.contact.get_contact_list()
    old_contact_list.append(Contact(first_name="", last_name=""))
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
