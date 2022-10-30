import pytest
from pages.text_boxes_page import TextBoxes
from data.test_data import Data


class TestTextBoxes:

        @pytest.fixture
        def test_setup(self, page):
            self.page = page
            self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
            self.text_boxes = TextBoxes(self.page)

            self.page.goto('https://demoqa.com/text-box', wait_until='networkidle')

        def test_text_boxes(self, test_setup):
            """Test to verify text boxes functionality
            :param test_setup: setting up the browser and page object
            :return: None
            """

            self.text_boxes.set_username(Data.username)
            self.text_boxes.set_email(Data.email)
            self.text_boxes.set_current_address(Data.current_address)
            self.text_boxes.set_permanent_address(Data.permanent_address)
            self.text_boxes.submit_form()

            # check results
            self.text_boxes.check_output_form(Data.username, Data.email, Data.current_address, Data.permanent_address)
