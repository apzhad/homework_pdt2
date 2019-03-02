from model.group import Group


def test_del_first_group(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_del"))
    old_group_list = gen.group.get_group_list()
    gen.group.del_first()
    assert len(old_group_list) - 1 == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list[0:1] = []
    assert old_group_list == new_group_list


def test_del_all_group(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_del_1"))
        gen.group.create(Group(name="for_del_2"))
        gen.group.create(Group(name="for_del_3"))
    gen.group.del_all()
    assert 0 == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    assert [] == new_group_list


def test_del_last_group(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_del_1"))
        gen.group.create(Group(name="for_del_2"))
        gen.group.create(Group(name="for_del_3"))
    old_group_list = gen.group.get_group_list()
    gen.group.del_last()
    assert len(old_group_list) - 1 == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    old_group_list[-1:] = []
    assert old_group_list == new_group_list


def test_del_without_choice_group(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_del_1"))
        gen.group.create(Group(name="for_del_2"))
    old_group_list = gen.group.get_group_list()
    gen.group.del_not_choose()
    assert len(old_group_list) == gen.group.get_group_count()
    new_group_list = gen.group.get_group_list()
    assert old_group_list == new_group_list
