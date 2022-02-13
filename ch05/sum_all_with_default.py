def sum_all(start=0, end=100,step=1):
    output =0
    for i in range(start, end+1, step):
        output += i
    return output

print("A.", sum_all(0, 100, 2))
print("B.", sum_all(end=50))
print("C.", sum_all(end=50,step=2))