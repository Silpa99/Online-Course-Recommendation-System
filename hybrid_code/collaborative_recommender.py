import csv

def rec_collab(loginUser):
  with open('ratings.csv', 'r') as file:
    ratings_file = csv.DictReader(file)
    u1_likes=[]
    u1_dislikes=[]
    other_likes={}
    other_dislikes={}
    for row in ratings_file:
      #print(dict(row))
      if row['username']== str(loginUser):
        if row['rating']=='1':
          u1_likes.append(row['courseId'])
        elif row['rating']=='-1':
          u1_dislikes.append(row['courseId'])
    #print(u1_likes,u1_dislikes)
      else:
        if row['username'] not in other_likes.keys():
          other_likes[row['username']]=[]
        if row['username'] not in other_dislikes.keys():
          other_dislikes[row['username']]=[]
        if row['rating']=='1':
          other_likes[row['username']].append(row['courseId'])
        elif row['rating']=='-1':
          other_dislikes[row['username']].append(row['courseId'])
    #print(u1_likes,u1_dislikes,other_likes,other_dislikes)
  with open('users.csv', 'r') as file:
    users_file = csv.DictReader(file)
    common_likes=[]
    common_dislikes=[]
    opposite_rating1=[]
    opposite_rating2=[]
    similarity={}
    for row in users_file:
      if row['username'] not in other_likes.keys():
        other_likes[row['username']]=[]
      if row['username'] not in other_dislikes.keys():
        other_dislikes[row['username']]=[]
      if row['username']==str(loginUser):
        #similarity[row['username']]=0
        continue
      else:
        common_likes=list(set(u1_likes).intersection(set(other_likes[row['username']])))
        common_dislikes=list(set(u1_dislikes).intersection(set(other_dislikes[row['username']])))
        opposite_rating1=list(set(u1_likes).intersection(set(other_dislikes[row['username']])))
        opposite_rating2=list(set(u1_dislikes).intersection(set(other_likes[row['username']])))
        lst=[u1_likes,u1_dislikes,other_likes[row['username']],other_dislikes[row['username']]]
        total=list(set().union(*lst))
        #print(common_likes,common_dislikes,opposite_rating1,opposite_rating2,total)
        if len(total)!=0:
          similarity[row['username']]=(len(common_likes)+len(common_dislikes)-len(opposite_rating1)-len(opposite_rating2))/len(total)
        else:
          similarity[row['username']]=0
    #print()
    #print("Similarity with other users : ",similarity)
    #print()
  with open('ratings.csv', 'r') as file:
    ratings_file = csv.DictReader(file)
    course_likes={}
    course_dislikes={}
    for row in ratings_file:
      if row['courseId'] not in course_likes.keys():
        course_likes[row['courseId']]=[]
      if row['courseId'] not in course_dislikes.keys():
        course_dislikes[row['courseId']]=[]
      if row['rating']=='1':
        course_likes[row['courseId']].append(row['username'])
      if row['rating']=='-1':
        course_dislikes[row['courseId']].append(row['username'])
    #print("course likes : ",course_likes,'\n',"course dislikes : ",course_dislikes)
  with open('courses.csv','r') as file:
    course_file=csv.DictReader(file)
    probability_list={}
    for row in course_file:
      if row['courseId'] not in course_likes.keys():
        course_likes[row['courseId']]=[]
      if row['courseId'] not in course_dislikes.keys():
        course_dislikes[row['courseId']]=[]
      similarity_sum_liked=0
      similarity_sum_disliked=0
      for i in course_likes[row['courseId']]:
        if i==str(loginUser):
          continue
        similarity_sum_liked+=similarity[i]
      for i in course_dislikes[row['courseId']]:
        if i==str(loginUser):
          continue
        similarity_sum_disliked+=similarity[i]
      liked_users=len(course_likes[row['courseId']])
      disliked_users=len(course_dislikes[row['courseId']])
      if (liked_users+disliked_users)!=0:
        prob_to_like=(similarity_sum_liked+similarity_sum_disliked)/(liked_users+disliked_users)
      else:
        prob_to_like=0
      probability_list[row['courseId']]=prob_to_like
  #print()
  #print("Probability list:")
  #print(probability_list)
  #print()
  #sorted_probability=sorted(probability_list,key=probability_list.get,reverse=True)
  #print("Sorted probability:")
  #print(sorted_probability)
  #print()
  #recommend first 2 courses
  '''print("Recommendations:")
  for i in range(2):
    print(sorted_probability[i])'''
  nonzero={}
  for i,j in probability_list.items():
    if j!=float(0):
      nonzero[i]=j
  #sorted_nonzero=sorted(nonzero,key=nonzero.get,reverse=True)
  #print("Sorted non-zero probability list:")
  #print()
  #print(sorted_nonzero)
  return probability_list