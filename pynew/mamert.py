tt= [0]*4
ta = [0,2,3,4]
ts =[4,3,1,5]


def fcfs(ta ,ts,tt):
    tw =[]
    for i in range(len(ts)):


        if sum(tt[:]) >= ta[i]:

            tt[i] = tt[i-1] + ts[i] 
            
        else:
            
            tt[i] = tt[i-1] + (ta[i]-tt[i-1]) +ts[i]
           
        tw.append(abs(ta[i] + ts[i] - tt[i]) )
    print(" Fjfc ")
    print(" ta   ts   tt   tw")
    print("_"*20)
    for i in range(len(ts)):

        print(" ",ta[i],"   ",ts[i],"   ", tt[i],"   ",tw[i])
        
    print(tt)
def sjf(ta ,ts: list,tt:list):
    tw =[0]*4
    indexs = [0]
    tss =ts.copy()
    tss.pop(0)
    tt[0] = ts[0]
    for i in range(1,len(ts)):
        indexs.append(ts.index(min(tss)))
        tss.remove( min(tss))
        ind =indexs[-1] if len(indexs) <2 else indexs[-2]
        tt[indexs[-1]] = tt[ind] + ts[indexs[-1]] 
        tw[indexs[-1]] =  abs(ta[indexs[-1]] + ts[indexs[-1]] - tt[indexs[-1]]) 
    
    
    
    print(" Fjfc ")
    print(" ta   ts   tt   tw")
    print("_"*20)
    for i in range(len(ts)):

        print(" ",ta[i],"   ",ts[i],"   ", tt[i],"   ",tw[i])
        
    print(tt)
def first_fit(mre , mre_bs):
    n = len(mre)
    loc = [None]*n
    fl1 = [False]*n
    fl2 = [False]*n
    jop =[]
    for i in range(len(mre)):
        jop.append(f"j{i}")
        for j in range(len(mre_bs)):
            if (mre[i] <= mre_bs[j] and fl1[i] == False and fl2[j] == False):
                fl1[i] = True
                fl2[j] = True
                loc[i]=j
    print("frist - fit")
    print("Process    Process_size    Block no")

    for x in range(len(mre)):
        print("  " , jop[x],"      ", mre[x] ,"\t\t" ,loc[x] if loc[x] != None else "Not allocated")
        
def bast_fit(mre , mre_bs):
    n = len(mre)
    loc = [None]*n
    fl1 = [False]*n
    fl2 = [False]*n
    jop =[]
    for i in range(len(mre)):
        jop.append(f"j{i+1}")
        temp = mre_bs.copy()
        for _ in range(len(mre_bs)):
            if (min(temp) >= mre[i] and fl1[i] == False and fl2[mre_bs.index(min(temp))] == False):
                fl1[i] = True
                fl2[mre_bs.index(min(temp))] = True
                loc[i]=mre_bs.index(min(temp))
            else:
                temp.remove(min(temp))
    
    print("bast - fit" , mer)
    bs ="Process    Process_size    Block no"
    print("-"*len(bs))
    print(bs)
    print("-"*len(bs))

    for x in range(len(mre)):
        print("  " , jop[x],"      ", mre[x] ,"\t\t" ,loc[x]+1 if loc[x] != None else "Not allocated")
        
mer = [20,200,500,50]         
mer_blo = [200,30 ,700,50]
first_fit(mer,mer_blo)
bast_fit(mer,mer_blo)
#sjf(ta,ts,tt)
#fcfs(ta,ts,tt)
