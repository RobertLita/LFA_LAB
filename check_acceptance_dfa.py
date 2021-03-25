def check():
    for t in transitions:
        if t[0] not in states or t[2] not in states or t[1] not in sigma:
            return 0
    return 1

def nextState():
    for t in transitions:
        if t[0]==cstate and t[1]==l:
            return t[2]
    return -1

f=open("pictori.in",'r')
date=f.read()
f.close()
states={}
ti=0
sigma=set()
transitions=[]
date=date.split('\n')
for i in range(0,len(date)):
    if 'Sigma' in date[i]:
        j=i+1
        while date[j]!='End':
            date[j]=str(date[j]).strip()
            sigma.add(date[j])
            j+=1
    elif 'States' in date[i]:
        j=i+1
        while date[j]!='End':
            date[j]=str(date[j]).strip()
            date[j]=date[j].split(',')
            for k in range(0,len(date[j])):
                date[j][k]=date[j][k].strip()
            if len(date[j])==3:
                states[date[j][0]]=(date[j][1],date[j][2])
            elif len(date[j])==2:
                states[date[j][0]]=(date[j][1])
            else:
                states[date[j][0]]=()
            j+=1
    elif 'Transitions' in date[i]:
        j=i+1
        while date[j]!='End':
            date[j] = str(date[j]).strip()
            date[j] = date[j].split(',')
            for k in range(0,len(date[j])):
                date[j][k]=date[j][k].strip()
            transitions.append(date[j])
            j+=1
if check()==0:
    print("Transition section has not valid states.")
else:
    print("Transition section has valid states.")
    cstate=''
    for state in states:
        if 'S' in states[state]:
            startstate=state
    w = input("Give a word for DFA: ")
    while w!='0':
        ok=1
        cstate=startstate
        while w and ok==1:
            l=w[0]
            if l not in sigma:
                ok=0
            p=nextState()
            if p==-1:
                ok=0
            cstate=p
            w=w[1:]
        if ok==1 and 'F' not in states[cstate]:
            ok=0
        if ok==1:
            print("Accepted")
        else:
            print("Rejected")
        w = input("Give a word for DFA: ")