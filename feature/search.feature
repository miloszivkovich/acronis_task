Scenario Outline: T1 - flight search one way
    Given As an not logged user navigate to homepage https://www.kiwi.com/en/
    When I select one-way trip type
    And Set as departure airport <Departure>
    And Set the arrival airport <Arrival>
    And Set the departure time <Days> in the future starting current date
    And Set <Check> to the 'Check accommodation with booking.com' option
    And Click the search button
    Then I am redirected to search results page for <Days> in future

    Examples:
        | TestId | Departure    | Arrival    | Days | Check |
        | T1.1   | rotterdam rt | madrid mad | 7    | true  |
        | T1.2   | beograd      | madrid mad | 5    | true  |
