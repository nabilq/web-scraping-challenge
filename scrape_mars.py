# dependencies here
import os

# make a function that will automatically scape everything
def scrape():

    # SCRAPE STUFF GOES HERE
    # from jupyter notebook
  

# In[54]:


    from splinter import Browser
    from bs4 import BeautifulSoup
    import time
    import requests


# In[55]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


# In[56]:


    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(5) 


# In[57]:


    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve the first element with the title info
    section = soup.find_all('div', class_='list_text', limit=1)


# In[58]:


    section


# In[59]:


    for sec in section:
        #get first and only title
        news_title=sec.find('div', class_='content_title').text
        #get paragraph
        news_p=sec.find('div', class_='article_teaser_body').text
    


    


# In[60]:


#check if news_title captured title
    news_title


# In[61]:


#check if paragrah captured title
    news_p


# ## JPL Mars Space Images - Featured Image

# In[62]:


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(5) 


# In[63]:


    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve the element with the pic info
    section2 = soup.find('div', class_='carousel_items')


# In[64]:


    #check section2 contents
    section2


# In[65]:


    for sec2 in section2:
        article= section2.find('article')
        img_url = article['style']
    
    


# In[66]:


    #check img_url
    img_url


# In[67]:


    #get url link within string
    clean_img_url=img_url.split("'", 1)[1].split("'")[0]


# In[68]:


    #combine url link with base to get complete url
    featured_image_url ='https://www.jpl.nasa.gov' + clean_img_url


# In[69]:


    featured_image_url


# ## Mars Weather

# In[70]:


    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(5) 


# In[123]:


    import re
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve the element with the pic info
    #section3 = soup.find_all('div', class_='css-1dbjc4n r-my5ep6 r-qklmqi r-1adg3ll')
    section3=soup.find_all('span',class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')


# In[121]:


    #check section3
    section3


# In[137]:


    #weather details start with 'InSight'-retrieve all strings with 'InSight'
    marsweathers=soup.find_all(string=re.compile("InSight"))


# In[143]:


    #get first element which represents latest weather tweet and remove 'InSight'
    mars_weather = marsweathers[0].strip('InSight') 


# In[144]:


    #remove white space where 'InSight' was 
    mars_weather=mars_weather.strip()


# In[146]:


    #check variable
    mars_weather


# ## Mars Facts

# In[179]:


    import pandas as pd
    url = 'https://space-facts.com/mars/'

    tables = pd.read_html(url)
    tables


# In[176]:


#take first table
    df = tables[0]


# In[177]:


    #rename columns
    df.rename(columns={0:'Description',
                          1:'Value'}, 
                 inplace=True)


# In[180]:


    #set index to column 'Description'
    df.set_index('Description', inplace=True)
    df


# In[181]:


    html_table = df.to_html()
    html_table


# In[182]:


    html_table.replace('\n', '')


# ## Mars Hemisphere

# In[183]:


#valles_marineris
#hemispheres

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    time.sleep(5) 


# In[235]:


    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve page
    results = soup.find_all('div', class_="container")


# In[241]:


    for result in results:
        li = result.find('li')
        link = li.a['href']
        h2 = result.find('h2', class_='title').text
    


# In[239]:





# In[242]:





# In[245]:


    valles_dictionary={"title": h2, "img_url":link} 
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)
    time.sleep(5) 
     # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve page
    results = soup.find_all('div', class_="container")
   

    for result in results:
        li = result.find('li')
        schialink = li.a['href']
        schiah2 = result.find('h2', class_='title').text

    schia_dictionary={"title": schiah2, "img_url":schialink}  

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)
    time.sleep(5) 
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve page
    results = soup.find_all('div', class_="container")

    for result in results:
        li = result.find('li')
        syrtislink = li.a['href']
        syrtish2 = result.find('h2', class_='title').text
    
    syrtis_dictionary={"title": syrtish2, "img_url":syrtislink}  

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    time.sleep(5) 
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve page
    results = soup.find_all('div', class_="container")

    for result in results:
        li = result.find('li')
        cerlink = li.a['href']
        cerh2 = result.find('h2', class_='title').text

    cer_dictionary={"title": cerh2, "img_url":cerlink}  



# In[248]:


    hemisphere_image_urls=[]
    dictionary_copy1=valles_dictionary.copy()
    dictionary_copy2=schia_dictionary.copy()
    dictionary_copy3=syrtis_dictionary.copy()
    dictionary_copy4=cer_dictionary.copy()
    hemisphere_image_urls.append(dictionary_copy1)
    hemisphere_image_urls.append(dictionary_copy2)
    hemisphere_image_urls.append(dictionary_copy3)
    hemisphere_image_urls.append(dictionary_copy4)


# In[ ]:


#hemisphere_image_urls = [
   # {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    #{"title": "Cerberus Hemisphere", "img_url": "..."},
    #{"title": "Schiaparelli Hemisphere", "img_url": "..."},
   # {"title": "Syrtis Major Hemisphere", "img_url": "..."},

    # this dictionary will hold EVERYTHING
    dict_scrape = {
        "Headline":news_title, 
        "Paragraph":news_p,
        "FeaturedImage": featured_image_url,
        "Weather": mars_weather,
        "Facts": html_table,
        "Images": hemisphere_image_urls

        }

    return dict_scrape

