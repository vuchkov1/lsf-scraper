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
    subreddit = reddit.subreddit('LivestreamFail')
    top_lines = subreddit.top('week', limit=5)
    for line in top_lines:
        if line.ups<800:
            break
        print('Title: %s\nUpvotes: %d\nUrl: %s\n' % (line.title, line.ups, line.url))

