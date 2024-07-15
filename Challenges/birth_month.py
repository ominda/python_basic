months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
birth_day = input("Enter your birthday (DD-MM-YYYY): ")
birth_month = int(birth_day.split("-")[1])
print(f"You were born in {months[birth_month-1]}")