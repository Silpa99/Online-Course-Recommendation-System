# -*- coding: utf-8 -*-
"""Collaborative.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jejasGSP-Bj22cABk-B-yttckqJYHlM4

Import Data
"""

import pandas as pd
 
courses = pd.read_csv("/content/Courses.csv")
users = pd.read_csv("/content/Users.csv")
rating = pd.read_csv("/content/Ratings.csv")

uid =  1#@param {type:"integer"}
print(uid)

"""Display Dataset"""

courses.head(15)

users.head(15)

rating.head(9)

"""Data Cleaning"""

courses.dropna(inplace=True)
users.dropna(inplace=True)
rating.dropna(inplace=True)

rating

"""Grouping of Likes and Dislikes from Users"""

u1_likes=[]
  u1_dislikes=[]
  other_likes={}
  other_dislikes={}
  for index, rows in rating.iterrows():
    if (rows.userId == uid):
      if (rows.rating == 1):
        u1_likes.append(rows.courseId.tolist())
      elif (rows.rating == -1):
        u1_dislikes.append(rows.courseId.tolist())
  #print(u1_likes, u1_dislikes)
    else:
      #Grouping of Likes and Dislikes of all Courses given by Users
      if rows.userId not in other_likes.keys():
        other_likes[rows.userId] = []
      if rows.userId not in other_dislikes.keys():
        other_dislikes[rows.userId] = []
      if (rows.rating == 1):
        other_likes[rows.userId].append(rows.courseId.tolist())
      elif (rows.rating == -1):
        other_dislikes[rows.userId].append(rows.courseId.tolist())
  #print(u1_likes,u1_dislikes,other_likes,other_dislikes)

"""Finding the Similarity of Liking with other Users"""

common_likes=[]
  common_dislikes=[]
  opposite_rating1=[]
  opposite_rating2=[]
  similarity={}
  for index,rows in users.iterrows():
    if rows.userId not in other_likes.keys():
      other_likes[rows.userId]=[]
    if rows.userId not in other_dislikes.keys():
      other_dislikes[rows.userId]=[]
    if (rows.userId == uid):
      continue
    else:
      common_likes=list(set(u1_likes).intersection(set(other_likes[rows.userId])))
      common_dislikes=list(set(u1_dislikes).intersection(set(other_dislikes[rows.userId])))
      opposite_rating1=list(set(u1_likes).intersection(set(other_dislikes[rows.userId])))
      opposite_rating2=list(set(u1_dislikes).intersection(set(other_likes[rows.userId])))
      lst=[u1_likes,u1_dislikes,other_likes[rows.userId],other_dislikes[rows.userId]]
      total=list(set().union(*lst))
      #print(common_likes,common_dislikes,opposite_rating1,opposite_rating2,total)

      if len(total)!=0:
        similarity[rows.userId]=(len(common_likes)+len(common_dislikes)-len(opposite_rating1)-len(opposite_rating2))/len(total)
      else:
        similarity[rows.userId]=0
  print()
  print("Similarity with other users : ",similarity)
  print()

"""Calculates How Many Likes and Dislikes the Courses have in Total From the Users"""

course_likes={}
  course_dislikes={}
  for index, rows in rating.iterrows():
    if rows.courseId not in course_likes.keys():
      course_likes[rows.courseId]=[]
    if rows.courseId not in course_dislikes.keys():
      course_dislikes[rows.courseId]=[]
    if (rows.rating == 1):
      course_likes[rows.courseId].append(rows.userId.tolist())
    if (rows.rating == -1):
      course_dislikes[rows.courseId].append(rows.userId.tolist())
  print(" Course Likes : ",course_likes,'\n',"Course Dislikes : ",course_dislikes)

"""Determination of Probability List and Sorting"""

probability_list={}
  for index,rows in courses.iterrows():
    if rows.courseId not in course_likes.keys():
      course_likes[rows.courseId]=[]
    if rows.courseId not in course_dislikes.keys():
      course_dislikes[rows.courseId]=[]
    similarity_sum_liked=0
    similarity_sum_disliked=0
    for i in course_likes[rows.courseId]:
      if (i==uid):
        continue
      similarity_sum_liked += similarity[i]
    for i in course_dislikes[rows.courseId]:
      if (i==uid):
        continue
      similarity_sum_disliked += similarity[i]
    liked_users=len(course_likes[rows.courseId])
    disliked_users=len(course_dislikes[rows.courseId])
    if (liked_users+disliked_users) != 0:
      prob_to_like=(similarity_sum_liked-similarity_sum_disliked)/(liked_users+disliked_users)
    else:
      prob_to_like=0
    probability_list[rows.courseId]=prob_to_like
print()
print("Probability list:")
print(probability_list)
print()
sorted_probability=sorted(probability_list,key=probability_list.get,reverse=True)
print("Sorted probability:")
print(sorted_probability)
print()

"""Recommendations"""

#Determining the recommendations by taking into account those probabilities which are Non-zero
nonzero={}
for i,j in probability_list.items():
  if j!=float(0):
    nonzero[i]=j
sorted_nonzero=sorted(nonzero,key=nonzero.get,reverse=True)
print("Recommendations:")
print()
for i in range(len(sorted_nonzero)):
  print(courses.title[sorted_nonzero[i] - 1])