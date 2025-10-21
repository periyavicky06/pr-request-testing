def runtime(func):
def display():
return len(func())
return display
@runtime
def username():
return "welcome to vglug" 
print (username())
