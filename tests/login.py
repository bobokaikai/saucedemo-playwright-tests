import random
from playwright.sync_api import Page,expect


def test_login(page:Page):

    # 登入
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    page.locator("#login-button").click()

    # 驗證是否登入成功
    expect(page.locator("#logout_sidebar_link")).to_be_visible()