#!/usr/bin/env python
# coding: utf-8

# # Module 6.8 Working with strings

# ### 1) Hello world

# Instructions from Codewars.com:
# 
# Complete the function body for this hello() function so that it takes one argument (person, a string) and returns a string saying hello to that person.

# In[12]:


def hello(name):
    return 'Hello, ' + name


# ### 2) Quotable

# Instructions from Codewars.com:
# 
# This function should take two string parameters: a person's name (name) and a quote of theirs (quote), and return a string attributing the quote to the person in the following format:
# 
# '[name] said: "[quote]"'

# In[13]:


def quotable(name, quote):
    return name +' said, ' + quote


# ### 3) Repeater

# Instructions from Codewars.com:
# 
# Write a function named repeater() that takes two arguments (a string and a number), and returns a new string where the input string is repeated that many times.

# In[19]:


def repeater(string, n):
    return string*n


# ### 4) Repeater, level 2

# Instructions from Codewars.com:
# 
# This challenge extends the previous repeater() challenge. Just like last time, your job is to write a function that accepts a string and a number as arguments. This time, however, you should format the string you return like this:
# 
# repeater('yo', 3)
# '"yo" repeated 3 times is: "yoyoyo"'
# repeater('WuB', 6)
# '"WuB" repeated 6 times is: "WuBWuBWuBWuBWuBWuB"'

# In[17]:


def repeater(string, n):
    return '"' + string + '"' + ' repeated ' + str(n) + ' times is: ' + '"' + string*n + '"'


# ### OR

# In[20]:


def repeater(string, n):
    repeated = string * n
    template = '"{}" repeated {} times is: "{}"'
    return template.format(string, n, repeated)


# ### 5) Jedi name

# Instructions from Codewars.com:
# 
# You just took a contract with the Jedi council. They need you to write a function, greet_jedi(), which takes two arguments (a first name and a last name), works out the corresponding Jedi name, and returns a string greeting the Jedi. A person's Jedi name is the first three letters of their last name followed by the first two letters of their first name.

# In[14]:


def greet_jedi(first,last):
    first_2 = first[0:2]
    last_3 = last[0:3]
    template = 'Greetings, master {}{}'
    return template.format(last_3.capitalize(),first_2.capitalize())


# ### 6) Area code extractor

# Instructions from Codewars.com:
# 
# You've got a bunch of textual data with embedded phone numbers. Write a function area_code() that finds and returns just the area code portion of the phone number. The returned area code should be a string, not a number. Every phone number is formatted like in the example, and the only non-alphanumeric characters in the string are apostrophes ' or the punctuation used in the phone number.

# In[21]:


def area_code(text):
    start = text.find('(') + 1
    end = text.find(')')
    return text[start : end]


# ### 7) Poem formatter

# Instructions from Codewars.com:
# 
# Write a function, format_poem() that takes a string like the one line example as an argument and returns a new string that is formatted across multiple lines with each new sentence starting on a new line when you print it out.
# 
# Try to solve this challenge with the str.split() and the str.join() string methods.
# 
# Every sentence will end with a period, and every new sentence will have one space before the previous period. Be careful about trailing whitespace in your solution.

# In[16]:


def format_poem(poem):
    sentences = poem.split('. ')
    result = '.\n'.join(sentences)
    return result

