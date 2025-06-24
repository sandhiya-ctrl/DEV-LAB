import matplotlib.pyplot as plt
#x=[2,4,6,8]
#y=[1,5,7,11]
#plt.plot(x,y)
#plt.show()

students=["san","rags","roh","nith","niv","pos","ragh"]
scores=[98,98,97,94,98,97,95]
plt.bar(students,scores,color='skyblue')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.title('Student Exam Scores')
plt.show()

