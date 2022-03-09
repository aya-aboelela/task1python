#!/usr/bin/env python
# coding: utf-8

# In[12]:


# 1. Print 

print('Hello from Jupyter')

# Define variable
my_str = 'Hello'
my_int = 16

print(my_str)
print(my_int)


my_str

    



# In[8]:


# 2. Conditionals:
number_of_apples = 5

if number_of_apples < 1:
    print('You have no apples')
elif number_of_apples == 1:
    print('You have one apple')
elif number_of_apples < 4:
    print('You have a few apples')
else:
    print('You have many apples!')
    


# In[9]:


# 3. Lists


student_names = ['Alice', 'Bob', 'Carol', 'Dave']


student_names[1]


# In[10]:


# Print first item:
student_names[0]


# In[11]:


# Print last item:
student_names[-1]


# In[13]:


# Get a subset of the list items:

student_names[0:2]


# In[14]:


# Slicing from the beginning of the list:
student_names[:2]


# In[15]:


# Slicing to the end of the list:
student_names[2:]


# In[16]:


# 3.2 Mutable
# Add items to the end of the list:
student_names.append('Esther')
student_names


# In[17]:


# delete items:
del student_names[2]
student_names


# In[18]:


# 3.3 Non-unique
# Add the same name to list:
student_names.append('Esther')
student_names.append('Esther')
student_names


# In[19]:


# 4. Loops
student_names = ['Alice', 'Bob', 'Carol', 'Dave']

for student_name in student_names:
    print('Hello ' + student_name + '!')


# In[20]:


# 4.2 Loops, lists, and conditionals
# Initialize an empty list and add to it the
# student names containing more than four characters
long_names = []
for student_name in student_names:
    # This is our criterion
    if len(student_name) > 4:
        long_names.append(student_name)

long_names


# In[21]:


# 4.3 Nested loops
student_names = ['Alice', 'Bob', 'Carol', 'Dave']

student_pairs = []
for student_name_0 in student_names:
    for student_name_1 in student_names:
        student_pairs.append(
            (student_name_0, student_name_1)
        )

student_pairs


# In[22]:


# Filter out repeat of name:

student_names = ['Alice', 'Bob', 'Carol', 'Dave']

student_pairs = []
for student_name_0 in student_names:
    for student_name_1 in student_names:
        # This is the criterion we added
        if student_name_0 != student_name_1:
            student_pairs.append(
                (student_name_0, student_name_1)
            )

student_pairs


# In[23]:


# 5. Tuples
student_grade = ('Alice', 'Spanish', 'A-')
student_grade


# In[25]:


# 5.2 Unpacking

student_grade = ('Alice', 'Spanish', 'A-')
student_name, subject, grade = student_grade

print(student_name)
print(subject)
print(grade)

student_grades = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]

for student_name, subject, grade in student_grades:
    if grade.startswith('A'):
        print('Congratulations', student_name,
              'on getting an', grade,
              'in', subject)


# In[26]:


# 6. Dictionaries
foreign_languages = {
    'Alice': 'Spanish',
    'Bob': 'French',
    'Carol': 'Italian',
    'Dave': 'Italian',
}
foreign_languages['Carol']


# In[29]:


# Check if a particular key is in a dictionary:
'Zeke' in foreign_languages


# In[30]:



# Add an entry that doesn't exist
foreign_languages['Esther'] = 'French'
foreign_languages


# In[31]:


# Delete an entry that exists
del foreign_languages['Bob']
foreign_languages


# In[32]:


# Change an entry that does exist
foreign_languages['Esther'] = 'Italian'
foreign_languages


# In[47]:


# 6.4 Looping over dictionaries:
for key in foreign_languages:
    value = foreign_languages[key]
    print(key, 'is taking', value)
    


# In[37]:


# 6.5 Dictionaries as records:
record = {
    'name': 'Alice',
    'subject': 'Spanish',
    'grade': 'A',
}
print(record['name'],
      'got a grade of', record['grade'],
      'in', record['subject'])


# In[39]:


# 7. Combining Data Types
# 7.1 List of tuples:
student_grades = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]

student_grades[1]


# In[40]:


# work with the individual tuples:

student_grades[1][2]


# In[41]:


# 7.2 List of dictionaries
student_grade_records = []
for student_name, subject, grade in student_grades:
    record = {
        'name': student_name,
        'subject': subject,
        'grade': grade,
    }
    student_grade_records.append(record)
    
student_grade_records


# In[42]:


# Print one dictionary from list of dictioneris :

student_grade_records[1]


# In[43]:


# Work with the individual records:

student_grade_records[1]['grade']


# In[44]:


# 7.3 Dictionary of dictionaries
foreign_language_grades = {}
for student_name, subject, grade in student_grades:
    record = {
        'subject': subject,
        'grade': grade,
    }
    foreign_language_grades[student_name] = record
    
foreign_language_grades


# In[45]:


# Print one dictionery by using student name:
foreign_language_grades['Alice']


# In[46]:


# 7.4 Dictionary with tuple keys
student_course_grades = {}
for student_name, subject, grade in student_grades:
    student_course_grades[student_name, subject] = grade
    
student_course_grades


# In[ ]:




