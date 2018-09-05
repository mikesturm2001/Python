
# coding: utf-8

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:


7 ** 4


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[2]:


s = "Hi there Sam!"


# In[3]:


wordList = s.split()
print(wordList)


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[6]:


planet = "Earth"
diameter = 12742


# In[8]:


string = "The diameter of {} is {} kilometers"
print (string.format(planet, diameter))


# ** Given this nested list, use indexing to grab the word "hello" **

# In[11]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[12]:


lst[3][1][2]


# ** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[14]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[15]:


d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# In[10]:


# Comment your answer here: a tuple is immutable while a list can be modified (mutable)


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[17]:


def domainGet(domain):
    domain = domain.split('@')
    return domain[1]


# In[19]:


domain = domainGet('user@domain.com')
print(domain)


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[20]:


def findDog(string):
    if "dog" in string.lower():
        return True
    else:
        return False


# In[25]:


findDog('Is there a dog! here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[27]:


def countDog(string):
    dogCount = 0
    wordList = string.split()
    for word in wordList:
        if word.lower() == "dog":
            dogCount = dogCount + 1;
    return dogCount


# In[29]:


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[30]:


seq = ['soup','dog','salad','cat','great']


# In[31]:


for word in filter(lambda x: x[0].lower() == 's', seq):
    print(word)


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[32]:


def caught_speeding(speed, is_birthday):
    if is_birthday or speed <= 60:
        return "No ticket"
    elif speed <= 80:
        return "Small Ticket"
    else:
        return "Big Ticket"
    pass


# In[36]:


caught_speeding(81,True)


# In[34]:


caught_speeding(81,False)

