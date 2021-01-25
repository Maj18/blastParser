#!/opt/anaconda3/envs/cluster/bin/python
import sys

if len(sys.argv)!=3:
    print("\n\n")
    print("ERROR! Please run the program as follows: python3 blastParser.py yeast_vs_Paxillus.blastp Q9.out")
    print("\n\n")

pre = [] 
with open (sys.argv[1], "r") as fin:
    for line in fin:  
        line=line.rstrip()
        if ("Query=" in line):
            Query = line.split()[1]
            t=0
        #print(Query)
        if "*****" in line:
                t=1
                target = " "
                score = " "
                evalue = " "
                ident = " "
                pre.append([Query, target, evalue, ident, score])
        
        elif (line.startswith(">")) and (t == 0) and Query!=line.split()[1]:
                target = line.split()[1]
                t=2
        elif (line.startswith(" Score")) and (t==2):
                score = line.split()[2]
                evalue = line.split()[7]
        elif (line.startswith(" Identities")) and (t==2): 
                ident = line.split()[3][0:-2][1:]
                pre.append([Query, target, evalue, ident, score])
        elif ("Query=" in line) and t==0: 
                target = " "
                score = " "
                evalue = " "
                ident = " "
                pre.append([Query, target, evalue, ident, score])


with open (sys.argv[2], "w") as fout:
    print("#query", "target", "e-value", "identity(%)", "score", sep="\t", file=fout)
    for i in pre:
        print(i[0], i[1], i[2], i[3], i[4], sep="\t", file=fout)

         
    
    
