sparshva=[]
times=int(input("Enter the number of elements in the lists:-"))
i=1
for i in range(i,times+1):
    sparshva.append(int(input("Enter the element:-")))
max=sparshva[0]
max_index=0
for num in sparshva:
    if num>max:
        max_index=i
        max=num
     
print("The largest eleement in the list is:-",max)
print("Index:-",i)