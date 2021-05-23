from page_object.FindAndClick import FindAndClick


class AdminLoginForm(FindAndClick):
    INPUT_EMAIL = "username"
    INPUT_PASSWORD = "password"
    LOGIN_BUTTON = "#content > div > div > div > div > div.panel-body > form > div.text-right >button"

    def userloginform(self, username, password):
        self._verify_name_presence(self.INPUT_EMAIL).send_keys(username)
        self._verify_name_presence(self.INPUT_PASSWORD).send_keys(password)
        self._css(self.LOGIN_BUTTON)