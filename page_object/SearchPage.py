from page_object.FindAndClick import FindAndClick


class SearchPage(FindAndClick):

    def click_in_find_product(self, text):
        self._xpath("//*[@id='content']/div[3]/div/div/div[2]/div[1]/h4/a")
        self._xpath("//*[@id='content']/div[3]/div/div/div[2]/div[1]/h4/a")