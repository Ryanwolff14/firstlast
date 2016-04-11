def firstorlast(): 
     first_last = input("Please input \n") 
     first_element = int(first_last[0]) 
     last_element = int(first_last[-1]) 
     
     if (first_element == 6) or (last_element == 6): 
        print("true")
     else: 
        print("false")

firstorlast()