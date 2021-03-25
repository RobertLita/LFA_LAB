def create_table1():
    for s in states:
        for l in sigma:
            table1[(s,l)]=[]
    for t in transitions:
        table1[(t[0],t[2])].append(t[1]);

def create_table2():
    new_states=[init]
    i=0
    while i<len(new_states):
        x=new_states[i]
        if x!='':
            table2[x]=[]
        for l in sigma:
            intersection=set()
            for p in x:
                for y in table1[p,l]:
                    intersection.add(y)
            z="".join(sorted(list(intersection)))
            if len(z)>0:
                table2[x].append(z)
                if z not in new_states:
                    new_states.append(z)
        i+=1

def afisare():
    print("NFA-ul a fost transformat in urmatorul DFA:\nSigma: ", end='')
    print(*sigma)
    print("Starea initiala: 1")
    print("Starile finale: ", end='')
    for state in states_dfa:
        if "F" in states_dfa[state]:
            print(state, end=' ')
    print("\nTranzitiile sunt: ")
    print(*transitions_dfa, sep=' ')

if __name__ == "__main__":
    file=input("Fisier de intrare: ")
    f=open(file,'r')
    date=f.read()
    f.close()
    states={}
    sigma=[]
    transitions=[]
    table1={}
    table2={}
    date=date.splitlines()
    for litera in date[0].split(' '):
        sigma.append(litera)
    for litera in date[1].split(' '):
        states[litera]=[]
    states[date[2]].append("I")
    init=date[2]
    for litera in date[3].split(' '):
        states[litera].append("F")
    for i in range(4,len(date)):
        transition=date[i].split(" ")
        transitions.append((transition[0],transition[1],transition[2]))
    create_table1()
    create_table2()
    states_dfa={}
    transitions_dfa=[]
    aka_states={}
    i=1
    for state in table2:
        aka_states[state]=i
        states_dfa[i]= []
        if state==init:
            states_dfa[i].append("I")
            init_dfa=state
        for l in state:
            if 'F' in states[l]:
                states_dfa[i].append("F")
                break
        i+=1
    for transition,to in table2.items():
        for i in range(0,len(to)):
            transitions_dfa.append((aka_states[transition],aka_states[to[i]],sigma[i]))
    afisare()