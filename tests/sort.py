import time

from playwright.sync_api import Page,expect

def test_sort(page:Page):
    # 登入
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    page.locator("#login-button").click()

    # 點擊排序 價格由低到高
    page.get_by_label("Sort products").select_option('Price (low to high)')

    time.sleep(1)

    # 統計所有價格
    price_list=[
        float(i.inner_text().replace("$", ""))
        for i in page.locator(".inventory_item_price").all()
    ]

    # 比較價格是否由小至大
    assert price_list==sorted(price_list)

