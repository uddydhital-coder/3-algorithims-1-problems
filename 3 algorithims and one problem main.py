#01-three-algorithms.py
#Topic: Algorithms- three ways to solve the same problem (Formula, Loop, Double Loop)
#Same answer everytime, but the number of steps is different

#4 students in a contest: student 1 earns 1pt, student 2 earns 2 points, student 3 earns 3pts, student 4 earns 4pts

n=4

guess= input("Formula: one calculation. Press Enter to run")

input("Formula: one calculation. Press enter to run")
total= n * (n+1) //2
print("    toal=", total,"  steps=1")

input("Loops: adds one student at a time. Press Enter to run")
total=0
for student in range(1, n+1):
    total +=student
print(" total=", total,"  steps=", n)

input("Double Loop: counts every single point. Press Enter to run" )
total=0
steps=0
for student in range(1,n+1):
    for point in range(1, student +1):
        total +=1
        steps +=1
print(". total=", total, "   steps=" steps, "  your guess was:" guess)
  
   
