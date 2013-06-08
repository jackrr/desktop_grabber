#downloads top submissions from reddit image subreddits and puts them in the desktops folder 
#also deletes yesterday's images to save space/keep content fresh
#intended to be run as a cron tab
import praw
import urllib
import os
import sys

if len(sys.argv) != 4:
    print ("usage: python grabber.py download_num sr_list(comma delim) imgs_dir")
    sys.exit()

#number of top submissions to download from each subreddit
DOWNLOAD_NUM = int(sys.argv[1])

#subreddits to download from
SR_LIST = sys.argv[2].split(',')

#desktop directory
#DESK_DIR = "/Users/mbc/daily_desktops/"
DESK_DIR = sys.argv[3]

print "downloading "+str(DOWNLOAD_NUM)+" images max per reddit from: "+str(SR_LIST)+" and storing them in "+DESK_DIR

#delete yesterday's photos
for f in os.listdir(DESK_DIR):
    if '.jpg' in f:
        print "deleting "+os.path.join(DESK_DIR, f)
        os.unlink(os.path.join(DESK_DIR, f))

#get today's photos
r = praw.Reddit(user_agent='Desktop_Grabber')
img_count = 0
for sub in SR_LIST:
    submissions = r.get_subreddit(sub).get_top(limit=DOWNLOAD_NUM)
    for x in submissions:
        if '.jpg' in x.url:
            urllib.urlretrieve(x.url, DESK_DIR+str(img_count)+".jpg") 
            print "trying to download "+x.url
            img_count += 1
