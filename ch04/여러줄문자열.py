# #if_string.py
# number = int(input("정수 입력>"))

# #if 조건문으로 홀수 짝수를 구분합니다.
# if number % 2 == 0:
#     print("""\
#         입력한 문자열은 {}입니다.
#         {}는 짝수입니다.""".format(number,number))
# else:
#     print("""\
#         입력한 문자열은 {}입니다.
#         {}는 홀수입니다.""".format(number,number))

# #if_string01.py
# number = int(input("정수 입력>"))

# #if 조건문으로 홀수 짝수를 구분합니다.
# if number % 2 == 0:
#     print("""입력한 문자열은 {}입니다.
# {}는 짝수입니다.""".format(number,number))
# else:
#     print("""입력한 문자열은 {}입니다.
# {}는 홀수입니다.""".format(number,number))

# #if_string02.py
# number = int(input("정수 입력>"))

# #if 조건문으로 홀수 짝수를 구분합니다.
# if number % 2 == 0:
#     print("""입력한 문자열은 {}입니다. {}는 짝수입니다.""".format(number,number))
# else:
#     print("""입력한 문자열은 {}입니다. {}는 홀수입니다.""".format(number,number))

# #string01.py
# test = (
#     "이렇게"
#     "입력해도"
#     "됩니다."
# )

# #출력합니다.
# print("test : ",test)
# print("type(test) : ",type(test))

# #string02.py
# number = int(input("정수 입력>"))

# #if 조건문으로 홀수 짝수를 구분합니다.
# if number % 2 == 0:
#     print(
#         ("입력한 문자열은 {}입니다.\n"
#         "{}는 짝수입니다."
#     ).format(number,number))
# else:
#     print(
#         ("입력한 문자열은 {}입니다.\n"
#         "{}는 홀수입니다."
#     ).format(number,number))

#string03.py
#print("::".join(["1", "2","3","4","5"]))

#변수를 선언합니다.
number = int(input("정수 입력>"))

#if 조건문으로 홀수 짝수를 구분합니다.
if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다",
        "{}는 짝수입니다."
    ]).format(number,number))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다",
        "{}는 홀수입니다."
    ]).format(number,number))