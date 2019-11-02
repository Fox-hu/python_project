# 带默认参数的函数定义 无返回值
def greet_user(username, age=10):
    print("hello, " + username.title() + "!")
    print("your age is  " + str(age) + "!")


greet_user(username='angel', age=20)
greet_user(username='hh')


# 带返回值的函数定义
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name


print(get_formatted_name("sliver", "fox"))


# 返回字典
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


print(build_person("silver", "fox"))


# 传递任意数量的实参
def make_pizza(*toppings):
    print('\nMaking a pizza with the following soppings')
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushroms', 'green peppers', 'extra cheese')


# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
