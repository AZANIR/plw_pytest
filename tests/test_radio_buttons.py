import pytest

from pages.radio_buttons_page import RadioButtons


class TestRadioButtons:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.radio_buttons = RadioButtons(self.page)

        self.page.goto('https://demoqa.com/radio-button')

    def test_radio_buttons(self, test_setup):
        """Test to verify radio buttons functionality
        :param test_setup: setting up the browser and page object
        :return: None
        """

        self.radio_buttons.select_radio_button('Yes')
        self.radio_buttons.check_result('Yes')

        self.radio_buttons.select_radio_button('Impressive')
        self.radio_buttons.check_result('Impressive')
