a,k = map(int,input().split())
a_list=list(map(int,input().split()))

tmp=[0 for _ in range(a)]
def merge_sort(a_list, p, r):
    
    global k
    #cnt+=1
    if(p<r):
        q = (p+r)//2
        merge_sort(a_list, p, q)
        merge_sort(a_list, q+1, r)
        merge(a_list,p,q,r)
        

def merge(a_list, p, q, r):
    i=p
    j=q+1
    t=0
    global tmp
   
    while(i<=q and j<=r):
        if a_list[i] <= a_list[j]:
            tmp[t]=a_list[i]
            result.append(tmp[t])
            t+=1
            i+=1
        else:
            tmp[t]=a_list[j]
            result.append(tmp[t])
            t+=1
            j+=1
    while (i<=q):
        tmp[t]=a_list[i]
        result.append(tmp[t])
        t+=1
        i+=1
    while (j<=r):
        tmp[t]=a_list[j]
        result.append(tmp[t])
        t+=1
        j+=1
    i=p
    t=0
    while(i<=r):
        a_list[i]=tmp[t]
        i+=1
        t+=1
    
result=[]
merge_sort(a_list,0,len(a_list)-1)
if len(result)>=k:
    print(result[k-1])
else:
    print(-1)
