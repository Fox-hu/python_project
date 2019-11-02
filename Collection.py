# 列表解析 for作为表达式传递给value 此时for没有冒号
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 列表切片
print(squares[0:4])
print(squares[1:])
print(squares[:4])

# 遍历切片
for value in squares[0:5]:
    print(value)

# 复制切片
squares1 = squares[:]
del squares1[-1]
print(squares)
print(squares1)