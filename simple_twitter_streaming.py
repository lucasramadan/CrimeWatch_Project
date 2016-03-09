# Code from http://adilmoujahid.com/posts/2014/07/twitter-analytics/
# Import tweepy library

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pprint import pprint
import json

# Create variables to hold my credentials
access_token = "4264444814-6NL7EBoxH3uLDAR5ui6OsCC3xq2ba38M7ZjUDFQ"
access_token_secret = "KfLqfQi4llqBinZFLUnaPozg2CrubmHs8vy0PsmrT4CXy"
consumer_key = "BUFnkoDJxoxLCkJue0WPtqSK1"
consumer_secret = "fo298tDkfm4FgmuIja3o7qpR8KPRqkxEsAc2VItl4KMc2hBAr7"

#Basic listener to print the received tweets to stdout

class StdOutListener(StreamListener):

    def on_data(self, data):
    	print data
    	return True

	def on_error(self,status):
		print status

if __name__ == '__main__':

	# Handles Twitter authentification and the connection to Twitter Streaming API
	s_listen = StdOutListener()
	auth = OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, s_listen)

	#Filters Twitter Streams to capture data by keywords: 'python','javascript','ruby'
	'''
	First keyword search
	'''

	stream.filter(location=['San Francisco', 'san francisco', 'san fran'])
	# stream.filter(track=[ 'crime san francisco', 'robbery san francisco', 'burglary san francisco', 'robbed san francisco', 'theft san francisco', 'assault san francisco', 'arson san francisco', 'robbed SF'])