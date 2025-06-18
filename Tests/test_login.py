from Pages.LoginPage import LoginPage

def test_login_valid(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    assert login_page.is_dashboard_displayed()
