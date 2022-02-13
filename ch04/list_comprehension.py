# #for_list01.py
# #변수를 선언합니다.
# array = []

# #반복문을 적용합니다.
# for i in range(0, 10, 2):
#     array.append(i*i)

# #출력합니다.
# print(array)

# #list_in.py
# #리스트를 선언합니다.
# array = [i*i for i in range(0, 10, 2)]

# #출력합니다.
# print(array)

#array_comprehensions.py
#리스트를 선언합니다.
array = ["사과", "자두", "체리"]
output = [fruit for fruit in array if fruit != "체리"]

#출력합니다.
print(output)