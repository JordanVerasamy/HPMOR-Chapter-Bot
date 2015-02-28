import praw
import time
import httplib
import sys

# returns the HTTP status code of `host` at `path`
def get_status_code(host, path="/"):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status
    except StandardError:
        return None

# to use these command line arguments properly, the bash command will look like:
# $ python hpmorbot.py <chapternumber> <username> <password>

chapter = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]

r = praw.Reddit('Taking free karma from /r/hpmor durng the final arc kappa')
r.login(username, password)
subreddit = r.get_subreddit('hpmor')

while True:
	status_code = get_status_code('hpmor.com', '/chapter/' + chapter)
	if status_code == 200:
		# New chapter is up. Post it to the subreddit and terminate.
		r.submit(subreddit, 'Chapter ' + chapter, url='hpmor.com/chapter/' + chapter)
		print 'Posted link to /r/hpmor! Free karma inbound!'
		break
	else:
		# New chapter isn't up yet. Keep trying.
		print 'Nothing posted yet. Status code:', status_code, 'at', time.time()
		time.sleep(0.6)

