from model.group import Group
import random
import string
import os.path
import json


def random_string(prefix, max_length):
    symbols = string.ascii_letters + string.digits + ' '*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header_group", 20), footer=random_string("footer", 20))
    for i in range(5)
]


data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/group.json")

with open(data_file, "w") as data:
    data.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
