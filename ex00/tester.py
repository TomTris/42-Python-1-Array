from give_bmi import give_bmi, apply_limit

height = [  1,   1.21,  1.1,    2.2,     3.3,     4.4,    0.5]
weight = [  1,   125,   23.2,   96.6,    135.9,  256.7,   99]

bmi = give_bmi(height, weight)
print(bmi)
print(apply_limit(bmi, 10))