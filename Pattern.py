'''
* 
* * 
* * * 
* * * * 
* * * * *

'''
rows=5
for i in range(0,rows):
    for j in range(0,i+1):
        print("* ",end="")
    print()    
print("==================================")

'''
      * 
     * * 
    * * * 
   * * * * 
  * * * * *

'''

for i in range(0,rows):
    for j in range(0,rows-i):
        print(" ",end="")
    for k in range(j,j+i+1):
        print("* ",end="")    
    print()    
print("====================================")

'''

* * * * *  
* * * *  
* * *  
* *  
* 

'''    

for i in range(0,rows):
    for i in range(0,rows-i):
        print("* ",end="")
    print()    
print("======================================")

'''
           * * * * * * * * * * 
            * * * * * * * * * 
             * * * * * * * * 
              * * * * * * * 
               * * * * * * 
                * * * * * 
                 * * * * 
                  * * * 
                   * * 
                    *
'''

for i in range(0,rows):
    for j in range(0,i+1):
        print(" ",end="")
    for k in range (j ,rows-j+i):
        print("* ",end="")    
    print()    
print("======================================")


'''
              * 
             * * 
            * * * 
           * * * * 
          * * * * * 
         * * * * * * 
        * * * * * * * 
       * * * * * * * * 
      * * * * * * * * * 
       * * * * * * * * 
        * * * * * * * 
         * * * * * * 
          * * * * * 
           * * * * 
            * * * 
             * * 
              *
'''

for i in range(0,rows):
    for j in range(0,rows-i):
        print(" ",end="")
    for k in range(j,j+i+1):
        print("* ",end="")  
    print()  
for i in range(0,rows):
    for j in range(0,i+1):
        print(" ",end="")
    for k in range (j ,rows-j+i):
        print("* ",end="")    
    print()    
print("======================================")

'''
*  
* *  
* * *  
* * * *  
* * * * *  
* * * * * *  
* * * * * * *  
* * * * * * *  
* * * * * *  
* * * * *  
* * * *  
* * *  
* *  
*
'''

for i in range(0,rows):
    for j in range(0,i+1):
        print("* ",end="")
    print()  
for i in range(0,rows):
    for i in range(0,rows-i-1):
        print("* ",end="")
    print()    
print("======================================")

'''
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
        * 
       * * 
      * * * 
     * * * * 
   * * * * * 
  * * * * * *

'''
for i in range(0,rows):
    for j in range(0,i+1):
        print(" ",end="")
    for k in range (j ,rows-j+i):
        print("* ",end="")    
    print()
for i in range(0,rows):
    for j in range(0,rows-i):
        print(" ",end="")
    for k in range(j,j+i+1):
        print("* ",end="")    
    print()    
print("====================================")        