# #리스트를 선언하고 뒤집습니다.
# list_a = [1,2,3,4,5]
# list_reversed=reversed(list_a)

# #출력합니다
# print("reversed([1,2,3,4,5]) : ",list_reversed)
# print("list(reversed([1,2,3,4,5])) : ",list(list_reversed))
# print()

# # #반복문을 적용해봅니다.
# print("for i in reversed([1,2,3,4,5]) :")
# for i in reversed(list_a):
#     print("-",i)

##처음 공부할 때 이해가 안되던 코드
# temp = reversed([1,2,3,4,5])

# for i in temp:
#     print("첫 번째 반복문: {}".format(i))
# for i in temp:
#     print("두 번째 반복문: {}".format(i))

##따라서 이렇게 작성하세요
temp = [1,2,3,4,5]

for i in reversed(temp):
    print("첫 번째 반복문: {}".format(i))
for i in reversed(temp):
    print("두 번째 반복문: {}".format(i))
    