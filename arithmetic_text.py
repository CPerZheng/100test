"""
<算法图解>第六章 广度搜索
edit by Cper
2023/09/02
"""

from collections import deque

# 根据人际网络查询芒果商
"""
实现流程 找出自己的关系网, 逐个查询是否为芒果商
0.列出自己的朋友, 放到一个数组里
1.查询自己的朋友是否为芒果商, 是则返回朋友的名字, 否则查询该朋友的朋友
2.将已查询的名字剔除
"""


graph = {}
graph['you'] = ['a', 'b', 'c']
graph['a'] = ['d', 'e', 'f']
graph['b'] = ['g', 'h', 'i']
graph['c'] = ['j', 'k', 'l']
graph['d'] = ['m', 'n', 'o']
graph['e'] = ['p', 'q', 'r']
graph['f'] = ['s', 't', 'u']


def person_is_seller(name):
    person_list = list(graph[name])
    for item in person_list:
        if item[-1] == 'm':
            return item
    return False


def find_merchant(name):
    search_list = deque()
    search_list += graph[name]
    searched = []
    while search_list:
        person = search_list.popleft()
        if person not in searched:
            searched.append(person)
            merchant = person_is_seller(person)
            if merchant:
                tip = merchant + " is merchant"
                return tip
            else:
                search_list += graph[person]
    return False


print(find_merchant('you'))


