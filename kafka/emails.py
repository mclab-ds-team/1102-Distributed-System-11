import json
from kafka import KafkaConsumer
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
	
####################################################
content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "Food service"  #郵件標題
content["from"] = "zard102232@gmail.com"  #寄件者

content.attach(MIMEText("service completed\n"))  #郵件內容

######################################################

ORDER_CONFIRMED_KAFKA_TOPIC = "order_confirmed"


consumer = KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC, 
    bootstrap_servers="localhost:29092", 
           api_version=(2,0,2)
)

emails_sent_so_far = set()
print("Gonna start listening")
while True:
	for message in consumer:
		consumed_message = json.loads(message.value.decode())
		content.attach(MIMEText(f"你的訂單編號為 {consumed_message['order_id']}\n取餐門市為{consumed_message['position']}\n漢堡{consumed_message['food']['burger']}個、\n三明治{consumed_message['food']['sandwich']}個、\n可樂{consumed_message['food']['cola']}罐\n總共為{consumed_message['price']}元"))  #郵件內容
		customer_email = consumed_message["e-mail"]
		content["to"] = customer_email #收件者

		print(consumed_message)
		with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
			try:
				smtp.ehlo()  # 驗證SMTP伺服器
				smtp.starttls()  # 建立加密傳輸
				smtp.login("email here", "verification")  # 登入寄件者gmail
				smtp.send_message(content)  # 寄送郵件
				content = MIMEMultipart()
				content["subject"] = "Food service"  #郵件標題
				content["from"] = "zard102232@gmail.com"  #寄件者
				content.attach(MIMEText("service completed\n"))  #郵件內容
				print("Complete!")
			except Exception as e:
				print("Error message: ", e)

		print(f"Sending email to {customer_email} ")
		emails_sent_so_far.add(customer_email)
		print(f"So far emails sent to {len(emails_sent_so_far)} unique emails")
