x = 10
y = 20
z = 30

# if condition
# if x < y:
#     print(f"{y} is grater than {x}")

# if - else condition
# if x > y:
#     print(f"if part -> {x} is grater than {y}")
# else:
#     print(f"else part -> {y} is grater than {x}")

# if - elif - else condition
if x > y:
    print(f"if part -> {x} is grater than {y}")
elif x > z:
    print(f"elif part -> {x} is grater than {z}")
elif y > z:
    print(f"elif part -> {y} is grater than {z}")
else:
    print(f"else part -> {z} is grater than {x} or {y}")