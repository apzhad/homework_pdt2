# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import pytest
import string
import random
import re


def random_string(prefix, max_length):
    symbols = string.ascii_letters + string.digits + ' '*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


def random_string_with_eol(prefix, max_length):
    symbols = string.ascii_letters + string.digits + ' '*10 + '\n'*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


month = ("January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December")


test_data = [Contact(first_name="", last_name="")] + [
    Contact(first_name=random_string("first_name", 20), middle_name=random_string("middle_name", 5),
            last_name=random_string("last_name", 10), nickname=random_string("nickname", 10),
            title=random_string("title", 10), company=random_string("company", 10),
            address=random_string_with_eol("address", 20), home_phone=random_string("homephone", 15),
            fax=random_string("fax", 15), primary_email=random_string("email", 10))
    for i in range(3)
] + [
    Contact(first_name=random_string("first_name", 20), last_name=random_string("last_name", 10),
            title=random_string("title", 10), company=random_string("company", 10),
            mobile_phone=random_string("mobilephone", 15), work_phone=random_string("workphone", 15),
            secondary_email=random_string("email2", 10), third_email=random_string("email3", 10),
            homepage=random_string("homepage", 10))
    for m in range(3)
] + [
    Contact(first_name=random_string("first_name", 20), last_name=random_string("last_name", 10),
            address=random_string_with_eol("address", 20), home_phone=random_string("homephone", 15),
            birth_day=str(random.randint(1, 31)), birth_month=random.choice(month), birth_year=random_string("", 10),
            anniversary_day=str(random.randint(1, 31)), anniversary_month=random.choice(month),
            anniversary_year=random_string("", 10), secondary_address=random_string_with_eol("sec_address", 20))
    for j in range(3)
] + [
    Contact(first_name="", middle_name=random_string("middle_name", 5), last_name=random_string("last_name", 10),
            address=random_string_with_eol("address", 20), mobile_phone=random_string("mobilephone", 15),
            work_phone=random_string("workphone", 15), primary_email=random_string("email", 10),
            third_email=random_string("email3", 10), secondary_home_phone=random_string("sec_phone", 15),
            notes=random_string_with_eol("notes", 30), photo_path="\\tests\\test_data\\cat.jpg")
    for k in range(3)
]


def delete_whitespace(s):
    if len(s) > 0:
        s = re.sub('\s+', ' ', s)
        if s[-1] == " ":
            s = s[:-1]
    return s


def normalize_contact_for_check(contact):
    contact.first_name = delete_whitespace(contact.first_name)
    contact.last_name = delete_whitespace(contact.last_name)
    return contact


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(gen, contact):
    old_contact_list = gen.contact.get_contact_list()
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
                   secondary_home_phone="home secondary", notes="notes", photo_path="\\tests\\test_data\\cat.jpg")

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
