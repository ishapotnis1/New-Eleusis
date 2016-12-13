import re
import new_eleusis
import Main
#rule="orf(even(current),equal(color(current),B),equal(suit(current),S),less(value(prev),value(current)),notf(is_royal(current)))"
#correct=["4S", "6S", "8S","2H"]

##def func(p):
##    for k,v in p.iteritems():
##        ifp

def prune(rule,correct): #probability of current
    n=[]
    n=re.findall("[\w']+",rule)
    #print n
    #print n
    d=correct[len(correct)-3:len(correct)]
    #print d
    f=[]
    for i in range(0,len(d)):  #for general rule
        c=Main.extraction(d[i])
        #print c
        d1=c.keys()
        for i in range(0,len(d1)):
            for j in range(0,len(n)):
                if(d1[i]==n[j]):
                    if(c[d1[i]]==1):
                        f.append(d1[i])

    for i in range(0, len(n)):  #for greater,equal,less
            if(n[i]=='equal'):#k-m omk mk                                                                                                                                                      1
                    if(new_eleusis.equal(d[2],d[1]) and new_eleusis.equal(d[0],d[1])):
                        #print"equal"
                        f.append('equal')
            if(n[i]=='greater'):
                #print 'hello'
                #print new_eleusis.value(d[0])
                if(new_eleusis.value(d[len(d)-3])>new_eleusis.value(d[len(d)-2]) and new_eleusis.value(d[len(d)-2])>new_eleusis.value(d[len(d)-1])):
                    #print 'hello'
                    f.append('value_greater')
                else:
                    f.append('greater')
            if(n[i]=='less'):
                if(new_eleusis.value(d[len(d)-3])< new_eleusis.value(d[len(d)-2]) and new_eleusis.value(d[len(d)-2])< new_eleusis.value(d[len(d)-1])):
                    #print "hi" # and new_eleusis.value(d[len(d)-2])<new_eleusis.value(d[len(d)-1])):
                    f.append('value_less')
                else:                    #if(new_eleusis.less(d[1],d[2])):
                    f.append('less')

    #print "l"
    #print n
    count=0
    for i in range(0,len(n)):
        if(n[i]=='notf'):
           for j in range(0,len(d)):
               c1=Main.extraction(d[j])
               #print c1
               if(c1['royal']==1):
                   count=count+1
                   #print "hi"
                   break
           if(count>0):
                break
           else:
              f.append('not_royal')
        
                    
    for i in range(0,len(n)):
        if(n[i]=='less'):
            for j in range(0,len(f)):
                if(f[j]=='value_less' or f[j]=='less'):
                    for k in range(0,len(d)):
                        #print "hi1"
                        if(new_eleusis.value(d[len(d)-3])- new_eleusis.value(d[len(d)-2])==-1 and new_eleusis.value(d[len(d)-2])- new_eleusis.value(d[len(d)-1])==-1):
                            #print "hi2"
                            f.append('plus1')

    for i in range(0,len(n)):
        if(n[i]=='greater'):
            for j in range(0,len(f)):
                if(f[j]=='value_greater' or f[j]=='greater'):
                    for k in range(0,len(d)):
                        if(new_eleusis.value(d[len(d)-3])- new_eleusis.value(d[len(d)-2])== 1 and new_eleusis.value(d[len(d)-2])- new_eleusis.value(d[len(d)-1])==1):
                            #print "hi2"
                            f.append('minus1')
                              
    final=[]
    #print final
    for x in f:#pruning is_color
                if x not in final:
                        final.append(x)

    #print "pruned",final                    
    str1="orf("
    list=[]
    for s in range(0,len(final)):
        if(final[s]=='even'):
            list.append("even(current)")
        if(final[s]=='odd'):
            list.append("odd(current)")
        if(final[s]=='royal'):
            list.append("is_royal(current)")
        if(final[s]=='R'):
            list.append("equal(color(current),R)")
        if(final[s]=='B'):
            list.append("equal(color(current),B)")
        if(final[s]=='C'):
            list.append("equal(suit(current),C)")
        if(final[s]=='D'):
            list.append("equal(suit(current),D)")
        if(final[s]=='H'):
            list.append("equal(suit(current),H)")
        if(final[s]=='S'):
            list.append("equal(suit(current),S)")
        if(final[s]=='value_less'):
            list.append("less(value(prev),value(current))")
        if(final[s]=='less'):
            list.append("less(prev,current)")
        if(final[s]=='value_greater'):
            list.append("greater(value(prev),value(current))")
        if(final[s]=='greater'):
            list.append("greater(prev,current)")
        if(final[s]=='plus1'):
            list.append("plus1(value(prev),value(current))")
        if(final[s]=='minus1'):
            list.append("minus1(value(prev),value(current))")
        if(final[s]=='not_royal'):
            list.append("notf(is_royal(current))")
      

            
    for i in list:
        str1+=i+","
    str1=str1[:len(str1)-1]
    str1+=")"
    #print str1         
            
                    
                       

                    
             
    return str1
#print prune(rule,correct)
