import collections
import re

path = '/usr/lib/python3.5/LICENSE.txt'
words = re.findall('\w+', open(path).read().lower()) # 获取全不符合条件的内容，正则表达式。
c = collections.Counter(words).most_common(10) # most_common() 返回最常见的元素及其计数。
print(c)
