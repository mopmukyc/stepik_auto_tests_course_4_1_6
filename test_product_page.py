import pytest
from .pages.product_page import ProductPage

params = list(map(str, range(10)))

@pytest.mark.parametrize('param', [
    x if x != '7' else pytest.param(x, marks=pytest.mark.xfail) for x in params
])
def test_guest_can_add_product_to_basket(browser, param):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{param}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    



# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"