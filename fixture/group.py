# -*- coding: utf-8 -*-


class GroupManage:

    def __init__(self, gen):
        self.gen = gen

    def open_groups_page(self):
        wd = self.gen.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.gen.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.gen.wd
        self.open_groups_page()
        # init new group creation
        wd.find_element_by_name("new").click()
        # enter groups parameters
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation and return to group page
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def del_first(self):
        wd = self.gen.wd
        self.open_groups_page()
        # select group & submit deletion
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_first(self, group):
        wd = self.gen.wd
        self.open_groups_page()
        # select group & init editing
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        # change group parameters
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
