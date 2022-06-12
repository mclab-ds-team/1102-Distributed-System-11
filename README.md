# 分散式系統 第十一組 Kafka實作-食物訂單系統

組員姓名:
108753208 葉冠宏 109753209 李庭慶 110703065 詹松霖
110753113 張皓博 110753147 王盛泰 110753161 鄭仁傑

## 專案簡介

* 目的:利用 Kafka的系統來實作點餐系統
* Kafka 具有擴展性、緩衝性、減少耦合性、負載平衡...等特性，適合處理大量的訂單資料。

## Files

* app.py:負責執行主網頁的介面。
* transaction.py:去接收Kafka的order_details訊息，然後發佈有關訂單的訊息，以及email的訊息至order_confirmed的topic，以確認訂單。
* order_backend.py:負責去接收由網頁輸入的訊息，並發佈至Kafka的Topic: order_details。
* analytics.py:去接收來自order_confirmed 的訊息，並負責統計目前賣最好的商品。
* emails.py:負責去接收來自Kafka的order_confirmed 的Topic，並由使用者email的message發送email到使用者的信箱，以確認訂單。

## 操作步驟

* STEP1:用command line 分別執行transaction.py, order_backend.py, analytics.py, emails.py。
* STEP2:執行app.py後，會跳出訂單頁面。使用者可以輸入自己的email，以及所訂購的餐點數量，例如:漢堡、三明治、可樂的數量。
* STEP3:使用者會在自己輸入的信箱内收到訂單確認。訊息包括各餐點的訂單數量以及訂單編號等。
