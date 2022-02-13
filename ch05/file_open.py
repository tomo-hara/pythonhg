# #파일을 엽니다.
# file = open("basic.txt", "w")

# #파일에 텍스트를 씁니다.
# file.write("안녕")

# #파일을 닫습니다.
# file.close()

#with 키워드를 활용한 파일 열기
with open("basic.txt", "w") as file:
    #파일에 텍스트를 씁니다.
    file.write("Hi")