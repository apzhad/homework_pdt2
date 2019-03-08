from random import randrange
import re


def test_info_on_homepage(gen):
    index = randrange(len(gen.contact.get_contact_list()))
    info_on_homepage = gen.contact.get_contact_list()[index]
    info_from_edit = gen.contact.get_info_from_edit(index)
    assert info_on_homepage.first_name == info_from_edit.first_name
    assert info_on_homepage.last_name == info_from_edit.last_name
    assert info_on_homepage.address == info_from_edit.address
    assert info_on_homepage.all_email == merge_email(info_from_edit)
    assert info_on_homepage.all_phones == merge_phone(info_from_edit)


"""
def test_info_in_details(gen):
    #index = randrange(len(gen.contact.get_contact_list()))
    for index in range(len(gen.contact.get_contact_list())):
        info_from_details = gen.contact.get_info_from_details(index)
        info_from_edit = gen.contact.get_info_from_edit(index)
    #assert info_from_details.first_name == info_from_edit.first_name
    #assert info_from_details.last_name == info_from_edit.last_name
    #assert info_from_details.address == info_from_edit.address
    #assert info_from_details.all_email == merge_email(info_from_edit)
        assert merge_phone(info_from_details) == merge_phone(info_from_edit)
"""

def clear_spec_symbol(s):
    return re.sub("[() -]", "", s)


def merge_phone(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_spec_symbol(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone,
                                        contact.work_phone, contact.secondary_home_phone]))))


def merge_email(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.primary_email, contact.secondary_email, contact.third_email])))
