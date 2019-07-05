from collections import Counter

list1 = input().split()
list2 = input().split()
common_items = list((Counter(list1) & Counter(list2)).elements())


print(' '.join(common_items))
