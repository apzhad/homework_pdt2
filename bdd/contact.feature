Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <first_name>, <last_name>, <address> and <home_phone>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | first_name  | last_name  | address  | home_phone |
  | first_name1 | last_name1 | address1 | 12345      |
  | first_name2 | last_name2 | address2 | 78960      |
