import numpy as np
import pandas as pd
df = pd.read_csv('mlbootcamp5_train.csv', sep=';', index_col='id')
data = [ df[df["gender"] == 1], df[df["gender"] == 2] ]
w = [0,"Woman"]
m = [1,"Man"]
if data[0]['height'].mean() > data[1]['height'].mean():
     w = [1,"Woman"]
     m = [0,"Man"]
mc = data[m[0]].count().gender
wc = data[w[0]].count().gender
#task1
print("\n #task1")
print(m[1] + ": " + str(mc))
print(w[1] + ": " + str(wc))
#task2
print("\n #task2")
use_alco = len(data[m[0]][data[m[0]]['alco'] == 1]) / len(data[m[0]])
print(m[1] + " mean use alco: " + str(use_alco))
use_alco2 = len(data[w[0]][data[w[0]]['alco'] == 1]) / len(data[w[0]])
print(w[1] + " mean use alco: " + str(use_alco2))
#task3
print("\n #task3")
use_smoke = len(data[m[0]][data[m[0]]['smoke'] == 1]) / len(data[m[0]])
use_smoke2 = len(data[w[0]][data[w[0]]['smoke'] == 1]) / len(data[w[0]])
print("Avarage man use smoke: " + str(round(use_smoke / use_smoke2, 0)) + "%")
#task4
print("\n #task4")
someke_to_not = round(df[df['smoke'] == 0].age.median() / 365 * 12, 0) - round(df[df['smoke'] == 1].age.median() / 365 * 12, 0)
print("Smoke to not: " + str(someke_to_not))     
#task5
print("\n #task5")
good_man = data[m[0]][
    (data[m[0]]['smoke'] == 0) &
    (data[m[0]]['ap_hi'] <= 120) &
    (data[m[0]]['cholesterol'] == 1) &
    (data[m[0]]['age'] > 21914) & (data[m[0]]["age"] < 23740)
]
print("Good:", len(good_man))
worth_man = data[m[0]][
    (data[m[0]]['age'] > 21914) & (data[m[0]]["age"] < 23740) &
    (data[m[0]]['smoke'] == 1)
]
print("Worth:", len(worth_man))
group_one = worth_man[(worth_man['ap_hi'] < 120) & (worth_man['cholesterol'] == 1)]
group_one_with_cardio = group_one[group_one['cardio'] == 1]
print("\nGroup one:", len(group_one))
print("Group one with cardio:", len(group_one_with_cardio))
print("Percent:", round((len(group_one_with_cardio) / len(group_one))*100, 4))
group_second = worth_man[((worth_man['ap_hi'] >= 160) & (worth_man['ap_hi'] < 180)) & (worth_man['cholesterol'] == 3)]
group_second_with_cardio = group_second[group_second['cardio'] == 1]
print("\nGroup second:", len(group_second))
print("Group second with cardio:", len(group_second_with_cardio))
print("Percent:", round((len(group_second_with_cardio) / len(group_second))*100, 4))
#task6
print("\n #task6")
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
print("1: ", 18.5 <= df['BMI'].median() <= 25)
print("2: ", df[df['gender'] == 1]['BMI'].mean() < df[df['gender'] == 2]['BMI'].mean())
print("3: ", df[df['cardio'] == 1]['BMI'].mean() < df[df['cardio'] == 0]['BMI'].mean())
if ((df[(df['alco'] == 0) & (df['cardio'] == 0) & (df['gender'] == 2)]['BMI'].mean() - 25) <
    (df[(df['alco'] == 0) & (df['cardio'] == 0) & (df['gender'] == 1)]['BMI'].mean() - 25)):
    print("4: ", True)
else:
    print("5: ", False)
#task7
print("\n #task7")
cancle_data = df.drop(df[df["ap_lo"] > df["ap_hi"]].index)
cancle_data = cancle_data.drop(cancle_data[cancle_data['height'] < cancle_data['height'].quantile(0.025)].index)
cancle_data = cancle_data.drop(cancle_data[cancle_data['height'] > cancle_data['height'].quantile(0.975)].index)
cancle_data = cancle_data.drop(cancle_data[cancle_data['weight'] < cancle_data['weight'].quantile(0.025)].index)
cancle_data = cancle_data.drop(cancle_data[cancle_data['weight'] > cancle_data['weight'].quantile(0.975)].index)
print("Cancle data:", round((1 - len(cancle_data) / len(df))*100, 4), "%")
#task8
print("\n #task8")
data[m[0]]['BMI'] = data[m[0]]['weight'] / (data[m[0]]['height'] / 100) ** 2
first_bad_bmi = data[m[0]].drop(data[m[0]][data[m[0]]['BMI'] < 31].index)
first_bad_bmi = len(first_bad_bmi.drop(first_bad_bmi[first_bad_bmi['BMI'] > 35].index))
print(m[1] + " with bad BMI: " + str(first_bad_bmi))
data[w[0]]['BMI'] = data[w[0]]['weight'] / (data[w[0]]['height'] / 100) ** 2
first_bad_bmi2 = data[w[0]].drop(data[w[0]][data[w[0]]['BMI'] < 31].index)
first_bad_bmi2 = len(first_bad_bmi2.drop(first_bad_bmi2[first_bad_bmi2['BMI'] > 35].index))
print(w[1] + " with bad BMI: " + str(first_bad_bmi2))