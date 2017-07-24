#First In First Out Page Replacement Algorithm
def __fifo():
    global a,n,m
    f = -1
    page_faults = 0
    page = []
    for i in range(m):
        page.append(-1)

    for i in range(n):
        flag = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag = 1
                break

        if flag == 0:
            f=(f+1)%m
            page[f] = a[i]
            page_faults+=1
            print "\n%d ->" % (a[i]),
            for j in range(m):
                if page[j] != -1:
                    print page[j],
                else:
                    print "-",
        else:
            print "\n%d -> No Page Fault" % (a[i]),
            
    print "\n Total page faults : %d." % (page_faults)

#Least Recently Used Page Replacement Algorithm
def __lru():
    global a,n,m
    x = 0
    page_faults = 0
    page = []
    for i in range(m):
        page.append(-1)

    for i in range(n):
        flag = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag = 1
                break
            
        if flag == 0:
            if page[x] != -1:
                min = 999
                for k in range(m):
                    flag = 0
                    j =  i
                    while j>=0:
                        j-=1
                        if(page[k] == a[j]):
                            flag = 1
                            break
                    if (flag == 1 and min > j):
                        min = j
                        x = k

            page[x] = a[i]
            x=(x+1)%m
            page_faults+=1
            print "\n%d ->" % (a[i]),
            for j in range(m):
                if page[j] != -1:
                    print page[j],
                else:
                    print "-",
        else:
            print "\n%d -> No Page Fault" % (a[i]),
            
    print "\n Total page faults : %d." % (page_faults)

#Optimal Page Replacement Algorithm
def __optimal():
    global a,n,m
    x = 0
    page_faults = 0
    page = []
    for i in range(m):
        page.append(-1)

    for i in range(n):
        flag = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag = 1
                break
            
        if flag == 0:
            if page[x] != -1:
                max = -1
                for k in range(m):
                    flag = 0
                    j =  i
                    while j<n:
                        j+=1
                        if(page[k] == a[j]):
                            flag = 1
                            break
                    if (flag == 1 and min < j):
                        max = j
                        x = k

            page[x] = a[i]
            x=(x+1)%m
            page_faults+=1
            print "\n%d ->" % (a[i]),
            for j in range(m):
                if page[j] != -1:
                    print page[j],
                else:
                    print "-",
        else:
            print "\n%d -> No Page Fault" % (a[i]),
            
    print "\n Total page faults : %d." % (page_faults)
