
def test_del_first_group(gen):
    gen.group.del_first()


def test_del_all_group(gen):
    gen.group.del_all()


def test_del_last_group(gen):
    gen.group.del_last()


def test_del_without_choice_group(gen):
    gen.group.del_not_choose()
