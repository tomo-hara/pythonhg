#함수와 반복문 조합하기
example_list=["요소A","요소B","요소C"]

#0번째 요소는 A입니다.
#1번째 요소는 B입니다.
#2번째 요소는 C입니다.

# (1) #
# idx = 0
# for i in example_list:    
#     print("{}번째 요소는 {}입니다.".format(idx, i))
#     idx += 1

# PYTHONIC - enumerate #

#그냥 출력합니다.
print(example_list)
print()

#enumerate() 함수를 적용해 출력합니다.
print(enumerate(example_list))
print()

#list() 함수로 강제 변환해 출력합니다.
print(list(enumerate(example_list)))

#for 반복문과 enumerate() 함수 조합해서 사용하기
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))