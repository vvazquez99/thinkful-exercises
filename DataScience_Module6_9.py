#!/usr/bin/env python
# coding: utf-8

# # Module 6.9 Working with numbers

# ### 1) Romer temperature

# Instructions from Codewars.com:
# 
# You're writing an excruciatingly detailed alternate history novel set in a world where Daniel Gabriel Fahrenheit was never born.
# 
# Since Fahrenheit never lived the world kept on using the Rømer scale, invented by fellow Dane Ole Rømer to this very day, skipping over the Fahrenheit and Celsius scales entirely.
# 
# Your magnum opus contains several thousand references to temperature, but those temperatures are all currently in degrees Celsius. You don't want to convert everything by hand, so you've decided to write a function, celsius_to_romer() that takes a temperature in degrees Celsius and returns the equivalent temperature in degrees Rømer.

# In[1]:


def celsius_to_romer(celsius):
    return celsius * (21/40) + 7.5


# ### 2) Pixelart planning

# Instructions from Codewars.com:
# 
# You're laying out a rad pixel art mural to paint on your living room wall in homage to Paul Robertson, your favorite pixel artist.
# 
# You want your work to be perfect down to the millimeter. You haven't decided on the dimensions of your piece, how large you want your pixels to be, or which wall you want to use. You just know that you want to fit an exact number of pixels.
# 
# To help decide those things you've decided to write a function, is_divisible() that will tell you whether a wall of a certain length can exactly fit an integer number of pixels of a certain length.
# 
# Your function should take two arguments: the size of the wall in millimeters and the size of a pixel in millimeters. It should return True if you can fit an exact number of pixels on the wall, otherwise it should return False. For example is_divisible(4050, 27) should return True, but is_divisible(4066, 27) should return False.

# In[3]:


def is_divisible(wall_length, pixel_size):
    return wall_length % pixel_size == 0


# ### 3) Blue and red marbles

# Instructions from Codewars.com:
# 
# You and a friend have decided to play a game to drill your statistical intuitions. The game works like this:
# 
# You have a bunch of red and blue marbles. To start the game you grab a handful of marbles of each color and put them into the bag, keeping track of how many of each color go in. You take turns reaching into the bag, guessing a color, and then pulling one marble out. You get a point if you guessed correctly. The trick is you only have three seconds to make your guess, so you have to think quickly.
# 
# You've decided to write a function, guessBlue() to help automatically calculate whether you should guess "blue" or "red". The function should take four arguments:
# 
#     the number of blue marbles you put in the bag to start
#     the number of red marbles you put in the bag to start
#     the number of blue marbles pulled out so far, and
#     the number of red marbles pulled out so far.
# 
# guessBlue() should return the probability of drawing a blue marble, expressed as a float. For example, guessBlue(5, 5, 2, 3) should return 0.6.
# 

# In[4]:


def guess_blue(blue_start,red_start,blue_pulled,red_pulled):
    return((blue_start - blue_pulled)/((red_start - red_pulled) + (blue_start - blue_pulled)))


# ### 4) Congo pizza

# Instructions from Codewars.com:
# 
# Your company, Congo Pizza, is the second-largest online frozen pizza retailer. You own a number of international warehouses that you use to store your frozen pizzas, and you need to figure out how many crates of pizzas you can store at each location.
# 
# Congo recently standardized its storage containers: all pizzas fit inside a cubic crate, 16-inchs on a side. The crates are super tough so you can stack them as high as you want.
# 
# Write a function box_capacity() that figures out how many crates you can store in a given warehouse. The function should take three arguments: the length, width, and height of your warehouse (in feet) and should return an integer representing the number of boxes you can store in that space.
# 
# For example: a warehouse 32 feet long, 64 feet wide, and 16 feet high can hold 13,824 boxes because you can fit 24 boxes across, 48 boxes deep, and 12 boxes high, so box_capacity(32, 64, 16) should return 13824.

# In[7]:


def box_capacity(length, width, height):
    length_capacity = length // (16 / 12)
    width_capacity = width // (16 / 12)
    height_capacity = height // (16/12)
    return length_capacity * width_capacity * height_capacity


# ### 5) Quadratic formula

# Instructions from Codewards.com:
# 
# Remember all those quadratic equations you had to solve by hand in highschool? Well, no more! You're going to solve all the quadratic equations you might ever[1] have to wrangle with in the future once and for all by coding up the quadratic formula to handle them automatically.
# 
# Write a function quadratic_formula() that takes three arguments, a, b, and c that represent the coefficients in a formula of the form ax^2 + bx + c = 0. Your function shoud return a list with two elements where each element is one of the two roots. If the formula produces a double root the result should be a list where both elements are that value.
# 
# For example, quadratic_formula(2, 16, 1) should return the list [-0.06299606299409444, -7.937003937005906]. The order of the roots is not important.
# 
# [1] Well, not ever ever. You don't need to worry about getting quadratic equations with complex roots where you need the square root of a negative number. All the test cases will be for equations with real roots.
# 

# In[13]:


def quadratic_formula(a, b, c):
    root_of_square = ((b ** 2) - 4 * a * c) ** .5
    root1 = (-b + root_of_square) / (2 * a)
    root2 = (-b - root_of_square) / (2 * a)
    return [root1, root2]

