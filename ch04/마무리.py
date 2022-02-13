#리스트 내포를 사용햅노 코드입니다.
output = [num for num in range(1,101) if "{:b}".format(num).count("0") == 1]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:",sum(output))