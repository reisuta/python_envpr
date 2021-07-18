#ジェネレータ関数
# def generator(max):
#     print('ジェネレータ作成')
#     for n in range(max):
#         try:
#             x = yield n
#             print('x={}'.format(x))
#             print('yield実行')
#         except ValueError as e:
#             print('throwを実行しました。')

# gen = generator(10)
# next(gen)
# next(gen)
# gen.send(100)
# gen.throw(ValueError('Invalid Value'))
# gen.close()
# next(gen)
# n = next(gen)
# print('n={}'.format(n))
# n = next(gen)
# print('n={}'.format(n))
# for x in gen:
#     print('x = {}'.format(x))

#サブジェネレータ

def sub_sub_generator():
    yield "Sub subyield"
    return "sub sub return"

def sub_generator():
    yield "sub yield"
    res = yield from sub_sub_generator()
    print('sub res={}'.format(res))
    return "sub return"

def generator():
    yield "generator yield"
    res = yield from sub_generator()
    print('gen res={}'.format(res))
    return 'gen return'

gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))














