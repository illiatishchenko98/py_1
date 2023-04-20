# # # i = 10

# # # while i < 50:
# # #     print(i)
# # #     i += 5


# # import random


# # random_num = random.randint(1, 5)
# # while True:
# #     num = int(input('Guess a number from 1 to 5: '))
# #     if num != random_num:
# #         print('Try again...')
# #         continue
# #     print('Congratulations!', random_num)
# #     break


# # while True:
# #     try:
# #         a = float(input('Print first number: '))
# #         b = float(input('Print second number: '))
# #     except ValueError as e:
# #         print(e)
# #         print('Write a number')
# #         continue
# #     ab = a / b
# #     print(ab)
# #     abc = input('Do you want to continie?: ')
# #     if abc == 'yes':
# #         continue
# #     print(ab)
# #     break


# # a = [-10, -21, 2, -1111, 121]

# # abc = []

# # for q in a:
# #     abc.append(abs(q))

# # print(abc)


# # a = {1, 10, 15}
# # b = set()

# # for q in a:
# #     b.add(q * q)


# # print(b)


# # a = {1, 10, 15}

# # b = {val * val for val in a}

# # print(b)


# # a = {'a': 24,
# #      'b': 142,
# #      'c': 43646
# #      }


# # abc = {k: v * v for k, v in a.items()}

# # print(abc)


# # abc = {}

# # for k, v in a.items():
# #     abc[k] = v * v
# # print(abc)


# # a = [10, 7, 11]

# # abc = {index: value * 2 for index, value in enumerate(a)}

# # print(abc)


# # # abc = {l.upper(): da[l] for l in da}

# # # print(abc)


# # # abc = {k.upper(): v for k, v in da.items()}

# # # print(abc)


# da = {'f': 12, 'p': 12, }


# ab = {}

# for k, v in da.items():
#     ab[k] = v * 2
# print(ab)


# a = {'a': 24,
#      'b': 142,
#      'c': 43646
#      }


# abc = {}

# for k, v in a.items():
#     abc[k] = v * v
# print(abc)


# a = {'a': '24', 'b': 'abc'}


# b = {k.upper(): v for k, v in a.items()}

# print(b)


# a = ['a', 'b', 'c', 'adsadas']
# b = [k for k in a if len(k) > 3]
# print(b)


# a = [12, 2132, 12]
# b = []
# for bob in a:
#     print(bob)
# print(b)


# def abc(a, b):
#     abcd = []
#     for f in a:
#         if type(f) == b:
#             abcd.append(f)
#     return abcd


# print(abc([13132, 1313, 'abc', True], int))


# a = [12, 131, 242]

# # for q in a:
# #     q = a
# # print(q)
# b = [q for q in a]

# print(b)
