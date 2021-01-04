import tweepy
import csv

key_word=input('検索したいキーワードを入力してください')
number=input('取得件数を入力してください')
file_name=input('結果出力するCSVファイルの名前を入力してください')
number=int(number)

CONSUMER_KEY = "取得したーキーを入力"
CONSUMER_SECRET = "取得したーキーを入力"
ACCESS_TOKEN = "取得したーキーを入力"
ACCESS_SECRET = "取得したーキーを入力"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

tweet_data = [] #取得したツイートを格納するリスト

for tweet in api.search(q='{}'.format(key_word),tweet_mode='extended',count=number):
    try:
        tweet_data.append([tweet.id, tweet.user.screen_name, tweet.created_at, tweet.full_text.replace('\n',''), tweet.favorite_count, tweet.retweet_count, tweet.user.followers_count, tweet.user.friends_count])
    except Exception as e:
        print(e)

with open('{}.csv'.format(file_name), 'w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["id","user","created_at","text","fav","RT","follower","follows"])
    writer.writerows(tweet_data)
pass

print('出力件数:')
print(len(tweet_data))
