from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <first_name>, <last_name>, <address> and <home_phone>')
def new_contact(first_name, last_name, address, home_phone):
    return Contact(first_name=first_name, last_name=last_name, address=address, home_phone=home_phone)


@when('I add the contact to the list')
def add_contact(gen, new_contact):
    gen.contact.create(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(contact_list, db, new_contact, check_ui, gen):
    old_contact_list = contact_list
    new_contact_list = db.get_contact_list()
    assert len(old_contact_list) + 1 == len(db.get_contact_list())
    old_contact_list.append(new_contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(gen.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)
