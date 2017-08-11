from pytube import YouTube
import urllib2
import sys
from lxml import etree
import time
import random
import os

with open('user_agent.txt', 'r') as f:
    text = f.read()
    user_agent_list = text.split('\n')

def getUrl_multiTry(url, query, index):
    maxTryNum = 10
    video = "NOTHING"
    selected = False
    for tries in range(maxTryNum):
        try:
            yt = YouTube(url)
            print yt.get_videos(), " for ", query
            video = yt.filter("mp4")[-1]
            print "Choose ", video, " for ", query, " at ", url
            selected = True
            break
        except:
            if tries < (maxTryNum - 1):
                #print "Time %d" % tries
                time.sleep(3)
                continue
            else:
                #print "Time %d" % tries
                print "Has tried %d times to access url %s, all failed!" % (maxTryNum, url)
                time.sleep(3)
                break
    if selected == True:
        filepath = "/video/" + query + "/"
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)
        yt.set_filename(query + str(index))
        video.download(directory)
        print "Downloaded", video, " for ", query

def getlists_multitry(query):
    page_url = \
            'https://www.youtube.com/results?search_query=' + query
    print "Visit " + page_url
    chances = 20
    lenlist = 0
    while ( chances > 0 and lenlist == 0):
        time.sleep(10)
        headers = {
            "User-Agent" : random.choice(user_agent_list)
        }
        req = urllib2.Request(
            url = page_url,
            headers = headers
        )
        response = urllib2.urlopen(req)
        #print response.read()
        ss = etree.HTML(response.read())
        list = ss.xpath("//a[contains(@href,'/watch?v=') and @title]")
        lenlist = len(list)
        chances = chances - 1
    if(lenlist == 0):
        print "False to connect to " + page_url
    print "There are %d searched answer" % lenlist
    index = 0
    for context_item in list:
        href = context_item.xpath('@href')[0]
        str = "http://www.youtube.com" + href
        getUrl_multiTry(str, query, index)
        index = index + 1

if len(sys.argv) < 2:
    print('Please give some words as a query')
else:
    query = '+'.join( sys.argv[1::] )
    print 'query is %s' % query
    getlists_multitry(query)