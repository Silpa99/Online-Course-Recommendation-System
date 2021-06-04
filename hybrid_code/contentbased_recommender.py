import csv 

def rec_content(loginUser):
  with open('users.csv', 'r') as file:
    user_file = csv.DictReader(file)
    for row in user_file:
        #print(dict(row))
        if row['username']==str(loginUser):
          user_prefs=row['field_of_interest'].split("|")
          break
    print("user preferences = ",user_prefs)
    print()

  prob_list={}
  with open('courses.csv', 'r') as file:
    course_file = csv.DictReader(file)
    for row in course_file:
    #print(dict(row))
      course_catg=row['category'].split("|")
      #print(course_catg)
      pref_course=list(set(user_prefs).intersection(set(course_catg)))
      prob=len(pref_course)/len(course_catg)
      prob_list[row['courseId']]=prob
    #print("probability list = ",prob_list)
    #print()
    sorted_prob=sorted(prob_list,key=prob_list.get,reverse=True)
    #print(sorted_prob)
  #recommend first 2 courses
    #print("Recommendations:")
    #for i in range(2):
      #print(sorted_prob[i])
  return prob_list