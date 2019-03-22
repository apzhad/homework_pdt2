from model.group import Group


def test_group_list(gen, db):
    web_group = gen.group.get_group_list()
    db_group = db.get_group_list()
    assert sorted(web_group, key=Group.id_or_max) == sorted(db_group, key=Group.id_or_max)
