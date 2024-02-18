#customer = {
    #"name": "John Smith",
    #"is_verified": True,
    #"age": 30,
#}
#print(customer.get("birthdate", "Jan 1 1980"))

#You can either use customer["name"], if spelled incorrectly throws error. Using customer.get will return ""none" value if incorrectly spelled
#You can also user .get to add a value or update a value
#You can also just update a vlue but setting it equal like normal lol

#Exercise
phone = input("Phone: ")
digits_mapping = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four'
}
output =""
for ch in phone:
    output = digits_mapping.get(ch, '!') + ' '
    print(output)