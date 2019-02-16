# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.generic import Generic


@pytest.fixture
def gen(request):
    fixture = Generic()
    request.addfinalizer(fixture.finish)
    return fixture


def test_add_contact(gen):
    gen.login(username="admin", password="secret")
    gen.create_contact(Contact(first_name="first_name", middle_name="middle_name", last_name="last_name",
                               nickname="nickname", title="title", company="company", address="address",
                               home_phone="homephone", mobile_phone="mobilephone", work_phone="workphone",
                               fax="fax", primary_email="email", secondary_email="email2",
                               third_email="email3", homepage="homepage", birth_day="5", birth_month="January",
                               birth_year="1950", anniversary_day="15", anniversary_month="June",
                               anniversary_year="2000", group_name="[none]",
                               secondary_address="address secondary", secondary_home_phone="home secondary",
                               notes="notes", photo_path="\\test_data\\cat.jpg"))
    gen.logout()
