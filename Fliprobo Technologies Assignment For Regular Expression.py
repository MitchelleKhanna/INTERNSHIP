#!/usr/bin/env python
# coding: utf-8

# # Assignment for Regular Expressions
# # Name: Mitchelle Khanna

# Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# Sample Text- 'Python Exercises, PHP exercises.'
# Expected Output: Python:Exercises::PHP:exercises:

# In[6]:


import re

text = 'Python is important to become a Data Scientist, Isnt.'
reg = re.compile('[\s,\.]')
sub = reg.sub(':', text)
print(sub)


# Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
# Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
# Expected output-
# 0      hello world
# 1             test
# 2    four five six
# 

# In[78]:


import re
import pandas as pd
import numpy as np
dictionary={'Summary' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
df=pd.DataFrame(dictionary)
for i in df:
   df['Summary']=df['Summary'].apply(lambda x: re.sub('[,\d+:;.!]|X{5}','',x))
df


# Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

# In[12]:


import re

text = 'Today, continuous learning is a daily reality, and universities are embracing online education to meet this demand. At EduMaster, we\'re dedicated to supporting both educational institutions and businesses by providing a seamless platform. Our Learning Management System (LMS) combines crucial knowledge with practical experience, making education accessible and effective for everyone.'

def find():
    pattern = r'\b\w{4,25}\b'
    reg = re.compile(pattern)
    out = reg.findall(text)
    print(out)

find()


# Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

# In[16]:


import re

text = 'Today, continuous learning is a daily reality, and universities are embracing online education to meet this demand. At EduMaster, we\'re dedicated to supporting both educational institutions and businesses by providing a seamless platform. Our Learning Management System (LMS) combines crucial knowledge with practical experience, making education accessible and effective for everyone.'

def find_3():
    #pat=re.compile(r'(\b\w{3}\b)|(\b\w{4}\b)|(\b\w{5}\b)')
    pat=re.compile(r'\b\w{3,5}\b')
    output=pat.findall(text)
    print(output)

find_3()


# Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# Expected Output:
# example.com
# hr@fliprobo.com
# github.com
# Hello Data Science World
# Data Scientist
# 

# In[17]:


Sample_Text= ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

def rem_par():
    modtext=[]
    
    for i in Sample_Text:
        pat=re.compile('[\(\)\s]')
        new=pat.sub('',i)
        modtext.append(new)
        print(new)
rem_par()


# Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
# Note- Store given sample text in the text file and then to remove the parenthesis area from the text.
# 

# In[19]:


Sample_Text= '"example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"'
com=re.compile('(\(\.\w+\))|(\(\w+ \w+ \w+\))|(\(\w+\))|(\s)')
out=com.sub('',Sample_Text)
print(out)


# Question 7- Write a regular expression in Python to split a string into uppercase letters.
# Sample text: “ImportanceOfRegularExpressionsInPython”
# Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]
# 

# In[21]:


Stext="ImportanceOfRegularExpressionsInPython"
sp=filter(None,re.split(r'(?=[A-Z])',Stext))
print(list(sp))


# Question 8- Create a function in python to insert spaces between words starting with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython
# 

# In[22]:


Text= 'RegularExpression1IsAn2ImportantTopic3InPython'
def cap():
    split=re.sub(r'((?=[0-9]))',' ',Text)
    print(split)
cap() 


# Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython
# 

# In[23]:


Text= 'RegularExpression1IsAn2ImportantTopic3InPython'
def cap():
    split=re.sub(r'((?=[A-Z0-9]))',' ',Text)
    print(split)
cap() 


# In[29]:


import pandas
pandas .__version__


# Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
# Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv
# 

# Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# In[32]:


text=["Hello_world","you+are+awe$ome","ALFA&OMEGA","PEE_KA_boo","123_Mic_check"]
def match_string(m):
    if re.match('^[A-Za-z0-9_]+$',m):
        print(f"Match found [{m}]")
    else:
        print(f"The string [{m}] does not match")
for str in text:  
    match_string(str)


# Question 12- Write a Python program where a string will start with a specific number. 

# In[33]:


text=["1Hello_universe","4I+know+you+are+awe$ome","7ALPHA&GAMA","9DIM_DIM_Chik","123_Hello_World"]
pat=re.compile(r'^[123]')

def num_match(s):
    if re.match(pat,s):
        print(f"Match found [{s}]")
    
    else:
        print(f"[{s}] does not match the pattern")
        
for i in text:
    num_match(i)


# Question 13- Write a Python program to remove leading zeros from an IP address

# In[34]:


l="109.800.001.040"
pat=re.compile('(?<=\.|^ )0+(?=[0-9])')
match=pat.sub('',l)
match


# Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
# Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
# Expected Output- August 15th 1947
# Note- Store given sample text in the text file and then extract the date string asked format.
# 

# In[39]:


import re

with open('sample_text.txt', 'r') as file:
    text = file.read()

pattern = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)\s+\d{4}\b'

