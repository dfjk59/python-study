#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# -*- coding: utf-8 -*-

from functools import reduce


def str2float(s):
    l = s.split('.')

    def char2num(s):
        return {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}[s]

    if l.__len__()>1:
        n1 = reduce(lambda x, y: x * 10 + y, map(char2num, l[0]))
        n2 = reduce(lambda x, y: x * 10 + y, map(char2num, l[1])) * (10**-(len(l[1])))
        return n1 + n2
    else:
       return reduce(lambda x, y: x * 10 + y, map(char2num, l[0]))


print('str2float(\'123.456\') =', str2float('123.456'))