height = input('請輸入身高(公尺)：')
weight = input('請輸入體重(公斤)：')
height = float(height)
weight = float(weight)
bmi = weight/(height*height)
if height > 0 and weight > 0:
	if bmi < 18.5 and bmi >= 0:
		print('BMI = ', bmi, '體重過輕')
	elif bmi >=18.5 and bmi < 24:
		print('BMI = ', bmi, '正常範圍')
	elif bmi >= 24:
		print('BMI = ', bmi, '異常範圍')
else: 
	print('請重新輸入')