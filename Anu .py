def runtime(func):

2 def display():

3

return len(func())

4

return display

5 @runtime

6 def username():

return "welcome to vglug" 7

8 print (username())
