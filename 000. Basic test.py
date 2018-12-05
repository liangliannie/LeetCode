par = []
def hello(x):
    par.append(x)
    
print(par)
hello(1)
print(par)


neighbors ={0:[4,6],
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[0,3,9],
            6:[0,1,7],
            7:[2,6],
            8:[1,3],
            9:[2,4]}

def listall(start, n, sequence= None):
    if sequence is None:
        sequence = [start]
    if n==1:
        yield sequence
        return
    for nei in neighbors[start]:
        for bar in listall(nei, n-1,sequence+[nei]):
            yield bar
        
for i in listall(0, 2):
    print(i)