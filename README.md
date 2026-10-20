# QA測試

說明：本項目分別練習使用Playwright及Postman進行測試

## (一) SauceDemo 電商網站測試

### 1. 項目資訊
- 項目:SauceDemo 應用
- 網站連結：https://www.saucedemo.com/
- 測試類別：手動測試、UI自動化測試
- 自動化測試工具：Playwright
- 測試語言：Python

### 2. 測試範圍
1. 登入驗證
2. 商品排序
3. 購物車功能
4. 結帳流程


### 3.測試細節記錄
請參見：https://docs.google.com/spreadsheets/d/1MtfV4O93JI-kjjCgzD7vdd_Al4B6iBFXxwq_jMZkayo/edit?usp=sharing


## (二) DummyJSON API 測試

### 1. 項目資訊
- 項目:DummyJSON Products API 測試
- 網站連結：https://dummyjson.com/products
- 測試類別：API 功能測試
- 自動化測試工具：Postman
- 測試語言：Postman Script(JavaScript)

### 2. 測試範圍

1. 取得所有商品（包含以下驗證）
    1. 驗證回傳值Status Code =200
   2. 驗證Response有array
   3. 檢查第一筆資料是否含有必要欄位


2. 取得單一產品（包含以下驗證）
    1. 驗證回傳值Status Code =200
   2. 確認產品有id


3. 取得超出範圍商品ID（包含以下驗證）
   1. 驗證回傳值Status Code =404


4. 新增單一產品（包含以下驗證）
   1. 驗證回傳值Status Code =201
   2. 確認產品有id