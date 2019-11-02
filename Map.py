alien_0 = {'color': 'green', 'points': 5}

print(alien_0)
print(alien_0['color'])
print(alien_0['points'])


# 为map添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 为map删除键值对
del alien_0['x_position']
print(alien_0)

# 修改键值对value
alien_0['color'] = 'yellow'
print(alien_0)

# 遍历键值对
for key, value in alien_0.items():
    print("\nKey: " + key)
    print("Value: " + str(value))

# 只遍历key值
for key in alien_0.keys():
    print("\nKey: " + key)

# 只遍历value值
for value in alien_0.values():
    print("Value: " + value)

# 按照顺序进行遍历
for key in sorted(alien_0.keys()):
    print("\nKey: " + key)
