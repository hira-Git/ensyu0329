import calc_bmi

print("BMI計算アプリ")
w = int(input("体重(kg)を入力"))
h = float(input("身長(m)を入力"))
print(f"あなたのBMIは{calc_bmi.get_bmi(w,h)}")
