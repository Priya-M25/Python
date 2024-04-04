''' OUTPUT :-
Move disk 1 from A to B
Move disk 2 from A to C
Move disk 1 from B to C
Move disk 3 from A to B
Move disk 1 from C to A
Move disk 2 from C to B
Move disk 1 from A to B
Move disk 4 from A to C
Move disk 1 from B to C
Move disk 2 from B to A
Move disk 1 from C to A
Move disk 3 from B to C
Move disk 1 from A to B
Move disk 2 from A to C
Move disk 1 from B to C

'''

def towerOfHanoi(n,source,target,auxiliary):
    if(n==1):
        print(f"Move disk {n} from {source} to {target}")
        return
    towerOfHanoi(n-1,source,auxiliary,target) 
    print(f"Move disk {n} from {source} to {target}")
    towerOfHanoi(n-1,auxiliary,target,source) 
n=4
towerOfHanoi(n,'A','C', 'B')
