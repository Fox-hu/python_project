from Funtion import build_profile

print("hello world")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('hhhhh')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

for motorcycle in motorcycles:
    print(motorcycle)

for value in range(1, 5):
    print(value)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
print(sum(squares))
print(max(squares))
print(min(squares))

# 导入funtion模块中的函数
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

