
from playwright.sync_api import Page,expect

def test_cart(page:Page):
    # 登入
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    page.locator("#login-button").click()


    # 選取第一項商品名稱並加入購物車
    selected_first_item_name=page.locator(".inventory_item_name ").first.inner_text()
    print(selected_first_item_name)
    page.get_by_role("button", name="Add to cart").first.click()

    # 轉到商品頁
    page.locator(".shopping_cart_link").click()
    print(page.url)

    # 驗證商品數量為 1
    item_count=page.locator(".cart_item")
    expect(item_count).to_have_count(1)

    # 驗證商品名稱正確
    item_name= page.locator(".cart_item .inventory_item_name")
    expect(item_name).to_have_text(selected_first_item_name)