import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

class Dog():
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.mark = 0
  def sit(self):
    print(self.name.title() + '蹲下')
  def rollOver(self):
    print(self.name.title() + '打滚')

# my_dog = Dog('xiaohua', 18)
# # print('my dog name is' + my_dog.name)
# # print('my dog age is' + str(my_dog.age))
# # print('my dog mark is' + str(my_dog.mark))
# my_dog.sit()
# my_dog.rollOver()
# my_dog.mark = 1
# print(my_dog.mark)

class ChineseRuralDog():
  def __init__(self, types='yellow'):
    self.types = types

class SmallDog(Dog):
  def __init__(self, name, age):
    super().__init__(name, age)
    self.chineseRuralDog = ChineseRuralDog()

my_dog = SmallDog('xiaohua', 19)
my_dog.sit()
print(my_dog.chineseRuralDog.types)