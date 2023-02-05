password = 'a123456'
time = 3
while True:
	if time == 0:
		print('失敗太多次')
		break
	else:	
		password_try = input('請輸入密碼')
		if password_try == password:
			print('登入成功')
			break
		else:
			print('密碼錯誤，還有', time - 1,'次機會')
			time = time - 1	

