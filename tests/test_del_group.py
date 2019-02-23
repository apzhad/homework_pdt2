from model.group import Group


def test_del_first_group(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_del"))
    gen.group.del_first()


def test_del_all_group(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_del_1"))
        gen.group.create(Group(name="for_del_2"))
        gen.group.create(Group(name="for_del_3"))
    gen.group.del_all()


def test_del_last_group(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_del_1"))
        gen.group.create(Group(name="for_del_2"))
        gen.group.create(Group(name="for_del_3"))
    gen.group.del_last()


def test_del_without_choice_group(gen):
    if gen.group.get_group_count() == 0:
        gen.group.create(Group(name="for_del_1"))
        gen.group.create(Group(name="for_del_2"))
    gen.group.del_not_choose()
