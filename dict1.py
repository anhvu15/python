# d = {
#     "Name": "Guido",
#     "Age": 56,
#     "BDFL": True
# }
# for a,b in d.items():
# 	print(a,b)

# for a in d.keys():
# 	print(a)

# for b in d.values():
# 	print(b)

# #create a comprehesive list
# my_list = [x**3 for x in range(1,11) if x % 2 != 0]
# my_list = [x**3 for x in range(1,11) if x % 4 == 0]
# print(my_list)
squares = [x**2 for x in range(1,11)]
a = filter(lambda x: x >= 30 and x <= 70,squares)
print (a)