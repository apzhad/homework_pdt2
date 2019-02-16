# -*- coding: utf-8 -*-
import unittest
from contact import Contact

from generic import Generic


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.gen = Generic()

    def test_add_contact(self):
        self.gen.login(username="admin", password="secret")
        self.gen.create_contact(Contact(first_name="first_name", middle_name="middle_name", last_name="last_name",
                                    nickname="nickname", title="title", company="company", address="address",
                                    home_phone="homephone", mobile_phone="mobilephone", work_phone="workphone",
                                    fax="fax", primary_email="email", secondary_email="email2",
                                    third_email="email3", homepage="homepage", birth_day="5", birth_month="January",
                                    birth_year="1950", anniversary_day="15", anniversary_month="June",
                                    anniversary_year="2000", group_name="[none]",
                                    secondary_address="address secondary", secondary_home_phone="home secondary",
                                    notes="notes", photo_path="\\test_data\\cat.jpg"))
        self.gen.logout()

    def tearDown(self):
        self.gen.finish()


if __name__ == "__main__":
    unittest.main()
