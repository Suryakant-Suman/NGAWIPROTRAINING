*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Get All Movies
    Create Session    movieapi    ${BASE_URL}
    ${response}=    GET On Session    movieapi    /api/movies
    Status Should Be    200    ${response}
    Log    ${response.json()}

Add New Movie
    Create Session    movieapi    ${BASE_URL}
    ${movie}=    Create Dictionary
    ...    id=201
    ...    movie_name=Tenet
    ...    language=English
    ...    duration=2h 30m
    ...    price=300

    ${response}=    POST On Session    movieapi    /api/movies    json=${movie}
    Status Should Be    201    ${response}
    Dictionary Should Contain Key    ${response.json()}    movie_name
