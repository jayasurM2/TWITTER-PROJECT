import streamlit as st
st.title("TWITTER SCRAPPING PROJECT")
import pymongo
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import date
from io import StringIO
st.subheader("Scrape Tweets with  Hashtag !")
st.title("Twitter scraping")
maxTweets = 100
# A list to append tweet data to
tweets = []
# Scrapped data was downloaded and append it to list.
Username=st.sidebar.text_input("Enter the User_Hashtag:")
start_date=st.sidebar.date_input("From_date(YYYY-MM-DD):")
end_date=st.sidebar.date_input("End_date(YYYY-MM-DD):")
def convert_dataframe(dataframe):
    return dataframe.to_csv().encode('utf-8')
if st.button('Click me'):
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f"from:{Username} since:{start_date} until:{end_date}").get_items()):
        if i>maxTweets:
            break
        tweets.append([ tweet.id,
                        tweet.user.username,
                        tweet.url,
                        tweet.rawContent,
                        tweet.replyCount,
                        tweet.retweetCount,
                        tweet.likeCount,
                        tweet.lang,
                        tweet.source,
                        tweet.date,])


tweetsdf = pd.DataFrame(tweets_list2, columns=['Tweet Id','Username', 'URL', 'Content', 'Replay Count', 'Re Tweet', 'Like Count', 'Lang', 'Source','Datetime'])
tweetsdf2
tweetdata = convert_dataframe(tweetsdf)
dic_value1=tweetdf.to_dict('list')
client=pymongo.MongoClient("mongodb+srv://Jayasuriyaa:Suriya27@cluster0.qyd69sg.mongodb.net/test")
db=client["project"]
twitter_data=db["scrappeddata"]    
twitter_data.insert_one(dic_value1)
#where the upload data was found                      
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
#     To read file as bytes:
    data1 = uploaded_file.getvalue()
    st.write(data1)
    data2= pd.read_csv(uploaded_file)
    dic_value=data2.to_dict('list')
    dic_value
    twitter_data.insert_one(dic_value)
    st.success('Upload to MongoDB Successful!', icon="✅")
   

 #Download file
upload_file = convert_dataframe(data2)
st.download_button(
    label="Download the scraped  data as CSV",
    data=tweetdata,
    file_name='scraped_data.csv',
    types='text/csv')
st.download_button(
    label="Download the upload data as CSV",
    data=upload_file,
    file_name='upload_file_data.csv',
    types='text/csv')