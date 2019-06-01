#!/usr/bin/env python
# coding: utf-8

# # Module 6.10 Logic, control flow, and conditionals

# ### 1) Traffic light

# Instructions from Codewars.com:
# 
# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.
# 
# Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.
# 
# For example, update_light('green') should return 'yellow'.

# In[2]:


def update_light(current):
    if current ==  'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    elif current == 'red':
        return 'green'
    else:
        return "{} is not a traffic light color.".format(current)


# ### 2) Umbrella decider

# Instructions from Codewars.com:
# 
# Write a function take_umbrella() that takes two arguments: a string representing the current weather and a float representing the chance of rain today.
# 
# Your function should return True or False based on the following criteria.
# 
#     You should take an umbrella if it's currently raining or if it's cloudy and the chance of rain is over 0.20.
#     You shouldn't take an umbrella if it's sunny unless it's more likely to rain than not.
# 
# The options for the current weather are sunny, cloudy, and rainy.
# 
# For example, take_umbrella('sunny', 0.40) should return False.

# In[3]:


def take_umbrella(weather, rain_chance):
    return bool((weather == 'rainy') or (weather == 'cloudy' and rain_chance > 0.20) or (weather == 'sunny' and rain_chance > 0.50))


# ### 3) Graceful addition

# Instructions from Codewar.com:
# 
# You like the way the Python + operator easily handles adding different numeric types, but you need a tool to do that kind of addition without killing your program with a TypeError exception whenever you accidentally try adding incompatible types like strings and lists to numbers.
# 
# You decide to write a function my_add() that takes two arguments. If the arguments can be added together it returns the sum. If adding the arguments together would raise an error the function should return None instead.
# 
# For example, my_add(1, 3.414) would return 4.414, but my_add(42, " is the answer.") would return None.
# 
# Hint: using a try / except statement may simplify this kata.

# In[ ]:


def my_add(a, b):
    try:
        return a + b
    except TypeError:
        return None


# ### 4) Red and bumpy

# You're playing a game with a friend involving a bag of marbles. In the bag are ten marbles:
# 
#     1 smooth red marble
#     4 bumpy red marbles
#     2 bumpy yellow marbles
#     1 smooth yellow marble
#     1 bumpy green marble
#     1 smooth green marble
# 
# You can see that the probability of picking a smooth red marble from the bag is 1 / 10 or 0.10 and the probability of picking a bumpy yellow marble is 2 / 10 or 0.20.
# 
# The game works like this: your friend puts her hand in the bag, chooses a marble (without looking at it) and tells you whether it's bumpy or smooth. Then you have to guess which color it is before she pulls it out and reveals whether you're correct or not.
# 
# You know that the information about whether the marble is bumpy or smooth changes the probability of what color it is, and you want some help with your guesses.
# 
# Write a function color_probability() that takes two arguments: a color ('red', 'yellow', or 'green') and a texture ('bumpy' or 'smooth') and returns the probability as a decimal fraction accurate to two places.
# 
# The probability should be a string and should discard any digits after the 100ths place. For example, 2 / 3 or 0.6666666666666666 would become the string '0.66'. Note this is different from rounding.
# 
# As a complete example, color_probability('red', 'bumpy') should return the string '0.57'.
# 

# In[ ]:


def color_probability(color, texture):
    if color == 'green':
        if texture == 'bumpy':
            result = 1 / 7
        else:
            result = 1 / 3
    elif color == 'yellow':
        if texture == 'bumpy':
            result = 2 / 7
        else:
            result = 1 / 3
    else:
        if texture == 'bumpy':
            result = 4 / 7
        else:
            result = 1 / 3
    return str(result)[:4]


#   ### 5) Hacking p-hackers

# As a member of the editorial board of the prestigous scientific Journal Proceedings of the National Academy of Sciences, you've decided to go back and review how well old articles you've published stand up to modern publication best practices. Specifically, you'd like to re-evaluate old findings in light of recent literature about "researcher degrees of freedom".
# 
# You want to categorize all the old articles into three groups: "Fine", "Needs review" and "Pants on fire".
# 
# In order to categorize them you've enlisted an army of unpaid grad students to review and give you two data points from each study: (1) the p-value behind the paper's primary conclusions, and (2) the number of recommended author requirements to limit researcher degrees of freedom the authors satisfied:
# 
# * Authors must decide the rule for terminating data collection before data collection begins and report this rule in the article.
# * Authors must collect at least 20 observations per cell or else provide a compelling cost-of-data-collection justification. 
# * Authors must list all variables collected in a study.
# * Authors must report all experimental conditions, including failed manipulations.
# * If observations are eliminated, authors must also report what the statistical results are if those observations are included.
# * If an analysis includes a covariate, authors must report the statistical results of the analysis without the covariate.
# 
# Your army of tenure-hungry grad students will give you the p-value as a float between 1.0 and 0.0 exclusive, and the number of author requirements satisfied as an integer from 0 through 6 inclusive.
# 
# You've decided to write a function, categorize_study() to automatically categorize each study based on these two inputs using the completely scientifically legitimate "bs-factor". The bs-factor for a particular paper is calculated as follows:
# 
#     bs-factor when the authors satisfy all six requirements is 1
#     bs-factor when the authors satisfy only five requirements is 2
#     bs-factor when the authors satisfy only four requirements is 4
#     bs-factor when the authors satisfy only three requirements is 8...
# 
# Your function should multiply the p-value by the bs-factor and use that product to return one of the following strings:
# 
#     product is less than 0.05: "Fine"
#     product is 0.05 to 0.15: "Needs review"
#     product is 0.15 or higher: "Pants on fire"
# 
# You've also decided that all studies meeting none of the author requirements that would have been categorized as "Fine" should instead be categorized as "Needs review".

# In[4]:


def categorize_study(p_value, requirements):
    bs_factor = 2 ** (6 - requirements)
    product = p_value * bs_factor
    
    if product < 0.05:
        result = "Fine"
    elif product < 0.15:
        result = "Needs review"
    else:
        result = "Pants on fire"
    
    if requirements == 0 and result == "Fine":
        result = "Needs review" 
    return result

