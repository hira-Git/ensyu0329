import calc_bmi

print("BMI計算アプリ")
w = int(input("体重(kg)を入力"))
h = float(input("高さ(m)を入力"))
for i in range(0,2):
    print(f"あなたのBMIは{calc_bmi.get_bmi(w,h)}")
