import pytest

from pages.select_menu_page import SelectMenu
from data.test_data import Data


class TestSelect:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.select_menu = SelectMenu(self.page)

        self.page.goto('https://demoqa.com/select-menu', wait_until='networkidle')

    def test_select_menu(self, test_setup):
        """Test to verify select menu functionality
        :param test_setup: setting up the browser and page object
        :return: None
        """

        self.select_menu.select_group_1_option_1()
        self.select_menu.select_professor()
        self.select_menu.select_color_old()
        self.select_menu.select_multiple_cars()
        self.select_menu.select_multiple_colors(Data.colors)
