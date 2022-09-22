a = input()
b = input()
l = []
lb = []
flag = True

if len(a) != len(b):
  flag = False
else:
  for i in range(len(a)):
    for j in range(len(a)):
      if a[j] == b[j]:
        flag = False
        break

      if j in l or j in lb:
        continue
      
      if a[i] == a[j]:
        l.append(j)

      if b[i] == b[j]:
        lb.append(j)
      
        
if flag and l == lb:
  print("yes")
else:
  print("no")