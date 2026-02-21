*** Settings ***
Library    DataDriver    file=${CURDIR}/../../TestData/e2e_master_data.csv
Resource   ../keywords/account_keywords.robot
Resource   ../keywords/common_keywords.robot

Test Setup     Open Application
Test Teardown  Close Application
Suite Teardown    Finalize Suite Screenshot Policy
Test Template  Scenario 1 Registration And Login

*** Test Cases ***
Registration Login Scenario
    [Tags]    modular    scenario1

*** Keywords ***
Scenario 1 Registration And Login
    [Arguments]    ${firstname}    ${lastname}    ${phone}    ${password}
    Login User With Shared Registration    ${firstname}    ${lastname}    ${phone}    ${password}
    Logout User
    Verify Logout Successful
    Login User With Shared Registration    ${firstname}    ${lastname}    ${phone}    ${password}
