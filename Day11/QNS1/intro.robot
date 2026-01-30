*** Settings ***
Library    BuiltIn

*** Variables ***
${GREETING}    Hello, Robot Framework!
@{ITEMS}       One    Two    Three

*** Test Cases ***
First Test Case
    Log    ${GREETING}
    Log To Console    ${GREETING}

Second Test Case
    Log    The items are: ${ITEMS}
    Log To Console    First item is: ${ITEMS}[0]