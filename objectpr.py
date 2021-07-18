#map関数の練習

# man = {
#     'name': 'san',
#     'age': '17',
#     'country': 'japan'
# }

# map_man =  map(lambda y: y + ',' + man.get(y), man)
# for x in map_man:
#     print(x)

# def calculate(x,y,z):
#     if z == 'plus':
#         return x + y
#     elif z == 'minus':
#         return x - y

# map_sample  = map(calculate, range(1,5), [1,2,3,3,3], ['plus','minus','plus','minus', 'plus'])
# for i in map_sample:
#     print(i)

# def multiple_2(x):
#     return x *2

# list_a = [1,2,3]

# map_b = map(lambda x: x*6, list_a)
# for j in map_b:
#     print(j)

# map_a = map(multiple_2,list_a)
# print(map_a)
# for i in map_a:
#     print(i)

#lambda の練習
y = -10
x = 0 if y>0 else 3
print(x)

lambda_a = lambda x: x* x

print(lambda_a(5))













