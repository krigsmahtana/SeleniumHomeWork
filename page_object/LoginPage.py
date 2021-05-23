from page_object.FindAndClick import FindAndClick


class LoginPage(FindAndClick):
    INPUT_EMAIL = "email"
    INPUT_PASSWORD = "password"
    LOGIN_BUTTON = "//*[@id='content']/div/div[2]/div/form/input"

    def _login(self, email, password):
        self._name(self.INPUT_EMAIL)
        self._verify_name_presence(self.INPUT_EMAIL).send_keys(email)
        self._name(self.INPUT_PASSWORD)
        self._verify_name_presence(self.INPUT_PASSWORD).send_keys(password)
        self._xpath(self.LOGIN_BUTTON)