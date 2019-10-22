#!/usr/bin/env python
# coding: utf-8

import networkx as nx
from networkx.algorithms import bipartite

def construct_user_bigram_network(list_of_tuples):
    network = nx.Graph()
    bipartite_network.add_edges_from(list_of_tuples)    
    return network
        
    
def construct_user_sentiment_network(users_sentiments_tuples):
    network = nx.Graph()
    network.add_edges_from(users_sentiments_tuples)    
    return network    
    
def construct_user_hashtag_network(users_hashtag_tuples):
    network = nx.Graph()
    network.add_edges_from(users_hashtag_tuples)    
    return network      
    
    
# This function is to project the set of keywords,
#  hashtags, or sentiments onto the twitter users
def project_notwork(bnetwork, list_of_items):    
    if nx.is_bipartite(bipartite_network):
        # print("My network is Bipartite")
        projected_nodes = bipartite.weighted_projected_graph(bipartite_network, list_of_items)        
    # nx.draw(projected_users, with_labels=True)
    return projected_nodes             
    
    
def closeness(network):
    closeness = nx.closeness_centrality(network) 
    return closeness
    
    
def degree(network):
    degrees = nx.degree_centrality(network) 
    return degrees    

def betweenness(network):
    betweenness = nx.betweenness_centrality(network) 
    return betweenness 

    
    