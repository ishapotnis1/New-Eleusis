from new_eleusis import *
import scientist
count=0

cb={}

constraints={}
currentBestHypothesis={}
forvalidation={}
threshold=0.0

def pruning(hypothesis,correct,a1):
        k=hypothesis
        w=len(k)
        h=k.keys()
        print h
##        h1=[]
##        h2=[]
##        h3=[]
##        print "inprune"
##        #print k[h[0]][0]
##        for x in h[0]:#pruning is_color
##                print x
##                if x not  in h1:
##                        h1.append(x)
##        for x in h[1]:#pruning is_value
##                #print x
##                if x not  in h2:
##                        h2.append(x)
##        for x in h[2]:#pruning is_suit
##                #print x
##                if x not  in h3:
##                        h3.append(x)            
##        hypo=h1+h2+h3
##        #return hypo
##        #print hypo
        print "correct list"
        print correct
        f=[]
        q=[]
        for i in range(0,len(correct)):
                c=scientist.extraction(correct[i])
                #print correct
                #print c
                d=c.keys()
                for i in range(0,len(d)):
                        for j in range(0,len(h)):
                                if(d[i]==h[j]):
                                        if(c[d[i]]==1):
                                                f.append(d[i])
        final1=[]
        c1=scientist.extraction(correct[0])
        c2=scientist.extraction(correct[1])
        c3=scientist.extraction(correct[2])
        #print "d3"
        d3=scientist.comparator(c1,c2,c3)
        #print d3
        i=3
        while(i<len(correct)):
                d2=scientist.comparator(c1,c2,c3)
                #print c1
                d1=d2.keys()
                #print d2
                #print d2
                for i1 in range(0,len(d1)):
                        for j in range(0,len(h)):
                                if(d1[i1]==h[j]):
                                        if(d2[d1[i1]]==1):
                                                q.append(d1[i1])
                                                #print q
                #final1=[]+1
                c2=c1
                c3=c2
                c1=scientist.extraction(correct[i])
                i=i+1
                if(i==len(correct)):
                        break
                #i=i+1
                #c1=extraction(correct[i])
        for x in q:#pruning is_color
                        #print x
                        if x not  in final1:
                                final1.append(x)
        final=[]  
        for x in f:#pruning is_color
                 #print x
                if x not  in final:
                        final.append(x)
        final2=[]
        final_hypo={}
        if(len(a1)!=0):
                final2=a1.keys()        
                
        best=final+final1
        final_hypo['AND of rule']=best
        final_hypo['AND of Alternate']=final2
        if(final_hypo==None):
                 y=scientist.score(scientist.scoring,30)  #Score=30 if no hypthesis match with correct list
        return final_hypo

def scientist(hypothesis,flag,correct,a1,count_iter):
        temp={}
	tempconstraints={}
	tempValidation={}
	print "flag",flag
	if flag==20:
                w=pruning(currentBestHypothesis,correct,a1)
                print w
                return
        else:
                for field, possible_values in hypothesis.iteritems():
                        for a,x in possible_values.iteritems():
                                if x>0.15:
                                         currentBestHypothesis[a] = x
                                if x<0.05:
                                         constraints[a] = x
                                if x<0.15and x>0.05:
                                         forvalidation[a] = x

                print "BEST",currentBestHypothesis
                print "forval",forvalidation
                return forvalidation,currentBestHypothesis
        if(count_iter==20):
                w1=pruning(currentBestHypothesis,correct,a1)
                print w1
                return
                
