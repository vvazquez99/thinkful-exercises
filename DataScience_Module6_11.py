#!/usr/bin/env python
# coding: utf-8

# # Module 6.11 Lists, loops, and iterations

# ### 1) Longest word

# Instructions from Codewars.com:
# 
# Complete the function that takes one argument, a list of words, and returns the length of the longest word in the list.

# In[2]:


def longest(words):
    result = 0
    for word in words:
        if len(word) > result:
            result = len(word)
    return result


# Instructions from Codewars.com:
# 
# You're a statistics professor and the deadline for submitting your students' grades is tonight at midnight. Each student's grade is determined by their mean score across all of the tests they took this semester.
# 
# You've decided to automate grade calculation by writing a function calculate_grade() that takes a list of test scores as an argument and returns a one character string representing the student's grade calculated as follows:
# 
#     90% <= mean score <= 100%: "A",
#     80% <= mean score < 90%: "B",
#     70% <= mean score < 80%: "C",
#     60% <= mean score < 70%: "D",
#     mean score < 60%: "F"
# 
# For example, calculate_grade([92, 94, 99]) would return "A" since the mean score is 95, and calculate_grade([50, 60, 70, 80, 90]) would return "C" since the mean score is 70.
# 
# Your function should handle an input list of any length greater than zero.
# 

# In[3]:


def calculate_grade(grades):
    sum_grades = 0
    for grade in grades:
        sum_grades += grade
    final_grade = sum_grades / len(grades)
    if final_grade >= 90:
        return 'A'
    elif final_grade >= 80:
        return 'B'
    elif final_grade >= 70:
        return 'C'
    elif final_grade >= 60:
        return 'D'
    else:
        return 'F'


# ### 3) Lists of lists

# Instructions from Codewars.com:
# 
# Each sub-list contains two items, and each item in the sub-lists is an integer.
# 
# Write a function process_data() that processes each sub-list like so:
# 
#     [2, 5] --> 2 - 5 --> -3
#     [3, 4] --> 3 - 4 --> -1
#     [8, 7] --> 8 - 7 --> 1
# 
# and then returns the product of all the processed sub-lists: -3 * -1 * 1 --> 3.
# 
# For input, you can trust that neither the main list nor the sublists will be empty.

# In[4]:


def process_data(data):
    product = 1
    for datum in data:
        difference = datum[0] - datum[1]
        print(difference)
        product = product * difference        
    return product


# ### 4) Inverse slicer

# Instructions from Codewars.com:
# 
# Write a function inverse_slice() that takes three arguments: a list items, an integer a and an integer b. The function should return a new list with the slice specified by items[a:b] excluded. For example:

# In[5]:


def inverse_slice(items,a,b):
    del items[a:b]
    return items

