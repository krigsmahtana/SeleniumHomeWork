from page_object.FindAndClick import FindAndClick


class AdminProduct(FindAndClick):

    def add_new_product(self, name, tagTitle, model):
        self._class_name("fa-plus")
        self._verify_id_presence("input-name1").send_keys(name)
        self._verify_id_presence("input-meta-title1").send_keys(tagTitle)
        self._xpath("//*[@id='form-product']/ul/li[2]/a")
        self._verify_id_presence("input-model").send_keys(model)
        self._class_name("fa-save")

    def find_product(self, name):
        self._verify_id_presence("input-name").send_keys(name)
        self._id("button-filter")
        text = self._verify_class_name_presence("text-center").text
        if text == "No results!":
            return "No results!"
        else:
            self._verify_xpath_presence("//*[@id='form-product']/div/table/tbody/tr[1]/td[3]")

    def delete_product(self, name):
        self.find_product(name)
        self._name("selected[]")
        self._class_name("fa-trash-o")
