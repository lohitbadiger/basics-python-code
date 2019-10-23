list = [1,2,3,4,5]  
flag = 0  
for i in list:  
    print("Current element:",i,end=" \n");  
    if i==3:  
        pass;  
        print("\nWe are inside pass block\n");  
        flag = 1;  
    if flag==1:  
        print("\nCame out of pass\n");  
        flag=0;  
        
        
# Flag variable is used as a signal in programming to let the program know that a certain condition has met. It usually acts as a boolean variable indicating a condition to be either true or false.