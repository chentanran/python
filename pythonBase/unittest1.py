import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def get_function(first, last):
  full_name = first + ' ' + last
  return full_name

# while True:
#   first = input('请输入开始')
#   if first == 'q':
#     break
#   last = input('请输入结束')
#   if last == 'q':
#     break
#   formatted_name = get_function(first, last)
#   print('开始和结束时: ' + formatted_name)