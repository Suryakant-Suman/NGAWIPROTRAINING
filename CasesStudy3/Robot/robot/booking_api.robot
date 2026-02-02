*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Book Movie Tickets
    Create Session    api    ${BASE_URL}

    # Ensure movie exists
    ${movie}=    Create Dictionary
    ...    id=101
    ...    movie_name=Interstellar
    ...    language=English
    ...    duration=2h 49m
    ...    price=250

    POST On Session    api    /api/movies    json=${movie}

    # Now book ticket
    ${booking}=    Create Dictionary
    ...    movie_id=101
    ...    seats=3

    ${response}=    POST On Session    api    /api/bookings    json=${booking}
    Status Should Be    201    ${response}
