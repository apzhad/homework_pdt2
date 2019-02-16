# -*- coding: utf-8 -*-


class SessionManage:

    def __init__(self, gen):
        self.gen = gen

    def login(self, username, password):
        wd = self.gen.wd
        self.gen.open_home_page()
        # enter username and password for login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        # login
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.gen.wd
        wd.find_element_by_link_text("Logout").click()
