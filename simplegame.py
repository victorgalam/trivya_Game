import random

# להגריל מספר אקראי בין 1 ל-10
number_to_guess = random.randint(1, 10)

# קבלת ניחוש מהמשתמש
guess = int(input("נחש מספר בין 1 ל-10: "))

# בדיקת הניחוש
if guess == number_to_guess:
    print("נכון! ניחשת את המספר!")
else:
    print(f"טעות! המספר הנכון היה {number_to_guess}. נסה שוב בפעם הבאה.")
