import pytest
import allure
from pages.buttons_page import Buttons
from pytest import mark
from utils.tools import take_screenshot


class TestButtons:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.buttons = Buttons(self.page)

        self.page.goto('https://demoqa.com/buttons')

    @mark.one
    def test_double_click_button(self, test_setup):
        """Test to verify double click button functionality
        :param test_setup: setting up the browser and page object
        :return: None
        """
        self.buttons.perform_double_click()
        self.buttons.check_double_click_result()
        take_screenshot(self.page, "double_click")

    @mark.two
    def test_rmb_click_button(self, test_setup):
        """Test to Verify rmb click button functionality
        :param test_setup: setting up the browser and page object
        :return: None
        """

        self.buttons.perform_right_click()
        self.buttons.check_right_click_result()

    def test_dynamic_button(self, test_setup):
        """Test to Verify dynamic click button functionality
        :param test_setup: setting up the browser and page object
        :return: None
        """

        self.buttons.click_the_button()
        self.buttons.check_click_result()
