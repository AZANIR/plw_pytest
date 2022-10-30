from playwright.sync_api import Page


class RadioButtons:

    def __init__(self, page:Page):
        self.page = page
        self.__result = self.page.locator('[class="mt-3"]')

    def select_radio_button(self, name) -> None:
        radio_button = self.page.locator(f'input[id="{name.lower()}Radio"]')
        radio_button.click(force=True)

    def check_result(self, name) -> None:
        self.__result.wait_for(state='visible')
        assert self.__result.text_content() == f'You have selected {name}', \
            f'Expected text: "You have selected {name}", Actual text: {self.__result.text_content()}'
