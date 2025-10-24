Feature: Test Scenarios for Filters functionality

  Scenario: User can filter by sale status Out of Stocks
    Given Open signin page
    When User log in
    And Click on off plan in left side menu
    And Filter by sales status of Out of Stocks
    Then Verify each product contains the out of stock tag
