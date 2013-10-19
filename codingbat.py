def sleep_in(weekday, vacation):
  if vacation or (not weekday): return True
  return False


def monkey_trouble(a_smile, b_smile):
    if (a_smile == b_smile): return True 
    return False 

def sum_double(a, b):
    if a == b: return 2*(a+b)
    return a+b

def diff21(n):
  
   if n>21: return abs(n-21)*2
   return abs(n-21)
   
def parrot_trouble(talking, hour):
  
    if talking and (hour < 7 or hour > 20): return True
    return False

def makes10(a, b):
  #tried a shorter more compact way
  return a==10 or b==10 or a+b==10

 def near_hundred(n):
    return abs(200-n) <= 10 or abs(100-n)<= 10
  


 