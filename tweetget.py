import tweepy
import csv


CONSUMER_KEY = "取得したーキーを入力"
CONSUMER_SECRET = "取得したーキーを入力"
ACCESS_TOKEN = "取得したーキーを入力"
ACCESS_SECRET = "取得したーキーを入力"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

tweet_data = [] #取得したツイートを格納するリスト
#q=の後に検索したいキーワード入力
for tweet in api.search(q="検索したいキーワード入力  exclude:retweets",tweet_mode='extended',count=1500):
    try:
        tweet_data.append([tweet.id, tweet.user.screen_name, tweet.created_at, tweet.full_text.replace('\n',''), tweet.favorite_count, tweet.retweet_count, tweet.user.followers_count, tweet.user.friends_count])
    except Exception as e:
        print(e)
#出力するCSVファイルの名称を入力
with open('ファイル名称.csv', 'w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["id","user","created_at","text","fav","RT","follower","follows"])
    writer.writerows(tweet_data)
pass
