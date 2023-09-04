from give_bmi import give_bmi
from give_bmi import apply_limit

height1 = [2, 1.15, 1.65, 1.95, 1.90]
weight1 = [165.3, 38.4, 62.2, 92, 73]

height2 = [2, 1.15, 1.65, 1.95, 1.90, 'hello']
weight2 = [165.3, 38.4, 62.2, 92, 73, 'world']

height3 = [2, 1.15, 1.65, 1.95, 1.90, 1.64]
weight3 = [165.3, 38.4, 62.2, 92, 73]

height4 = []
weight4 = [165.3, 38.4, 62.2, 92, 73]

height5 = 1
weight5 = 'hello'

print("\n\nExample 1")
try:
    bmi = give_bmi(height1, weight1)
    print(bmi)

    limits = apply_limit(bmi, 25)
    print(limits)
except Exception as e:
    print("Error:", e)

print("\n\nExample 2")
try:
    bmi = give_bmi(height2, weight2)
    print(bmi)

    limits = apply_limit(bmi, 25)
    print(limits)
except Exception as e:
    print("Error:", e)

print("\n\nExample 3")
try:
    bmi = give_bmi(height3, weight3)
    print(bmi)

    limits = apply_limit(bmi, 25)
    print(limits)
except Exception as e:
    print("Error:", e)

print("\n\nExample 4")
try:
    bmi = give_bmi(height4, weight4)
    print(bmi)

    limits = apply_limit(bmi, 25)
    print(limits)
except Exception as e:
    print("Error:", e)

print("\n\nExample 5")
try:
    bmi = give_bmi(height5, weight5)
    print(bmi)

    limits = apply_limit(bmi, 25)
    print(limits)
except Exception as e:
    print("Error:", e)
