numbers = []

# לולאה לקליטת מספרים
while True:
    num = int(input("הכנס מספר: "))


    # אם המספר הוא תלת ספרתי, יציאה מהלולאה
    if num > 99:
        break

    # הוספת המספר לרשימה
    numbers.append(num)


# הדפסת המספר הגדול ביותר והקטן ביותר
print("המספר הגדול ביותר שנקלט:", max(numbers))
print("המספר הקטן ביותר שנקלט:", min(numbers))