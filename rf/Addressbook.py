"""
Библиотека для Robot Framework 3.0
Запуск тестов осуществляется через python -m robot rf
"""

import pytest
from fixture.generic import Generic
from fixture.db import DbFixture
from fixture.orm import ORMFixture
import json
import os.path
from model.group import Group
import importlib
import jsonpickle


class Addressbook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="settings.json", browser="firefox"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.settings = json.load(f)

    def init_fixture(self):
        web_conf = self.settings['web']
        self.fixture = Generic(browser=self.browser, base_url=web_conf["base_url"])
        self.fixture.session.ensure_login(username=web_conf["username"], password=web_conf["password"])
        db_conf = self.settings["db"]
        self.dbfixture = DbFixture(host=db_conf["host"], name=db_conf["name"], user=db_conf["username"],
                                   password=db_conf["password"])

    def finish_fixture(self):
        self.fixture.finish()
        self.dbfixture.finish()

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def create_group(self, group):
        self.fixture.group.create(group)

    def delete_group(self, group):
        self.fixture.group.del_by_id(group.id)

    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

