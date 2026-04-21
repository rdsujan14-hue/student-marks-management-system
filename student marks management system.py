s={}
n=int(input("enter no of students:"))
for i in range(n):
    name=input(f"enter name of student {i}:")
    marks=[]
    for j in range(3):
        m=int(input("enter marks:"))
        marks.append(m)
    s[name]=marks
for name, marks in s.items():
    total=sum(marks)
    avrg=total/3

    print("name:",name)
    print("marks:",marks)
    print("total:",total)
    print("average:",avrg)
highest=0
topper=""
for name,marks in s.items():
    total=sum(marks)
    if total > highest :
        highest= total
        topper=name
print("topper is:",topper,"by total marks:",highest)


