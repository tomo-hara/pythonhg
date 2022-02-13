# numbers=[1,2,3,4,5]
# print("::".join(map(lambda x:str(x),numbers)))

# numbers = list(range(1,10+1))

# print("#홀수만 출력")
# print(list(filter(lambda x:x%2!=0,numbers)))
# print()

# print("#3이상 7미만")
# print(list(filter(lambda x:3<=x<7,numbers)))
# print()

# print("#제곱해서 50미만")
# print(list(filter(lambda x:x**2<50,numbers)))
# print()

numbers = list(range(1,5+1))
print("#4의 배수는 3을 곱하고, 3의 배수는 2로 나눈다.")
print(map(lambda x: 3*x % 4  == 0, numbers))
print(list(map(lambda x: 3*x % 4 == 0 , numbers)))
print()
print(filter(lambda x: 3*x % 4 == 0, numbers))
print(list(filter(lambda x: 3*x % 4 == 0, numbers)))