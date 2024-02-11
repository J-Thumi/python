
for j in range(15):
       
            if j==0:
                print(' ',end="")
         
            if j==1 :
                
                print('x'*3,end="")
           
            if j==5 :
                    
                print(' '*4,end="")
                
            if j==8 : 
                
                print('x'*6,end="")
print()
for i in range(5):
        for j in range(4):
            if j==0 or j==3:
                print("X",end="")
            
            if j==3:
                print(' '*2,end='')
            if j==3 :
                a=i+1
                print("X"+"/"*a+"-"*(6-a),end="")
            if j==3:
                print('X',end='')
           
            else:
                print('-',end="")
        print()
        

for j in range(15):
        
        if j==0:
            print(' ',end="")
        if j==1:
                print('x'*6+'X'+'~'*6+'X'+' '*3+'x'*3,end="")
print()

for i in range (1,6):
    print(' '*7+'X'+'-'*(6-i)+'\\'*i+'X'+' '*2+'X'+'-'*3+'X')


print(' '*7+'X'+'~'*6+'X'+'x'*6)
for i in range(6):
    print(' '*7+'X'+'~'*6+'X')

        
            
            
        
           
    
