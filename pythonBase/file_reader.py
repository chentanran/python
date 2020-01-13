# with open('pi.txt') as file_object:
#   # contents = file_object.read()
#   # for line in file_object:
#   #   print(line.rstrip())
#   lines = file_object.readlines()
#   # print(contents)
# for line in lines:
#   print(line)

# with open('123.txt', 'w') as file_object:
#   file_object.write('我喜欢python')

def count_words(filename):
  try:
    print(filename)
  except FileNotFoundError:
    pass # ??????
  else:
    print('wahaha')

filenames = ['1.txt', '2.txt', '3.txt', '4.txt']
for filename in filenames:
  count_words(filename)