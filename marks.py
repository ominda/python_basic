# 0 - 35 -> W
# 35 - 55 -> S
# 55 - 65 -> C
# 65 - 75 -> B
# 75 - 100 -> A

marks = 150
results = ""

### > Normal way to check with if condition < ###
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks < 35:
    results = "W"
elif marks < 55:
    results = "S"
elif marks < 65:
    results = "C"
elif marks < 75:
    results = "B"
elif marks <= 100:
    results = "A"


### > Single line of logic for above condition < ###
# results = "W" if marks < 35 else ("S" if marks < 55 else ("C" if marks < 65 else ("B" if marks < 75 else ("A" if marks <= 100 else "Invalid Marks"))))

print(results)