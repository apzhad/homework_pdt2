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
        self.enter_group_parameters(group)
        # submit group creation and return to group page
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def enter_group_parameters(self, group):
        self.set_field_value("group_name", group.name)
        self.set_field_value("group_header", group.header)
        self.set_field_value("group_footer", group.footer)

    def set_field_value(self, field_name, text):
        if text is not None:
            wd = self.gen.wd
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def del_first(self):
        wd = self.gen.wd
        self.open_groups_page()
        # select group & submit deletion
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.gen.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first(self, group):
        wd = self.gen.wd
        self.open_groups_page()
        # select group & init editing
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        # change group parameters
        self.enter_group_parameters(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def update_first_wo_change(self):
        wd = self.gen.wd
        self.open_groups_page()
        # select group & init editing
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def del_all(self):
        wd = self.gen.wd
        self.open_groups_page()
        self.select_all_groups()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_all_groups(self):
        wd = self.gen.wd
        # get group count
        group_count = len(wd.find_elements_by_name("selected[]"))
        # select all groups
        for i in range(group_count):
            wd.find_element_by_xpath("(//input[@name='selected[]'])[%s]" % (i + 1)).click()

    def del_last(self):
        wd = self.gen.wd
        self.open_groups_page()
        # get group count
        self.select_last_group()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def del_not_choose(self):
        wd = self.gen.wd
        self.open_groups_page()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def create_empty(self):
        wd = self.gen.wd
        self.open_groups_page()
        # init new group creation
        wd.find_element_by_name("new").click()
        # submit group creation and return to group page
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def edit_all(self, group):
        wd = self.gen.wd
        self.open_groups_page()
        self.select_all_groups()
        wd.find_element_by_name("edit").click()
        # change group parameters
        self.enter_group_parameters(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def edit_all_wo_change(self):
        wd = self.gen.wd
        self.open_groups_page()
        self.select_all_groups()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def edit_last(self, group):
        wd = self.gen.wd
        self.open_groups_page()
        # select group & init editing
        self.select_last_group()
        wd.find_element_by_name("edit").click()
        # change group parameters
        self.enter_group_parameters(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def select_last_group(self):
        wd = self.gen.wd
        group_count = len(wd.find_elements_by_name("selected[]"))
        wd.find_element_by_xpath("(//input[@name='selected[]'])[%s]" % group_count).click()

    def update_last_wo_change(self):
        wd = self.gen.wd
        self.open_groups_page()
        # select group & init editing
        self.select_last_group()
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
