import qrcode

UPI_ID = input("Enter you upi id: ")

paytm_url =f"upi://pay?pa={UPI_ID}&pn=Recipient%20Name&mc=1234"
google_pay_url =f"upi://pay?pa={UPI_ID}&pn=Recipient%20Name&mc=1234"
phonepe_url =f"upi://pay?pa={UPI_ID}&pn=Recipient%20Name&mc=1234"

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()