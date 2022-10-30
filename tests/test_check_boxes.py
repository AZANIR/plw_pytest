import pytest

from pages.check_boxes_page import CheckBox


class TestCheckBoxes:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.check_boxes = CheckBox(self.page)

        self.page.goto('https://demoqa.com/checkbox', wait_until='networkidle')

    def test_check_boxes(self, test_setup):
        """Test to verify check boxes functionality
        :param test_setup: setting up the browser and page object
        :return: None
        """

        self.check_boxes.expand_home_directory()

        self.check_boxes.select_chevron('Downloads')
        self.check_boxes.check_result('Downloads')

        self.check_boxes.select_chevron('Documents')
        self.check_boxes.check_result('Documents')

        self.check_boxes.select_chevron('Downloads')
        self.check_boxes.check_result('Downloads')

        self.check_boxes.select_chevron('Desktop')
        self.check_boxes.check_result('Desktop')