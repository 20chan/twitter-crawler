import tweepy
import urllib.request
import os

screen_name = ''

cons_key, cons_sec, tok_key, tok_sec= open('key.config', encoding='utf-8').read().split('\n')
auth = tweepy.OAuthHandler(cons_key, cons_sec)
auth.set_access_token(tok_key, tok_sec)
api = tweepy.API(auth, wait_on_rate_limit=True)

if __name__ == '__main__':
    twts = api.user_timeline(screen_name=screen_name, count=10000)
    urls = []
    for t in twts:
        try:
            v = t.extended_entities['media'][0]['video_info']['variants'][0]
            u = v['url']
            s = u.split('/')
            if u.endswith('mp4'):
                urls.append((u, s[len(s)-1]))
        except AttributeError:
            pass
        except KeyError:
            pass
    for url in urls:
        if os.path.exists('Downloads/' + url[1]):
            continue
        urllib.request.urlretrieve(url[0], 'Downloads/' + url[1])
        print('downloaded!')
