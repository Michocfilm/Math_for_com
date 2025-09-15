count = 0
for i in range(ord('a'), ord('z') + 1):
   count += 1
   char = chr(i)
   print(f"{char} = {i}",end="\t")
   if(count%5 == 0):
      print()