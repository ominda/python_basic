# Below is wrong 
fruits = ['apple', 'graps', 'orange', 'cherry', 'kivi']
result = map(lambda x: x.title(), fruits)

print(result)
for data in result:
    print(data, end=' ')