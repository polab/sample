fabiona_lst = []
for j,i in enumerate(range(0,56)):
  if i in range(0,2):
    fabiona_lst.append(i)
  
#print(fabiona_lst[j] + fabiona_lst[j + 1])




for j,i in enumerate(fabiona_lst):
  if i <  34:
    fabiona_lst.append((fabiona_lst[j] + fabiona_lst[j + 1]))
print(fabiona_lst)
