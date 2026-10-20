from playwright.sync_api import Page,expect

def test_checkout(page:Page):

    # 登入
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    page.locator("#login-button").click()


    # 選擇加入商品
    page.get_by_role("button",name="Add to cart").first.click()

    # 轉到商品頁
    page.locator(".shopping_cart_link").click()

    # 點選結帳
    page.get_by_role("button",name="Checkout").click()

    # First Name 留空，其他填入資訊
    page.get_by_label("First Name").fill("")
    page.get_by_label("Last Name").fill("User")
    page.get_by_label("Zip/Postal Code").fill("123")
    page.get_by_role("button",name="Continue").click()

    #預期出現欄位顯示必填
    error_message = page.locator('[data-test="error"]')
    expect(error_message).to_have_text("Error: First Name is required")