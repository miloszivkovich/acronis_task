from pytest_bdd import scenario, given, when, then, parsers
from pages.kiwi_homepage import KiwiHomepage
from playwright.sync_api import expect

# 1. Scenario Definition
# Links the feature file to the Python test file.
@scenario('../feature/search.feature', 'T1 - flight search one way')
def test_one_way_flight_search():
    pass

# 2. Given Steps
@given('As an not logged user navigate to homepage https://www.kiwi.com/en/')
def navigate_to_homepage(kiwi_homepage: KiwiHomepage):
    kiwi_homepage.navigate()
    kiwi_homepage.accept_cookies() # Handle the mandatory cookie banner

# 3. When Steps
@when('I select one-way trip type')
def select_one_way_trip(kiwi_homepage: KiwiHomepage):
    kiwi_homepage.select_one_way()

@when(parsers.parse('Set as departure airport {airport_code_from}'))
def set_departure_airport(kiwi_homepage: KiwiHomepage, airport_code_from: str):
    kiwi_homepage.set_airport_from(airport_code_from)

@when(parsers.parse('Set the arrival airport {airport_code_to}'))
def set_arrival_airport(kiwi_homepage: KiwiHomepage, airport_code_to: str):
    kiwi_homepage.set_airport_to(airport_code_to)

@when(parsers.parse('Set the departure time {days_in_future} in the future starting current date'))
def set_departure_time_one_week(kiwi_homepage: KiwiHomepage, days_in_future: str):
    days_in_future_int = int(days_in_future)
    kiwi_homepage.set_departure_date(days_in_future_int)

@when(parsers.parse("Set {value} to the 'Check accommodation with booking.com' option"))
def uncheck_accommodation(kiwi_homepage: KiwiHomepage, value: str):
    kiwi_homepage.uncheck_accommodation(value)

@when('Click the search button')
def click_search(kiwi_homepage: KiwiHomepage):
    kiwi_homepage.click_search()

@then(parsers.parse('I am redirected to search results page for {days_in_future} in future'))
def verify_redirection(kiwi_homepage: KiwiHomepage, days_in_future: str):
    days_in_future_int = int(days_in_future)
    kiwi_homepage.verify_redirect_to_search(days_in_future_int)