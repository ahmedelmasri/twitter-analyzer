# twitter-analyzer
A python library specialized in analyzing tweet datasets using NLP and Network Analysis

The end-user can immediatly clone the repo and start working with the package

Steps:
------
1- using your own tweet dataset of (user_handle, tweet_text), you can extract a list of relevant tweets as follows

  import tanalyzer as twt

  The first argument is designated for passing the datafile
  The second argument is designated for the list of search keywords 
  The call returns a list of relevant tweets related to the search keywords for each user_handle

  ex:
  ----
  list_of_relevant_tweets = twt.extract_relevant_tweets("data/twitter-data.txt", ["climate", "weather"]) 

2- Now we can construct lists of interests
  * user-hashtags 
  * user-mentions
  * user-bigrams
  * user-sentiment

  ex:
  user_hashtag_list = twt.construct_user_sentiment_list(list_of_relevant_tweets)

3- Now you can construct a network of user_hashtags as follow

  import networkanalysis as sna
  
  user_hashtag_graph = sna.construct_user_hashtag_network(user_hashtag_list)

4- Now you can analyze the graph's centrality as follows

  closeness = sna.closeness(user_hashtag_graph)
  for node in user_hashtag_graph:
    print("Node: {} has Closeness Centrality {}: ".format(node, closeness[node]))
    
  
Enjoy! 
  
  
  
