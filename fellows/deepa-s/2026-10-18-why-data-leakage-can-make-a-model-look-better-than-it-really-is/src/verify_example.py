answers=[0,1,0,1]
assert sum(a==0 for a in answers)==2
assert sum(a==b for a,b in zip(answers,answers))==4
print("Fictional test: always-zero 2/4; leaked lookup 4/4. Not a generalization estimate.")
