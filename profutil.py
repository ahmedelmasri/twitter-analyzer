#!/usr/bin/env python
# coding: utf-8

def write_tweet_tfile(file_to_populate, text):
    file_handler = open(file_to_populate,"a+")  
    file_handler.writelines(text) 
    file_handler.close()


def strip_token(myword, chars_token):
	return myword.strip(chars_token)
