import re

str = '12+2-3*34-56+12'
ret = re.finditer('\d+', str)
if ret:
    for i in ret:
        print(i.group())
