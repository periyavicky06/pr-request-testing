 a=input()
 i=0
 while i < len(a):
if a[i] !=a[len(a)-i-1]:
break
   i = i+1
  if i==len(a):
 print("It is palindrome")
 else:
print("Not a palindrome")
