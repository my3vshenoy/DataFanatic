
# coding: utf-8

# <b>Goal:</b> Analyze data on Thanksgiving dinner in the US.

# <b>About the data:</b>
# 
# The dataset is stored in the thanksgiving.csv file. It contains 1058 responses to an online survey about what Americans eat for Thanksgiving dinner.
# 
# Each survey respondent was asked questions about what they typically eat for Thanksgiving, along with some demographic questions, like their gender, income, and location. This dataset will allow us to discover regional and income-based patterns in what Americans eat for Thanksgiving dinner.

# <b>Some statistics of the data:</b>
# 
# The dataset has 65 columns, and 1058 rows. Most of the column names are questions, and most of the column values are string responses to the questions. Most of the columns are categorical, as a survey respondent had to select one of a few options.

# <b>Information about the important rows and columns</b>
# 
# <li><b>RespondentID </b>-- a unique ID of the respondent to the survey.
# 
# <li><b>Do you celebrate Thanksgiving?</b> -- a Yes/No reponse to the question.
# <li><b>How would you describe where you live?</b> -- responses are Suburban, Urban, and Rural.
# <li><b>Age</b> -- resposes are one of several categories, such as 18-29, and 30-44.
# <li><b>How much total combined money did all members of your household earn last year?</b> -- one of several categories, such as $75,000 to $99,999.

# In[7]:


#Import the pandas package
import pandas as pd


# In[8]:


#Use the pandas.read_csv() function to read the thanksgiving.csv file in.
data = pd.read_csv("thanksgiving.csv", encoding = "Latin-1")

print(data.head())


# In[9]:


print(data.columns)


# #Because we want to understand what people ate for Thanksgiving, we'll remove any responses from people who don't celebrate it. The column Do you celebrate Thanksgiving? contains this information. We only want to keep data for people who answered Yes to this questions.

# #The pandas.Series.value_counts() method to display counts of how many times each category occurs in the Do you celebrate Thanksgiving? column.

# In[10]:


data["Do you celebrate Thanksgiving?"].value_counts()


# In[11]:


is_yes = data["Do you celebrate Thanksgiving?"] == "Yes"
data_yes_celebrate_thanksgiving = data[is_yes]


# In[12]:


#is_yes = data["Do you celebrate Thanksgiving?"] == "Yes"
#data = data[is_yes]


# In[13]:


#print(is_yes)


# In[14]:


data_yes_celebrate_thanksgiving["Do you celebrate Thanksgiving?"].value_counts()


# #the pandas.Series.value_counts() method to display counts of how many times each category occurs in the What is typically the main dish at your Thanksgiving dinner? column.

# In[15]:


data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()


# In[16]:


is_Tofurkey = data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"
data_main_dish_Tofurkey = data[is_Tofurkey]


# In[17]:


data_main_dish_Tofurkey["What is typically the main dish at your Thanksgiving dinner?"].value_counts()


# In[18]:


gravy_column = data_main_dish_Tofurkey["Do you typically have gravy?"]


# In[19]:


print(gravy_column)


# Now that we've looked into the main dishes, let's explore the dessert dishes. Specifically, we'll look at how many people eat Apple, Pecan, or Pumpkin pie during Thanksgiving dinner. This data is encoded in the following three columns:
# 
# <li>Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple
# <li>Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin
# <li>Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan

# In all three columns, the value is either the name of the pie if the person eats it for Thanksgiving dinner, or null otherwise.
# 
# 

# We can find out how many people eat one of these three pies for Thanksgiving dinner by figuring out for how many people all three columns are null.

# In[20]:


#Generate a Boolean Series indicating where the Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple column is null.
apple_isnull = data_yes_celebrate_thanksgiving["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"].isnull() 


# In[21]:


#Generate a Boolean Series indicating where the Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin column is null.
pumpkin_isnull = data_yes_celebrate_thanksgiving["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"].isnull()


# In[22]:


#Generate a Boolean Series indicating where the Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan column is null.
pecan_isnull = data_yes_celebrate_thanksgiving["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"].isnull()


# In[23]:


#Join all three Series using the & operator
ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull


# In[24]:


ate_pies.value_counts()


# Let's analyze the Age column in more depth. This will make it simple to figure out things like the average age of survey respondents. <br>
# The age value falls in one of the below windows:<br>
# <li>18-29
# <li>30-44
# <li>45-59
# <li>60+
# <li>null

# In[25]:


data["Age"].value_counts()


# In[33]:


def convert_to_int(age):
    if pd.isnull(age):
        return None
    age = age.split(" ")[0]
    #When the age bracket is 60+, the split will fetch the + symbol as well. So, we replace it
    age = age.replace("+", "")
    return int(age)
    


# In[34]:


data["int_age"] = data["Age"].apply(convert_to_int)


# In[35]:


data["int_age"].describe()


# <h1> Findings: </h1>
# <body>In a total of 1025 surveyors, the youngest surveyor is 18 years old and the oldest is 60. Since we have taken the lower value of the age bin, the ages are vary uniformly. The average age of the surveyor is 39.

# How much total combined money did all members of your HOUSEHOLD earn last year?

# In[44]:


def convert_income_to_int(income):
    if (pd.isnull(income) or income.split(" ")[0] == "Prefer"):
        return None
    income = income.split(" ")[0]
    income = income.replace("$", "")
    income = income.replace(",", "")
    return int(income)
    


# In[45]:


data["int_income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(convert_income_to_int)


# In[46]:


data["int_income"].describe()


# <h1>Findings</h1>
# <body><li>Since we are taking the lower value of the range, the accuracy of the prediction may be skewed. Because a person with \$49,000 salary would be counted to have a salary of $25,000. <li>Also, the mean looks very large and can cause an error as there are very few people who have a higher income.

# We can now see how the distance someone travels for Thanksgiving dinner relates to their income level. It's safe to hypothesize that people earning less money could be younger, and would travel to their parent's houses for Thanksgiving. People earning more are more likely to have Thanksgiving at their house as a result.

# In[47]:


data["How far will you travel for Thanksgiving?"].value_counts()


# In[49]:


is_earning_under_15k = data["int_income"] < 15000
earning_under_15k = data[is_earning_under_15k]


# In[51]:


earning_under_15k["How far will you travel for Thanksgiving?"].value_counts()


# In[52]:


is_earning_over_15k = data["int_income"] > 15000
earning_over_15k = data[is_earning_over_15k]


# In[53]:


earning_over_15k["How far will you travel for Thanksgiving?"].value_counts()


# <h1>Findings</h1>
# <body><li>Surveyors earning less than \$15000 tend to stay at home compared to the option of flying as it can be expensive
# <li> However, in comparison to people earning over \$15000, they travel more as going to someone else's party works out better

# In the US, a "Friendsgiving" is when instead of traveling home for the holiday, you celebrate it with friends who live in your area. Both questions seem skewed towards younger people. Let's see if this hypothesis holds up.

# In order to see the average ages of people who have done both, we can use a pivot table.

# Generate a pivot table showing the average age of respondents for each category of <b>"Have you ever tried to meet up with hometown friends on Thanksgiving night?"</b> and <b>"Have you ever attended a "Friendsgiving?"</b>

# In[54]:


data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_age"
)


# In[55]:


data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_income"
)


# <h1>Findings</h1>
# <li>It appears that people who are younger (average: 33 years) are more likely to attend a Friendsgiving, and try to meet up with friends on Thanksgiving.
# <li>It appears that people who earn less are more likely to go for a Friendsgiving (average income: 66019 USD)
