from model.group import Group
from model.contact import Contact


def test_group_list(gen, db):
    web_group = gen.group.get_group_list()
    db_group = db.get_group_list()
    assert sorted(web_group, key=Group.id_or_max) == sorted(db_group, key=Group.id_or_max)


def test_contact_list(gen, db):
    web_contact = gen.contact.get_contact_list()
    db_contact = db.get_contact_list()
    assert sorted(web_contact, key=Contact.id_or_max) == sorted(db_contact, key=Contact.id_or_max)
