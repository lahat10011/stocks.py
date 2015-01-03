
import time
import urllib
import re 

def get_time ():
	# looks up the date and time, returns a string
	return  (time.strftime("%d/%m/%y %H:%M"))

def get_minute():
	#returns minute as interger 
	return int(time.strftime("%M")) 

def min_break (minutes = 5):
	#checks to see if minute can be devided by a number with no remainder 
	if get_minute()%minutes==0:
		return True
	else:
		return False

def open_list(filename):
	""" opens and returns the list of stocks split by enter as seperate string
	filename -- it has to be a txt file, with a list of stock  names seperated by enter (/n)
	"""
	l= open(filename, "r")
	contents= l.read()
	return contents.split("\n")[:-1] 

def URL_Generator (stock_abbreviations):
	#this makes a url for the yahoo api to look up current stocks
	static= "http://download.finance.yahoo.com/d/quotes.csv?s="
	ID= ','.join(stock_abbreviations)
	properties= "&f=l1"
	return static+ID+properties
	
def Fetch_URL (url):
	#this returns the text from the stock  values
	url= urllib.urlopen(url)
	raw_text= url.read()
	return raw_text

def CSV_To_Floats (csv):
	#gets rid of the enters \r\n from the url returned values
	csv_split= csv.split("\r\n")[:-1]
	CSV_Float= map(float,csv_split)
	return CSV_Float

def get_stock_values (stock_abbreviations):
	#puts the stock abbreviations in a dict with the corresponding stock values
	url= URL_Generator(stock_abbreviations)
	data= Fetch_URL(url)
	l= CSV_To_Floats(data)
	dictionary= dict(zip(stock_abbreviations,l))
	return  dictionary
	

def remove_tags(html):
	#returns a str without HTML tags. takes as input a html str
        new = ''
        level=0
        for i in html:
                if i == '<': level +=1
                if level < 1: new +=i
                if i == '>': level -=1
        return new


def tweets(q):
	#returns 20 polon separated list of tweets of hashtag query
        url = 'https://twitter.com/search?f=realtime&q=%23'+q+'&src=typd'
        f = urllib.urlopen(url)
        raw = f.read()
        parts = raw.split('<p class="js-tweet-text tweet-text" lang="en" data-aria-label-part="0">')[1:]
        out = ''
        for part in parts:
                text =remove_tags(part).split('...')[0]
                text = text.split('\n')[0]
                out += text + '|'
        return out[:-1]
	
		
