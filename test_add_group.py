# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group
from generic import Generic


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.gen = Generic()

    def test_add_group(self):
        self.gen.login(username="admin", password="secret")
        self.gen.create_new_group(Group(name="new_group", header="header_group", footer="first_group"))
        self.gen.logout()

    def test_add_empty_group(self):
        self.gen.login(username="admin", password="secret")
        self.gen.create_new_group(Group(name="", header="", footer=""))
        self.gen.logout()

    def tearDown(self):
        self.gen.finish()

    def is_element_present(self, how, what):
        try: self.gen.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.gen.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True


if __name__ == "__main__":
    unittest.main()
