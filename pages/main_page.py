from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    OFF_PLAN_LINK = (By.XPATH, '//a[@wized="newOffPlanLink"]')
    SALE_STATUS_FILTER = (By.XPATH, '//button[@data-test-id="filter-sale-status-dropdown"]')
    FILTER_OUT_OF_STOCK = (By.XPATH, '//div[@class="flex gap-1" and text()="Out of Stock"]')
    LISTINGS = (By.CSS_SELECTOR, 'a[data-test-id*="project-card"]')
    SALE_STATUS_TAG = (By.CSS_SELECTOR, 'span[data-test-id="project-card-sale-status"]')
    OUTSIDE = (By.TAG_NAME, 'body')

    def click_offplan_link(self):
        self.wait_until_clickable_then_click(*self.OFF_PLAN_LINK)
        self.wait_until_url_contains('find.reelly.io')

    def filter_by_outofstocks(self):
        self.wait_until_clickable_then_click(*self.SALE_STATUS_FILTER)
        self.wait_until_clickable_then_click(*self.FILTER_OUT_OF_STOCK)
        body_element = self.find_element(*self.OUTSIDE)  # the body of the elements
        body_element.click()  # click anywhere
        sleep(5)

    def verify_correct_tag(self, expected_tag):
        elements = self.find_elements(*self.LISTINGS)
        for e in elements:
            actual_tag = e.find_element(*self.SALE_STATUS_TAG).text
            assert expected_tag == actual_tag, f'Expected {expected_tag} but got {actual_tag}'
