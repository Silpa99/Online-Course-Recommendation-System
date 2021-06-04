import csv
from contentbased_recommender import rec_content 
from collaborative_recommender import rec_collab

loginUser=int(input("Username:"))
rec1=rec_content(loginUser)
rec2=rec_collab(loginUser)
print(rec1)
print(rec2)
print()
hyb_prob={}
course_list={}
with open('courses.csv', 'r') as file:
  course_file = csv.DictReader(file)
  for row in course_file:
    hyb_prob[row['courseId']]=rec1[row['courseId']]*rec2[row['courseId']]
    course_list[row['courseId']]=row['title']
  nonzero_hybrid={}
  for i,j in hyb_prob.items():
    if j!=float(0):
      nonzero_hybrid[i]=j
  sorted_keys=sorted(nonzero_hybrid,key=nonzero_hybrid.get,reverse=True)
  sorted_hyb={}
  for i in sorted_keys:
    sorted_hyb[i]=nonzero_hybrid[i]
  print("Hybrid probability: ",sorted_hyb)
  print("Recommendations: ")
  for x in sorted_keys:
    print(course_list[x])