date_match = re.search(pattern, text)

if date_match:
    date_string = date_match.group()
    print(date_string)
else:
    print("Date string not found in the text.")


# Question 15- Write a Python program to search some literals strings in a string. 
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
# 

# In[41]:


text = 'The quick brown fox jumps over the lazy dog.'
matches=re.findall('(fox|dog|horse)',text)
matches


# Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'
# 

# In[42]:


text = 'The quick brown fox jumps over the lazy dog.'
pat=re.compile(r'(fox)')
loc=pat.finditer(text)

for match in loc:
    print("Pattern ",match.group()," found at index ",match.start()," : ",match.end())
    


# Question 17- Write a Python program to find the substrings within a string.
# Sample text : 'Python exercises, PHP exercises, C# exercises'
# Pattern : 'exercises'.
# 

# In[43]:


text='Python exercises, PHP exercises, C# exercises'
pat=re.compile('exercises')
loc=pat.finditer(text)

for mat in loc:
    print("The substring '{}' is present at {}:{}".format(mat.group(),mat.start(),mat.end()))


# Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

# In[45]:


text='He has studied hard and studied in such a way that other student could not studied that way the way he studied'
pat=re.compile('studied')
loc=pat.finditer(text)
i=1
for mat in loc:
    print("The no {} occurrence of substring '{}' is present at {}:{}".format(i,mat.group(),mat.start(),mat.end()))
    i=i+1


# Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# In[46]:


datestr="1985-08-13"
def convert():
    sp=re.split('-', datestr)
    sp.reverse()
    revstr='-'.join(sp)
    print(revstr)
convert()


# Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
# Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
# Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']
# 

# In[47]:


Text="01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
def find_D():
    pat=re.compile(r'\b\d+\.\d{1,2}\b')
    sp=pat.findall(Text)
    print(sp)
find_D() 


# Question 21- Write a Python program to separate and print the numbers and their position of a given string

# In[48]:


text= 'MitchelleKhanna1Islearning2anImportantTopic3InPython'
spl=re.split('',text)
mat=re.finditer('\d{1}',text)
for i in mat:
    print("Found {} at {}:{}".format(i.group(),i.start(),i.end()))


# Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
# Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
# Expected Output: 950
# 

# In[49]:


text='My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
pat=re.compile('\d+')
match=pat.findall(text)
print(max(match))


# Question 23- Create a function in python to insert spaces between words starting with capital letters.
# Sample Text: “RegularExpressionIsAnImportantTopicInPython"
# Expected Output: Regular Expression Is An Important Topic In Python
# 

# In[60]:


def insert_spaces(text):
    result = re.sub(r'(?<!^)([A-Z][a-z])', r' \1', text)  # Insert space before each word starting with a capital letter
    return result

sample_text = "MitchelleKhannaIsLearningAnImportantTopicInPython"
result = insert_spaces(sample_text)
print(result)


# Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

# In[62]:


text="MitchelleKhannaIsLearningAnImportantTopicInPythonCheck"
match=re.findall('[A-Z][a-z]+',text)
print(match)


# Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
# Sample Text: "Hello hello world world"
# Expected Output: Hello hello world
# 

# In[68]:


text="Hello hello world world"
sp= re.split(r'\s+', text)
new=[]
for i in sp:
    if not new or i!=new[-1]:
        new.append(i)
    
result=' '.join(new)
print(result)


# Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

# In[69]:


strings = ["mit123", "Hi Universe!", "blessings3", "45689", "?!@#$%^&*()"]
pat=re.compile('\w$')
new=[]
for i in strings:
    if pat.findall(i):
        new.append(i)
new


# Question 27-Write a python program using RegEx to extract the hashtags.
# Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
# Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']
# 

# In[70]:


Text= '''RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered 
USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo'''
match=re.finditer('\#\w+',Text)
new=[]
for i in match:
    new.append(i.group())
print(new)


# Question 28- Write a python program using RegEx to remove <U+..> like symbols
# Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
# Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
# Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders
# 

# In[71]:


text= "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
sp=re.sub('<\w+[+|A-Z|0-9]+>','',text)
sp


# Question 29- Write a python program to extract dates from the text stored in the text file.
# Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
# Note- Store this sample text in the file and then extract dates.
# 

# In[76]:


import re
with open('sample_text.txt','r+') as file:
    text=file.read()
    match=re.findall(r'\d{2}-\d{2}-\d{4}',text)
match


# Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
# The use of the re.compile() method is mandatory.
# Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
# Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.

# In[77]:


text="The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
pat=re.compile(r'\b\w{2,4}\b')
rem=pat.sub('',text)
print(rem)


# In[ ]:




