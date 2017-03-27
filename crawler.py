import tweepy
import urllib.request
import os

cons_key, cons_sec, tok_key, tok_sec= open('key.config', encoding='utf-8').read().split('\n')
auth = tweepy.OAuthHandler(cons_key, cons_sec)
auth.set_access_token(tok_key, tok_sec)
api = tweepy.API(auth, wait_on_rate_limit=True)


def download_url(url, path='Downloads/'):
    if os.path.exists(path + url[1]):
        return
    urllib.request.urlretrieve(url[0], path + url[1])
    print('downloaded' + url[1])


def crawl_videos(name, count):
    twts = api.user_timeline(screen_name=name, count=count)
    urls = []
    for t in twts:
        try:
            v = t.extended_entities['media'][0]['video_info']['variants'][0]
            u = v['url']
            s = u.split('/')
            if u.endswith('mp4'):
                download_url((u, s[len(s)-1]))
        except AttributeError:
            pass
        except KeyError:
            pass


def crawl_images(name, count):
    twts = api.user_timeline(screen_name=name, count=count)
    urls = []
    for t in twts:
        try:
            for media in t.entities['media']:
                u = media['media_url_https']
                s = u.split('/')
                download_url((u, s[len(s)-1]), path='Ryuarin/')
        except AttributeError:
            pass
        except KeyError:
            pass

crawl_images('_RyuaRin', 600000)
