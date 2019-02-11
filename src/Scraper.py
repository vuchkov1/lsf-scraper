import praw
import credentials
import urllib.request


def download_clip(url, title):
    urllib.request.urlretrieve(url, title+'.flv')


def samo_levski():
    return "SAMO LEVSKI"


def login():
    reddit = praw.Reddit(client_id=credentials.client_id,
                         client_secret=credentials.client_secret,
                         username=credentials.username,
                         password=credentials.password,
                         user_agent='r/LivestreamFail/ scraper')
    print('Logged in')
    return reddit


if __name__ == '__main__':
    reddit = login()
    subreddit = reddit.subreddit('LivestreamFail')
    limit=10
    top_lines = subreddit.top('day', limit=limit)
    myfile = open('xyz.txt', 'w')
    for line in top_lines:
        # if line.ups<800:
        #     break
        myfile.write("%s\n" % line.url)

    myfile.close()
        # download_clip(line.url, line.title)
        # print('Title: %s\nUpvotes: %d\nUrl: %s\n' % (line.title, line.ups, line.url))

