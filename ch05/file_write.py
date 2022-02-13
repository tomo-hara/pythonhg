#랜덤한 숫자를 만들기 위해 가져옵니다.
import random
#간단한 한글 리스트를 만듭니다.
hanguls = list("가나다라마바")
#파일을 쓰기 모드로 엽니다.
with open("info.txt", "w") as file:
    for i in range(9):
        #랜덤한 값으로 변수를 생성합니다.
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(20,40)
        height = random.randrange(5,10)
        #텍스트를 씁니다.
        file.write("{}, {}, {}\n".format(name, weight, height))