from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


try:
    group = Group(id="300")
    l = db.get_contact_in_group(group)
    s = db.get_contact_in_group(group, sorted=True)
    for item in l:
        print(item)
    print(len(l))
    print(l)
    print(s)

finally:
    pass
