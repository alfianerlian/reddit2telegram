#encoding:utf-8

from utils import get_url, weighted_random_subreddit


t_channel = '@r_bitcoin'
subreddit = weighted_random_subreddit({
    'btc': 0.0,
    'bitcoin': 1.0
})


def send_post(submission, r2t):
    what, url, ext = get_url(submission)
    title = submission.title
    link = submission.shortlink
    text = '{}\n{}'.format(title, link)

    if what == 'text':
        punchline = submission.selftext
        text = '{}\n\n{}\n\n{}'.format(title, punchline, link)
        return r2t.send_text(text)
    elif what == 'other':
        base_url = submission.url
        text = '{}\n{}\n\n{}'.format(title, base_url, link)
        return r2t.send_text(text)
    elif what == 'album':
        base_url = submission.url
        text = '{}\n{}\n\n{}'.format(title, base_url, link)
        r2t.send_text(text)
        r2t.send_album(url)
        return True
    elif what in ('gif', 'img'):
        return r2t.send_gif_img(what, url, ext, text)
    else:
        return False
