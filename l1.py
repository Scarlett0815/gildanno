#!usr/bin/python3
filename="l1.txt"
width=20
sign="*"
fo1=open(filename,"r")
i=0
line=[]
n=[]
length=[]
done=0
while not done:
    line.append(fo1.readline())
    length.append(len(line[i]))         
    n.append((width-length[i])//2)
    i=i+1
    if(line[i-1]==""):
        done=1
fo2=open(filename,'w')
m=0
while m<i-1:
    for j in range(n[m]):
        v=fo2.write(sign)
    for p in range(length[m]-1):
        v=fo2.write(line[m][p])
    for k in range(width-length[m]-n[m]):
        v=fo2.write(sign)
    v=fo2.write("\n")
    m=m+1
fo1.close()
fo2.close()
