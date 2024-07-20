person = {'name': 'Jenn', 'age': 23, "gender": 'female', "address" : "No, 430, 3rd lane, Embilipitiya", "phone" : "+94777 123 4567"}
query = input("What information do you need (name/age/gender/address/phone) ? ")
print(person.get(query, "Required information not available!"))