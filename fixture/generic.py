# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionManage
from fixture.group import GroupManage
from fixture.contact import ContactManage


class Generic:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(1)
        self.session = SessionManage(self)
        self.group = GroupManage(self)
        self.contact = ContactManage(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def finish(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
