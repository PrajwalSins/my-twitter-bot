import tweepy
import time
from googlesearch import search
import nltk
from nltk.corpus import stopwords
import pymongo
from pymongo import MongoClient
from spellchecker import SpellChecker

CONSUMER_KEY = 'osDCxy9STdyR9ImpAt9GQNN5c'
CONSUMER_SECRET = 'W5VxgaTzZro9aUMYTj9WMny5IBpDaZEWZ7jngw806N1ndpTLDd'
ACCESS_KEY = '1087023067589570565-lnSoT1rKcYQ8Ba4CJBjp2MX02kh5q5'
ACCESS_SECRET = 'CCzzFlPHrbNYjGgb00WsekI9ehT9fZupJNnu0OFrMNo5k'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def retrieve_last_seen_id():
	f_read = open('last_seen.txt', 'r')
	last = f_read.read()
	f_read.close()
	x = int(last)
	return x

def store_last_seen_id(last_seen_id):
	s = str(last_seen_id)
	f_write = open('last_seen.txt', 'w')
	f_write.write(s)
	f_write.close()
	return

def analyze(topic):
	spell_check = SpellChecker()
	stop_words = stopwords.words('english')
	full_sentence = topic.split(" ")
	for i in range(0, len(full_sentence)):
		full_sentence[i] = spell_check.correction(full_sentence[i])
	filtered_sentence=[]
	for word in full_sentence:
		if word not in stop_words:
			filtered_sentence.append(word)
	match_percent = search_database(filtered_sentence)
	if(match_percent >= 90):
		return True
	else:
		return False
		
def search_database(filtered_sentence):
	client = MongoClient('localhost', 27017)
	database = client['programming_terms']
	terms = database['programming_related_terms']
	counter, total = 0, len(filtered_sentence)
	for word in filtered_sentence:
		character = word[0]
		querry = { character: word}
		resulting_dictionary = terms.find(querry)
		if (word in resulting_dictonary[character]) == True:
			counter +=1
	result_percent = (counter/total)*100
	return result_percent

def internet_search(topic):
	search_results = []
	for url in search(topic, tld = 'com', lang = 'en', stop = 5):
			search_results.append(url)
	text  = 'Please refer to following links:=>' + '\n1 ' + search_results[0] + '\n2 ' + search_results[1] + '\n3 ' + search_results[2] + '\n4 '+ search_results[3] + '\n5 ' + search_results[4] 
	return text

def reply_to_tweets():
	last_seen_id = retrieve_last_seen_id()
	mentions = api.mentions_timeline(last_seen_id)
	for mention in reversed(mentions):
		last_seen_id = mention.id
		store_last_seen_id(last_seen_id)
		topic = mention.text.lower()
		validity = analyze(topic)
		if(validity == True):	
			results = internet_search(topic)  
			api.update_status('@' + mention.user.screen_name + results, mention.id)
		elif(validity == False):
			api.update_status('@' + mention.user.screen_name + "Sorry cannot find anything,Please try something else related to programming.", mention.id)	

while True:
	reply_to_tweets()
	time.sleep(15)
