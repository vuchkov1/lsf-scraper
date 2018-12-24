import praw
import credentials

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
    subreddit = reddit.subreddit('formula1')
    top_lines = subreddit.top('week')
    # top_lines1 = reddit.hot(limit=10)
    for submission in reddit.front.hot():
        print(submission)

