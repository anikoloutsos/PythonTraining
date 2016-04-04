
#  @author: Zack


if __name__ == '__main__':
    
    print ('Copy-paste Colour Configuration')
    
    CCstring = input()
    
    ntiles = len(CCstring)
    
    nstrokes = 1
    
    print(str(ntiles))
    
    for i in range(1,ntiles):
        
        
              
        if CCstring[i] != CCstring[i-1] :
            
            nstrokes = nstrokes+1
        
        
        
    
        print (str(i)+'    '+CCstring[i]+'   '+str(nstrokes))
    print ('Number of strokes is : '+str(nstrokes))
    
    pass