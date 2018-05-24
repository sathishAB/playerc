a = int(input(" Enter any Number: "))    
Reverse = 0    
while(a > 0):    
  Reminder = a %10    
  Reverse = (Reverse *10) + Reminder   
  a = a //10    
print("\n Reverse of number is = %d" %Reverse)   
