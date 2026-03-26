import pandas as pd
from sklearn.linear_model import LinearRegression

# some old student data i put together
data = {
    'attendance': [90,80,70,60,95,85,75,65,50,40],
    'study_hours': [20,15,10,5,25,18,12,8,4,2],
    'prev_grade': [85,75,65,55,90,80,70,60,50,40],
    'final_grade': [88,78,68,58,93,83,73,63,53,43]
}

df = pd.DataFrame(data)

X = df[['attendance', 'study_hours', 'prev_grade']]
y = df['final_grade']

model = LinearRegression()
model.fit(X, y)

print("Student Grade Predictor")
print("quick tool i made\n")

name = input("enter your name: ")

try:
    attendance = float(input("your attendance percentage? "))
    study_hours = float(input("how many hours do you study per week? "))
    prev_grade = float(input("your previous grade? "))

    prediction = model.predict([[attendance, study_hours, prev_grade]])[0]

    print("\nhey", name)
    print(f"your predicted final grade is {prediction:.1f}%")

    if prediction < 50:
        print("damn thats low... you should probably start attending classes and study more")
    elif prediction < 75:
        print("its okay but you can do better")
        print("try putting in a few more hours every week")
    else:
        print("looks good man, keep it up")

except:
    print("please enter numbers only")

print("\ngood luck with your studies bro!")