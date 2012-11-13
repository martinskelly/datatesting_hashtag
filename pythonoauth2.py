from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import serial 

# Go to http://dev.twitter.com and create an app. 
# The consumer key and secret will be generated for you after
consumer_key="2Fo0l3djWI0mCzoL15H5dA"
consumer_secret="UWRJrJrOc379uQW3sAdTOu4s7X2GjOkKmCCRhvHM1ug"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="167338854-rnucLEksLEscrfOWoajK26wWrl147Nhua4i3FKCT"
access_token_secret="IwR6NHmkoc7FaIykxEVhhGTrULV9HnXDbcCtYXBLFY"

ser = serial.Serial('/dev/cu.usbmodemfa131', 9600)
ser = serial.Serial('/dev/ttyACM0', 9600)

class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream. 
	This is a basic listener that just prints received tweets to stdout.

	"""
	def on_data(self, data):
		print data
		ser.write('F')
		return True

	def on_error(self, status):
		print status

if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	stream = Stream(auth, l)	
	stream.filter(track=['#datatesting'])