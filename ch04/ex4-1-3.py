from numpy import number


numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

# for n in numbers:
# 	if n % 2 == 0:
# 		print("{}은 짝수입니다.".format(n))
# 	else:
# 		print("{}은 홀수입니다.".format(n))

for n in numbers:
	print("{}의 자릿수는 {}입니다.".format(n, len(str(n))))