password = 'a123456'
time = 3 # 剩餘機會
while time > 0:	
	password_try = input('請輸入密碼')
	if password_try == password:
		print('登入成功')
		break
	else:
		time = time - 1
		print('密碼錯誤，還有', time,'次機會')