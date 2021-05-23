from page_object.FindAndClick import FindAndClick


class TopMenu(FindAndClick):

    def register(self):
        self._class_name("fa-user")
        self._xpath("//*[@id='top-links']/ul/li[2]/ul/li[1]/a")

    def login(self):
        self._xpath("//*[@id='top-links']/ul/li[2]/a/span[1]")
        self._xpath("//*[@id='top-links']/ul/li[2]/ul/li[2]/a")

    def change_currency(self, currensy):
        self._class_name("pull-left")
        self._name(currensy)

    def find_product(self, text):
        self._class_name("input-lg")
        self._verify_class_name_presence("input-lg").send_keys(text)
        self._class_name("input-group-btn")