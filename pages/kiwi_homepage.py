from datetime import date, timedelta
from playwright.sync_api import Page, expect


class KiwiHomepage:

    URL = "https://www.kiwi.com/en/"

    def __init__(self, page: Page):
        self.page = page
        
        self.accept_cookies_btn = page.locator('//button[@data-test="CookiesPopup-Accept"]') 
        self.ticket_type_dropdown = page.locator('//div[@data-test="SearchFormModesPicker-active-return"]')
        self.one_way_radio = page.locator('[data-test="ModePopupOption-oneWay"]')
        self.departure_input = page.locator('[data-test="PlacePickerInput-origin"] input')
        self.arrival_input = page.locator('[data-test="PlacePickerInput-destination"] input')
        self.first_airport_suggestion = page.locator('[data-test="PlacePickerRow-wrapper"]')
        self.close_previous_airport_suggestions = page.locator('[data-test="PlacePickerInputPlace-close"]') 
        self.departure_date_input = page.locator('[data-test="SearchDateInput"]')
        self.departure_date_tile = lambda d: self.page.locator(
            f'[data-value="{d.year}-{d.month:02d}-{d.day:02d}"][data-test="CalendarDay"] [data-test="DayContentContainer"]')
        self.deperture_date_done_button = page.locator('//button[@data-test="SearchFormDoneButton"]')
        self.accommodation_checkbox = page.locator('[data-test="accommodationCheckbox"]')
        self.search_button = page.locator('[data-test="LandingSearchButton"]')
        #self.search_page = page.locator('[data-test="SearchFormFilters"]')

    def navigate(self):
        self.page.goto(self.URL)
        
    def accept_cookies(self):
        self.accept_cookies_btn.click(timeout=5000)

    def select_one_way(self):
        self.ticket_type_dropdown.click(timeout=5000)
        self.one_way_radio.click(timeout=5000)
        
    def set_airport_from(self, airport_code: str):
        self.close_previous_airport_suggestions.click(timeout=5000)
        self.page.wait_for_timeout(1000)
        self.departure_input.fill(airport_code)
        self.page.wait_for_timeout(1000)
        self.first_airport_suggestion.first.click()
    
    def set_airport_to(self, airport_code: str):
        self.page.wait_for_timeout(1000)
        self.arrival_input.fill(airport_code)
        self.page.wait_for_timeout(1000)
        self.first_airport_suggestion.first.click()

    def set_departure_date(self, days_in_future: int):
        target_date = date.today() + timedelta(days=days_in_future)
        self.departure_date_input.click(timeout=5000)
        date_tile_locator = self.departure_date_tile(target_date)
        date_tile_locator.click(timeout=5000)
        self.deperture_date_done_button.click(timeout=5000)


    def uncheck_accommodation(self, uncheck: bool ):
        if uncheck == "true":
            self.accommodation_checkbox.click(timeout=5000)
        
    def click_search(self):
        self.search_button.click(timeout=5000)
        
    def verify_redirect_to_search(self, days_in_future: int):
        self.page.wait_for_url("**/search/results/**", timeout=10000)
        current_url = self.page.url
        assert "/search/results/" in current_url, f"Expected results page, got {current_url}"
        target_date = date.today() + timedelta(days=days_in_future)
        assert target_date.strftime("%Y-%m-%d") in current_url, f"Departure date {target_date} not in URL {current_url}"
        assert "no-return" in current_url, f"One-way trip not indicated in URL {current_url}"