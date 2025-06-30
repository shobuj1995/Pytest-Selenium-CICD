import pytest
from project2_automation.Pages.LoginPage import LoginPage

@pytest.mark.functionaltest
def test_login_valid(browserInstance, login_data_row):
    driver = browserInstance
    driver.get(login_data_row["url"])

    login_page = LoginPage(driver)
    print(login_page.getTitle())

    home_page = login_page.login(
        login_data_row["userEmail"],
        login_data_row["userPassword"]
    )

    assert home_page.is_home_displayed()

    shop_page = home_page.navigate_to_shoppage()
    shop_page.add_product_to_cart(login_data_row["productName"])
    print(shop_page.getTitle())

    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("Ban")
    checkout_confirmation.validate_order()




# # Load data from JSON
# data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'testdata.json')
#
# with open(data_path) as f:
#     json_data = json.load(f)
#     login_data_list = json_data["data"]
#
# @pytest.mark.functionaltest
# @pytest.mark.parametrize("test_input", login_data_list)
# def test_login_valid(browserInstance, test_input):
#     driver = browserInstance
#     driver.get(test_input["url"])  # Load URL from JSON
#     login_page = LoginPage(driver)
#     print(login_page.getTitle())
#
#     # Perform login with test data from JSON
#     home_page = login_page.login(
#         test_input["userEmail"],
#         test_input["userPassword"]
#     )
#
#     # Verify landing page (assuming such method exists in home_page)
#     assert home_page.is_home_displayed()
#     shop_page=home_page.navigate_to_shoppage()
#     shop_page.add_product_to_cart(test_input["productName"])
#     print(shop_page.getTitle())
#     checkout_confirmation = shop_page.goToCart()
#     checkout_confirmation.checkout()
#     checkout_confirmation.enter_delivery_address("Ban")
#     checkout_confirmation.validate_order()
