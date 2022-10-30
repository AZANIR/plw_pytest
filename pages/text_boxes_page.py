from playwright.sync_api import Page, expect


class TextBoxes:

    def __init__(self, page: Page):
        self.page = page
        # form
        self.__full_name = self.page.locator('[id="userName"]')
        self.__email_input = self.page.locator('#userEmail')
        self.__current_address_input = self.page.locator('textarea#currentAddress')
        self.__permanent_address_input = self.page.locator('textarea#permanentAddress')
        self.__submit_btn = self.page.locator('#submit')
        # output form
        self.__output_form = self.page.locator('div[id="output"]')
        self.__name_field = self.page.locator('p[id="name"]')
        self.__email_field = self.page.locator('p[id="email"]')
        self.__current_address_field = self.page.locator('p[id="currentAddress"]')
        self.__permanent_address_field = self.page.locator('p[id="permanentAddress"]')

    def set_username(self, username) -> None:
        self.__full_name.fill(username)

    def set_email(self, email) -> None:
        self.__email_input.fill(email)

    def set_current_address(self, address) -> None:
        self.__current_address_input.fill(address)

    def set_permanent_address(self, address) -> None:
        self.__permanent_address_input.fill(address)

    def submit_form(self) -> None:
        self.__submit_btn.click()
        self.__output_form.wait_for(state='visible')

    def check_output_form(self, username, email, current_address, permanent_address) -> None:
        assert self.__name_field.text_content() == f'Name:{username}', \
            f'Expected text: "{username}", Actual text: {self.__name_field.text_content()}'
        assert self.__email_field.text_content() == f'Email:{email}', \
            f'Expected text: "{email}", Actual text: {self.__email_field.text_content()}'
        print(current_address)
        expect(self.__current_address_field).to_have_text(f'Current Address :{current_address}')
        expect(self.__permanent_address_field).to_have_text(f'Permananet Address :{permanent_address}')
