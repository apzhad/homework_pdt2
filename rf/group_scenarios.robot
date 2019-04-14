*** Settings ***
Library  rf.Addressbook
Suite Setup  Init fixture
Suite Teardown  Finish Fixture


*** Test Cases ***
Add new group
    Create Group  name1  header1  footer1