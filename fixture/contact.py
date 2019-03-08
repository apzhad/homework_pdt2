# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
import os
from model.contact import Contact


class ContactManage:

    def __init__(self, gen):
        self.gen = gen

    def open_home_page(self):
        wd = self.gen.wd
        if "addressbook/?group=" in wd.current_url:
            self.select_from_list("group", "[all]")
        elif not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name('searchstring')) > 0):
            wd.find_element_by_link_text("home").click()

    def select_all_contact(self):
        wd = self.gen.wd
        # get contact count
        contact_count = self.get_contact_count()
        for i in range(contact_count):
            wd.find_element_by_xpath("(//input[@name='selected[]'])[%s]" % (i + 1)).click()

    def get_contact_count(self, group_name=None):
        wd = self.gen.wd
        # wd.find_element_by_link_text("home").click()
        if group_name is not None:
            self.open_contact_group(group_name)
            #self.select_from_list("group", group_name)
        else:
            self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_result_count(self, search, group_name=None):
        wd = self.gen.wd
        self.open_home_page()
        if group_name is not None:  # if search in defined group
            self.select_from_list("group", group_name)
        self.set_field_value("searchstring", search)
        return int(wd.find_element_by_id("search_count").text)

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
        self.init_create_contact()
        # enter contact parameters
        self.enter_contact_parameters(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_homepage()
        self.contact_cache = None

    def init_create_contact(self):
        wd = self.gen.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def return_to_homepage(self):
        wd = self.gen.wd
        wd.find_element_by_link_text("home page").click()

    def select_first_contact(self):
        wd = self.gen.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.gen.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def create_empty(self):
        wd = self.gen.wd
        # init new contact creation
        self.init_create_contact()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_homepage()
        self.contact_cache = None

    def del_first(self):
        self.del_by_index(0)

    def del_by_index(self, index):
        wd = self.gen.wd
        self.open_home_page()
        # select first contact & submit deletion
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def cancel_del_first(self):
        self.cancel_del_by_index(0)

    def cancel_del_by_index(self, index):
        wd = self.gen.wd
        self.open_home_page()
        # select contact & submit deletion
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().dismiss()
        self.contact_cache = None

    def del_by_select_all(self):
        wd = self.gen.wd
        self.open_home_page()
        # click "select all" & submit deletion
        wd.find_element_by_xpath("(//input[@id='MassCB'])").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def del_all_by_click(self):
        wd = self.gen.wd
        self.open_home_page()
        self.select_all_contact()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def del_unselected(self):
        wd = self.gen.wd
        self.open_home_page()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def del_all_from_group(self, group_name):
        wd = self.gen.wd
        self.open_contact_group(group_name)
        # click "select all" & submit deletion
        wd.find_element_by_xpath("(//input[@id='MassCB'])").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def open_contact_group(self, group_name):
        wd = self.gen.wd
        if len(wd.find_elements_by_xpath("(//input[@id='MassCB'])")) > 0 and len(wd.find_elements_by_name('searchstring')) > 0:
            if not (wd.current_url.endswith("addressbook/?group=" + self.get_group_id(group_name))):
                self.select_from_list("group", group_name)
        else:
            wd.find_element_by_link_text("home").click()
            self.select_from_list("group", group_name)

    def get_group_id(self, group):
        wd = self.gen.wd
        # todo: get id from fixture group. Maybe should use wd.back?
        if wd.find_element_by_xpath('//select[@name="group"]'):
            select = Select(wd.find_element_by_xpath('//select[@name="group"]'))
            for option in select.options:
                if option.text == group:
                    return str(option.get_attribute('value'))

    def del_first_from_group(self, group_name):
        self.del_from_group_by_index(0, group_name)

    def del_from_group_by_index(self, index, group_name):
        wd = self.gen.wd
        self.open_contact_group(group_name)
        # click "select all" & submit deletion
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def del_first_using_edit(self):
        self.del_using_edit_by_index(0)

    def del_using_edit_by_index(self, index):
        wd = self.gen.wd
        self.open_edit(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def open_edit(self, index):
        wd = self.gen.wd
        self.open_home_page()
        self.click_pencil_img(index)

    def edit_first(self, contact):
        self.edit_by_index(0, contact)

    def edit_by_index(self, index, contact):
        wd = self.gen.wd
        self.open_edit(index)
        self.enter_contact_parameters(contact)
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    def edit_first_wo_change(self):
        self.edit_wo_change_by_index(0)

    def edit_wo_change_by_index(self, index):
        wd = self.gen.wd
        self.open_edit(index)
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    def edit_first_from_details(self, contact):
        self.edit_from_details_by_index(0, contact)

    def edit_from_details_by_index(self, index, contact):
        wd = self.gen.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()
        wd.find_element_by_name("modifiy").click()
        self.enter_contact_parameters(contact)
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    def edit_first_in_group(self, group_name, contact):
        self.edit_in_group_by_index(0, group_name, contact)

    def edit_in_group_by_index(self, index, group_name, contact):
        wd = self.gen.wd
        self.open_contact_group(group_name)
        self.click_pencil_img(index)
        self.enter_contact_parameters(contact)
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    def add_all_to_group(self, group_name):
        wd = self.gen.wd
        self.open_home_page()
        wd.find_element_by_xpath("(//input[@id='MassCB'])").click()
        self.select_from_list("to_group", group_name)
        wd.find_element_by_name("add").click()
        wd.find_element_by_link_text('group page "%s"' % group_name).click()
        self.contact_cache = None

    def add_to_group_unselected(self, group_name):
        wd = self.gen.wd
        self.open_home_page()
        self.select_from_list("to_group", group_name)
        wd.find_element_by_name("add").click()
        self.contact_cache = None

    def add_to_group_from_another(self, group_from, group_to):
        wd = self.gen.wd
        self.open_contact_group(group_from)
        wd.find_element_by_xpath("(//input[@id='MassCB'])").click()
        self.select_from_list("to_group", group_to)
        wd.find_element_by_name("add").click()
        wd.find_element_by_link_text('group page "%s"' % group_to).click()
        self.contact_cache = None

    def remove_from_group(self, group_name):
        wd = self.gen.wd
        self.open_contact_group(group_name)
        wd.find_element_by_xpath("(//input[@id='MassCB'])").click()
        wd.find_element_by_name("remove").click()
        wd.find_element_by_link_text('group page "%s"' % group_name).click()
        self.contact_cache = None

    def del_all_found(self, search):
        wd = self.gen.wd
        self.open_home_page()
        # find text
        self.set_field_value("searchstring", search)
        # click "select all" & submit deletion
        wd.find_element_by_xpath("(//input[@id='MassCB'])").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def edit_first_found(self, search, contact):
        wd = self.gen.wd
        # find text & edit contact
        self.open_home_page()
        self.set_field_value("searchstring", search)
        self.click_first_pencil_img()
        self.enter_contact_parameters(contact)
        wd.find_element_by_name("update").click()
        self.return_to_homepage()
        self.contact_cache = None

    def click_first_pencil_img(self, group=None):
        wd = self.gen.wd
        for i in range(self.get_contact_count(group)):
            if wd.find_element_by_xpath("(//img[@alt='Edit'])[%s]" % (i+1)):
                wd.find_element_by_xpath("(//img[@alt='Edit'])[%s]" % (i+1)).click()
                return

    def click_pencil_img(self, index):
        wd = self.gen.wd
        wd.find_elements_by_xpath("(//img[@alt='Edit'])")[index].click()

    contact_cache = None

    def get_contact_list(self, group_name=None, search=None):
        if self.contact_cache is None:
            wd = self.gen.wd
            if group_name is not None:
                self.open_contact_group(group_name)
            else:
                self.open_home_page()
            if search is not None:
                self.set_field_value("searchstring", search)
            self.contact_cache = []
            for i in wd.find_elements_by_name("entry"):
                id = i.find_element_by_name("selected[]").get_attribute('value')
                cells = i.find_elements_by_tag_name("td")
                self.contact_cache.append(Contact(id=id, last_name=cells[1].text, first_name=cells[2].text))
        return self.contact_cache
