import re
import new_eleusis
import Main
rule="or(even(current),equal(color(current),R),greater(prev,current))"
correct=['4H','2D','6H','8D']
#print rule
##for i in range(0,len(rule)):
##    if((i+2)!=len(rule) and (i+1)!=len(rule) and rule[i]==')' and rule[i+1]==')' and rule[i+2]==','):#and rule[i+2]==',' and (i+2)<=len(rule) and (i+1)<=len(rule)):
##            #print 'ggrg'if(rule[i+2]==','):
##        print rule[i+2]
##        d=rule.split(rule[i+2])
            
#print d[1]
##for i in range(0,len(rule)):
##    if(rule[i]=='equal'):
##        if(rule[i]==
##    if(rule[i]==',' and rule[i-1]==')' and rule[i-2]==')' ):
##        f=rule.split(')),')
##        break
##    if(rule[i]==',' and rule[i-1]==')' and rule[i-2]!=')'):
##        f=rule.split('),')
##        break
##    
##    
###list1=[]
##n={}
##for i in range(0,len(f)):
##    n[i]=re.findall("[\w']+",f[i])
##print nhn=[]
n=re.findall("[\w']+",rule)
print n
def prune(rule,correct):
    n=[]
    n=re.findall("[\w']+",rule)
    print n
    d=correct[(len(correct)-3):len(correct)]
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

    for i in range(0, len(n)):
            if(n[i]=='equal'):#k-m omk mk                                                                                                                                                      1
                    if(new_eleusis.equal(d[1],d[2])):
                        f.append('equal')
            if(n[i]=='greater'):
                print 'hello'
                print new_eleusis.value(d[0])
                if(new_eleusis.value(d[0])>new_eleusis.value(d[1]) and new_eleusis.value(d[1])>new_eleusis.value(d[2])):
                    print 'hello'
                    f.append('value_greater')
                else:
                    f.append('greater')
            if(n[i]=='less'):
                if(new_eleusis.value(d[0])<new_eleusis.value(d[1]) and new_eleusis.value(d[1])<new_eleusis.value(d[2])):
                    f.append('value_less')
                else:
                    #if(new_eleusis.less(d[1],d[2])):
                    f.append('less')
                        
    final=[]
    print final
    for x in f:#pruning is_color
                if x not in final:
                        final.append(x)

    print final                    
    str1="or("
    list=[]
    for s in range(0,len(final)):
        if(final[s]=='R'):
            list.append("equal(color(current),R)")
        if(final[s]=='B'):
            list.append("equal(color(current),B)")
        if(final[s]=='even'):
            list.append("even(current)")
        if(final[s]=='odd'):
            list.append("odd(current)")
        if(final[s]=='royal'):
            list.append("is_royal(current)")
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
            
    for i in list:
        str1+=i+","
    str1=str1[:len(str1)-1]
    str1+=")"
    print str1         
            
                    
                       

                    
##     c1=Main.extraction(correct[0])
##        c2=Main.extraction(correct[1])
##        c3=Main.extraction(correct[2])
##        d3=Main.comparator(c1,c2,c3)
##        i=3
##        while(i<len(correct)):
##                d2=Main.comparator(c1,c2,c3)
##                d1=d2.keys()
##                for i1 in range(0,len(d1)):
##                        for j in range(0,len(h)):
##                                if(d1[i1]==h[j]):
##                                        if(d2[d1[i1]]==1):
##                                                q.append(d1[i1])
##                c2=c1
##                c3=c2
##                c1=Main.extraction(correct[i])
##                i=i+1
##                if(i==len(correct)):
##                        break                   
    return str1
print prune(rule,correct)

                        
        


    
    
