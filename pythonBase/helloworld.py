import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

message = 'XIAOHUAHUA'
# print(message.title())

message1 = ' xiaoxiaoxio '
# 去尾部空格
# print(message1.rstrip())
# print(message1)
# print(message1.strip())

num = 2
# print(num ** 5)

message2 = 'qqqq' + str(num) + 'oooo'
# print(message2)
# print(5+3)
# print(5 * 3)
# print(5 / 3)
# print(5 - 3)

bic = ['sss', 'ddd', 'fff', 'eee']
# bic[0] = 'rrr'
# bic.append('www')
# bic.insert(1, 'ggg')
# del bic[4]
# bic.remove('fff')
# bic.sort()
# print(bic)

# for b in bic:
#   print(b)
# print('---')

# for value in range(10,50):
#   print(value)

# number = list(range(1,10, 2))
number = list(range(1,10))
# print(min(number))
# print(max(number))
# print(sum(number))

squares = [value**2 for value in range(1, 11)]
# print(squares)

# for value in range(1,21):
#   print(value)

# lists = list(range(1,1000001))
# for value in lists:
#   print(value)
# print(sum(lists))

# list3 = range(3, 31, 3)
# for list31 in list3:
#   print(list31)

lists = list(value**3 for value in range(1,11))
len1 = 3
# print(lists[1:4])
# print(lists[-len1:])
# for value in lists[:len1]:
#   print(value)
list2s = lists[:]
# print(list2s)
# lists.append(23)
# print(list2s)
# print(lists)

ganso = (2,3)
# print(ganso[0])
# print(ganso[1])
# for value in ganso:
#   print(value)

ganso = (4,5)
# for value in ganso:
#   print(value)

food = ('xiaoji', 'xiaoya', 'xiaoe', 'xiaoniao')
# for value in food:
  # print(value)

# food[0] = 'xiaoxiao'

# print(food)

cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#   if car == 'bmw':
#     print(car.upper())
#   else:
#     print(car.title())

age = 18
# if age == 18 and age < 10:
#   print(age)
# elif age > 10:
#   print(age - 1)
# else:
#   print(age + 1)

inlist = [1, 2, 4, 5]
# print(1 in inlist)
# print(8 not in inlist)

isTrue = True
isFalse = False
# print(isTrue, isFalse)

reList = [1]
# if reList:
#   print('wahha')
# else:
#   print('---哈哈')

dictionaries = { 'color': 'red', 'points': 3, 'wahaha': 3 }
# print(dictionaries['color'])
# print(dictionaries['points'])

# del dictionaries['color']
# print(dictionaries)
# for key, value in dictionaries.items():
#   print(str(value) + '-' + str(key))

# for name in dictionaries.keys():
#   print(name)

# for value in set(dictionaries.values()):
#   print(value)

# message = input('wahha:iiiii')
# print(message + 'helloworld')

message  = '18'
# print(message)
# print(int(message))

count = 1
# while count <= 5:
#   count += 1
#   print(count)

unconfirmed = ['eee', 'ddd', 'fff', 'eee', 'rrr', 'ddd', 'eee']
unconfirmed_list = []
# while unconfirmed:
#   unconfirmed_list.append(unconfirmed.pop())
# print(unconfirmed_list)
# while 'eee' in unconfirmed:
#   unconfirmed.remove('eee')
# print(unconfirmed)

# def xiaoming(xiao, huahua):
#   print(xiao + 'xiaohua' + huahua)
#   return xiao + 'hua' + huahua
# print(xiaoming(huahua="haha", xiao='wa'))

# def get_unconfirmed(unconfirmeds):
#   for value in unconfirmeds:
#     value += '---'
#   return unconfirmeds

# print(get_unconfirmed(unconfirmed[:]))
# unconfirmed.append('yyy')
# print(unconfirmed)

def make_pizza(*toppings):
  print(toppings)
make_pizza('wahha')
make_pizza('www', ';eee', 'rrr', 'ccc', 'ffff')