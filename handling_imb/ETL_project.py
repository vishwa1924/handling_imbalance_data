#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
from sqlalchemy import create_engine


# In[2]:


def get_URI(query:str, page_num:str, date:str, API_KEY:str) -> str:
    """# obtain the URI for access to articles for a given query, page number, and date"""
    
    # append query to uri
    URI = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={"covid"}'
    
    # add page_num and date parameters
    URI = URI + f'&page={10}&begin_date={5/12/2022}&end_date={5/13/2022}'
    
    # add API key
    URI = URI + f'&api-key={"cLado0kSBDKhVRbKrTKsOf5KcQHeuAhA"}'
    
    # return the new URI 
    return URI


# In[3]:


import time 
import datetime 

# create a dataframe that will store all articles 
df = pd.DataFrame()

# get current date
current_date = datetime.datetime.now().strftime('%Y%m%d')

# collect data from all available pages
page_num = 1
while True:
    # get the URI needed for the articles related to Winter Olympics from newest to oldest
    URI = get_URI(query='COVID', page_num=str(1), date=5/13/2022, API_KEY="cLado0kSBDKhVRbKrTKsOf5KcQHeuAhA")

    # make a request with the url
    response = requests.get(URI)

    # collect the data from the response in JSON format
    data = response.json() 

    # convert data to a data frame
    df_request = json_normalize(data["response"], record_path=['docs'])

    # end loop if no new articles are available 
    if df_request.empty:
        break

    # append df_request to the dataframe
    df = pd.concat([df, df_request])

    # pause to stay within the limit of number of requests
    time.sleep(6)

    # go to the next page
    page_num += 1


# In[21]:


URI = get_URI(query='Winter Olympics', page_num=1, date= 5/12/2022 , API_KEY="cLado0kSBDKhVRbKrTKsOf5KcQHeuAhA")


# In[22]:


import requests

# make a request to the server 
response = requests.get(URI)

# parse the response (only works for JSON format)
data = response.json() 


# In[23]:


print(data)


# In[ ]:


# obtain the URI for access to articles for a given query, page number, sorting order
def get_URI(query:str, page_num:int, sort_order:str, API_KEY:str) -> str:
    
    # create a URI string
    URI = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q='+query
    
    # if a page number is mentioned, add it to the URI
    if page_num:
        add_to_URI = '&page='+str(page_num)
        URI+= add_to_URI
    
    # if the sorting order is mentioned, add it to the URI
    if sort_order:
        add_to_URI = '&sort='+sort_order
        URI += add_to_URI
    
    # add the given API key to the URI
    add_to_URI = '&api-key='+API_KEY
    URI += add_to_URI
    
    # return the new URI 
    return URI


# In[ ]:





# In[29]:


def get_URI(query:str, page_num:int, sort_order:str, API_KEY:str) -> str:
    
    # create a URI string
    URI = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q='+"covid"
    
    # if a page number is mentioned, add it to the URI
    if page_num:
        add_to_URI = '&page='+str(page_num)
        URI+= add_to_URI
    
    # if the sorting order is mentioned, add it to the URI
    if sort_order:
        add_to_URI = '&sort='+sort_order
        URI += add_to_URI
    
    # add the given API key to the URI
    add_to_URI = '&api-key='+API_KEY
    URI += add_to_URI
    
    # return the new URI 
    return URI


# In[35]:



# get the URI needed for the articles related to Winter Olympics in page 1 from newest to oldest
URI = get_URI(query='covid', page_num=1, sort_order='newest', API_KEY="cLado0kSBDKhVRbKrTKsOf5KcQHeuAhA")


# In[36]:


import requests

# make a request to the server 
response = requests.get(URI)

# parse the response (only works for JSON format)
data = response.json() 


# In[37]:


print(data)


# In[38]:


from pandas.io.json import json_normalize

# convert JSON response to a data frame
df = json_normalize(data['response'], record_path=['docs'])


# In[39]:


df[['headline.main', 'pub_date']].head(5)


# In[ ]:





# In[40]:


pip install gTTS


# In[41]:


from gtts import gTTS

text = "Hello! My name is Vishwa."
tts = gTTS(text)
tts.save("hi.mp3")


# In[ ]:





# In[42]:


text = input("Enter your text: ")
tts = gTTS(text)
tts.save("user_input.mp3")


# In[43]:


import os 
os.system("hi.mp3")


# In[45]:


pip install playsound


# In[46]:


from playsound import playsound
os.system("user_input.mp3")


# In[ ]:




