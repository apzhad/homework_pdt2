*** Settings ***
Library  rf.Addressbook
Library  Collections
Suite Setup  Init fixture
Suite Teardown  Finish Fixture

*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  first_name1  last_name1  address1  12345
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${old_list}  ${new_list}
