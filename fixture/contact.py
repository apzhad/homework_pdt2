# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
import os


class ContactManage:

    def __init__(self, gen):
        self.gen = gen

    def open_home_page(self):
        wd = self.gen.wd
        wd.find_element_by_link_text("home").click()

    def select_all_contact(self):
        wd = self.gen.wd
        # get contact count
        contact_count = self.get_contact_count()
        for i in range(contact_count):
            wd.find_element_by_xpath("(//input[@name='selected[]'])[%s]" % (i + 1)).click()

    def get_contact_count(self, group_name=None):
        wd = self.gen.wd
        self.open_home_page()
        if group_name is not None:
            self.select_from_list("group", group_name)
        return len(wd.find_elements_by_name("selected[]"))

    def enter_contact_parameters(self, contact):
        wd = self.gen.wd
        # contact name
        self.set_field_value("firstname", contact.first_name)
        self.set_field_value("middlename", contact.middle_name)
        self.set_field_value("lastname", contact.last_name)
        self.set_field_value("nickname", contact.nickname)

        # add photo
        if contact.photo_path:
            photo = wd.find_element_by_name("photo")
            photo.send_keys(os.path.split(os.environ['VIRTUAL_ENV'])[0] + contact.photo_path)

        if contact.del_foto:
            wd.find_element_by_name("delete_photo").click()

        """
        # code from recoder
        wd.find_element_by_name("photo").click()
        wd.find_element_by_name("photo").clear()
        wd.find_element_by_name("photo").send_keys(os.getcwd() + "\\test_data\\cat.jpg")
        """

        # common info (company, address,title, etc.)
        self.set_field_value("title", contact.title)
        self.set_field_value("company", contact.company)
        self.set_field_value("address", contact.address)
        # phone info
        self.set_field_value("home", contact.home_phone)
        self.set_field_value("mobile", contact.mobile_phone)
        self.set_field_value("work", contact.work_phone)
        self.set_field_value("fax", contact.fax)

        # email info
        self.set_field_value("email", contact.primary_email)
        self.set_field_value("email2", contact.secondary_email)
        self.set_field_value("email3", contact.third_email)
        self.set_field_value("homepage", contact.homepage)

        # birthday info
        self.select_from_list("bday", contact.birth_day)
        self.select_from_list("bmonth", contact.birth_month)
        self.set_field_value("byear", contact.birth_year)

        # anniversary info
        self.select_from_list("aday", contact.anniversary_day)
        self.select_from_list("amonth", contact.anniversary_month)
        self.set_field_value("ayear", contact.anniversary_year)

        # select group
        if contact.group_name:
            self.select_from_list("new_group", contact.group_name)

        # secondary info
        self.set_field_value("address2", contact.secondary_address)
        self.set_field_value("phone2", contact.secondary_home_phone)
        self.set_field_value("notes", contact.notes)

    def select_from_list(self, list_name, text):
        wd = self.gen.wd
        if text is not None:
            wd.find_element_by_name(list_name).click()
            Select(wd.find_element_by_name(list_name)).select_by_visible_text(text)

    def set_field_value(self, field_name, text):
        wd = self.gen.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact):
        wd = self.gen.wd
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        # enter contact parameters
        self.enter_contact_parameters(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_homepage()

    def return_to_homepage(self):
        wd = self.gen.wd
        wd.find_element_by_link_text("home page").click()

    def select_first_contact(self):
        wd = self.gen.wd
        wd.find_element_by_name("selected[]").click()

    def create_empty(self):
        wd = self.gen.wd
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_homepage()

    def del_first(self):
        wd = self.gen.wd
        self.open_home_page()
        # select first contact & submit deletion
        self.select_first_contact()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()

    def cancel_del_first(self):
        wd = self.gen.wd
        self.open_home_page()
        # select contact & submit deletion
        self.select_first_contact()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().dismiss()

    def del_by_select_all(self):
        wd = self.gen.wd
        self.open_home_page()
        # click "select all" & submit deletion
        wd.find_element_by_xpath("(//input[@id='MassCB'])").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()

    def del_all_by_click(self):
        wd = self.gen.wd
        self.open_home_page()
        self.select_all_contact()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()

    def del_unselected(self):
        wd = self.gen.wd
        self.open_home_page()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()

    def del_all_from_group(self, group_name):
        wd = self.gen.wd
        self.open_home_page()
        self.select_from_list("group", group_name)
        # click "select all" & submit deletion
        wd.find_element_by_xpath("(//input[@id='MassCB'])").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()

    def del_first_from_group(self, group_name):
        wd = self.gen.wd
        self.open_home_page()
        self.select_from_list("group", group_name)
        # click "select all" & submit deletion
        self.select_first_contact()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()

    def edit_first(self, contact):
        wd = self.gen.wd
        self.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.enter_contact_parameters(contact)
        wd.find_element_by_name("update").click()
        self.return_to_homepage()

    def del_first_using_edit(self):
        wd = self.gen.wd
        self.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def edit_first_wo_change(self):
        wd = self.gen.wd
        self.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_name("update").click()
        self.return_to_homepage()

    def edit_first_from_details(self, contact):
        wd = self.gen.wd
        self.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        wd.find_element_by_name("modifiy").click()
        self.enter_contact_parameters(contact)
        wd.find_element_by_name("update").click()
        self.return_to_homepage()

    def edit_first_in_group(self, group_name, contact):
        wd = self.gen.wd
        self.open_home_page()
        self.select_from_list("group", group_name)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.enter_contact_parameters(contact)
        wd.find_element_by_name("update").click()
        self.return_to_homepage()

    def add_to_group(self, group_name):
        wd = self.gen.wd
        self.open_home_page()
        wd.find_element_by_xpath("(//input[@id='MassCB'])").click()
        self.select_from_list("to_group", group_name)
        wd.find_element_by_name("add").click()
        wd.find_element_by_link_text("group page \"%s\"" % group_name).click()

    def add_to_group_unselected(self, group_name):
        wd = self.gen.wd
        self.open_home_page()
        self.select_from_list("to_group", group_name)
        wd.find_element_by_name("add").click()

    def add_to_group_from_another(self, group_from, group_to):
        wd = self.gen.wd
        self.open_home_page()
        self.select_from_list("group", group_from)
        wd.find_element_by_xpath("(//input[@id='MassCB'])").click()
        self.select_from_list("to_group", group_to)
        wd.find_element_by_name("add").click()
        wd.find_element_by_link_text("group page \"%s\"" % group_to).click()

    def remove_from_group(self, group_name):
        wd = self.gen.wd
        self.open_home_page()
        self.select_from_list("group", group_name)
        wd.find_element_by_xpath("(//input[@id='MassCB'])").click()
        wd.find_element_by_name("remove").click()
        wd.find_element_by_link_text("group page \"%s\"" % group_name).click()

    def del_all_found(self, search):
        wd = self.gen.wd
        self.open_home_page()
        self.select_from_list("group", "[all]")
        # find text
        self.set_field_value("searchstring", search)
        # click "select all" & submit deletion
        wd.find_element_by_xpath("(//input[@id='MassCB'])").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()

    def edit_first_found(self, search, contact):
        wd = self.gen.wd
        # find text & edit contact
        self.set_field_value("searchstring", search)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.enter_contact_parameters(contact)
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
