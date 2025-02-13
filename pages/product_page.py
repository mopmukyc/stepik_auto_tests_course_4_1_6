from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def should_be_product_page(self):

        # newYear
        self.should_be_new_year_url()

        # Add to basket
        self.add_product_to_basket()

        # Quiz
        self.solve_quiz_and_get_code()

        time.sleep(3)

        # Product name
        self.check_added_product_name()

        # Product price
        self.check_added_product_price()

        time.sleep(5)


    def should_be_new_year_url(self):
        assert '?promo=offer' in self.browser.current_url, 'Not found word "?promo=offer"in URL'
        
    
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        link.click()


    def check_added_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME)
        assert product_name.text == alert_product_name.text, 'Product name not right'


    def check_added_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        alert_product_price = self.browser.find_element(*ProductPageLocators.ALERT_BASKET_SUMM)
        assert product_price.text == alert_product_price.text, 'Product price not right'





# #messsages .alert:first-child .alertinner 