i=0
resize=2
spike1=[9,8,7,6,5,4,3,2,1]
spike2=[]
spike3=[]
m1=0
m2=0
m3=0
ss=max(len(spike1),len(spike2),len(spike3))    
if spike1: m1=max(spike1)
if spike2: m2=max(spike2)
if spike3: m3=max(spike3)
m=max(m1,m2,m3)*resize
def index_exists(arr, index):
    return -len(arr) <= index < len(arr)
def showSpike(spike):    
    spike.reverse()
    for i in spike:
        
        for spaces in range((m-i*resize)//2):
            print(" ",end="")
        for spaces in range((i*resize)):
            print('X',end="")
        for spaces in range((m-i*resize)//2):
            print(" ",end="")
        
        print()
def showSpikes(spike1,spike2,spike3):    
    #ss=max(len(spike1),len(spike2),len(spike3))    
    for i in range(ss-1,-1,-1):        
    # spike 1    
        if index_exists(spike1,i):            
            for spaces in range((m-spike1[i]*resize)//2):
                print(" ",end="")
            for spaces in range((spike1[i]*resize)):
                print('X',end="")
            for spaces in range((m-spike1[i]*resize)//2):
                print(" ",end="")
        else:
            for spaces in range(m):
                print(" ",end="")
                
    # spike 2    
        if index_exists(spike2,i):            
            for spaces in range((m-spike2[i]*resize)//2):
                print(" ",end="")
            for spaces in range((spike2[i]*resize)):
                print('X',end="")
            for spaces in range((m-spike2[i]*resize)//2):
                print(" ",end="")
        else:
            for spaces in range(m):
                print(" ",end="")        
            
    # spike 3
        if index_exists(spike3,i):            
            for spaces in range((m-spike3[i]*resize)//2):
                print(" ",end="")
            for spaces in range((spike3[i]*resize)):
                print('X',end="")
            for spaces in range((m-spike3[i]*resize)//2):
                print(" ",end="")
        else:
            for spaces in range(m):
                print(" ",end="")
                
        print();
    print();

def printMove(fr, to):
    
    if fr=='P1':
        tmp=spike1[len(spike1)-1]        
        spike1.pop(len(spike1)-1)        
    if fr=='P2':
        tmp=spike2[len(spike2)-1]        
        spike2.pop(len(spike2)-1)        
    if fr=='P3':
        tmp=spike3[len(spike3)-1]
        spike3.pop(len(spike3)-1)
        
        
    if to=='P1':
        spike1.insert(len(spike1),tmp)
    if to=='P2':
        spike2.insert(len(spike2),tmp)
    if to=='P3':
        spike3.insert(len(spike3),tmp)
        
        
    showSpikes(spike1,spike2,spike3)

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

showSpikes(spike1,spike2,spike3)
Towers(len(spike1), 'P1', 'P2', 'P3')

