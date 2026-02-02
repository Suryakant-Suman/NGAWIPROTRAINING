*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}      chrome


*** Keywords ***
open orangehrm
    open browser    ${url}     ${browser}
    maximize browser window
orangehrmlogin
    [Arguments]    ${username}  ${password}
    Input text    name=username    ${username}
    input text      name=password    ${password}
    sleep           5s
     capture page screenshot    beforelogin.png
    click button    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
     sleep          15s
    capture page screenshot    afterlogin.png
    close browser

*** Test Cases ***
Tc005_DD.robot
    open orangehrm
    Sleep       5s
    orangehrmlogin    Admin     admin123