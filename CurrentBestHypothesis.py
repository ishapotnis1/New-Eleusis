from new_eleusis import *
import scientist
count=0

cb={}

constraints={}
currentBestHypothesis={}
forvalidation={}
threshold=0.0

def pruning(hypothesis,correct):
        k=hypothesis
        w=len(k)
        h=k.keys()
        h1=[]
        h2=[]
        h3=[]
        #print k[h[0]][0]
        for x in k[h[0]]:#pruning is_color
                #print x
                if x not  in h1:
                        h1.append(x)
        for x in k[h[1]]:#pruning is_value
                #print x
                if x not  in h2:
                        h2.append(x)
        for x in k[h[2]]:#pruning is_suit
                #print x
                if x not  in h3:
                        h3.append(x)            
        hypo=h1+h2+h3
        #return hypo
        #print hypo
        print "correct list"
        print correct
        f=[]
        q=[]
        for i in range(0,len(correct)):
                c=extraction(correct[i])
                print correct
                #print c
                d=c.keys()
                for i in range(0,len(d)):
                        for j in range(0,len(hypo)):
                                if(d[i]==hypo[j]):
                                        if(c[d[i]]==1):
                                                f.append(d[i])
        final1=[]
        c1=extraction(correct[0])
        c2=extraction(correct[1])
        c3=extraction(correct[2])
        #print "d3"
        d3=comparator(c1,c2,c3)
        #print d3
        i=3
        while(i<len(correct)):
                d2=comparator(c1,c2,c3)
                #print c1
                d1=d2.keys()
                #print d2
                #print d2
                for i1 in range(0,len(d1)):
                        for j in range(0,len(hypo)):
                                if(d1[i1]==hypo[j]):
                                        if(d2[d1[i1]]==1):
                                                q.append(d1[i1])
                                                #print q
                #final1=[]+1
                c2=c1
                c3=c2
                c1=extraction(correct[i])
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
        best=final+final1
        return best

def current_best_hypothesis(hypothesis,flag,correct):
        temp={}
	tempconstraints={}
	tempValidation={}
	if flag==20:
                w=pruning(currentBestHypothesis,correct)
                print w
                return
        else:
                for field, possible_values in hypothesis.iteritems():
                        print  "whatis",field , possible_values
                        for a,x in possible_values.iteritems():
                                if x>0.005:
                                         currentBestHypothesis[a] = x
                                if x<0.002:
                                         constraints[a] = x
                                if x<0.005 and x>0.002:
                                         forvalidation[a] = x

                print "thisis",currentBestHypothesis
                return forvalidation,currentBestHypothesis
