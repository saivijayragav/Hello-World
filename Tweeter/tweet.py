# Importing Modules/Libraries
import tweepy
import time

# Credentials (Insert your keys and tokens below)
api_key = "j18sAlk5TV5hReg5eraHpSIbs"
api_secret = "c5qQqj4rFIXQpd7CmJRsPaCC8TiF3eRKErFwuPVrjOrachttbx"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAANCIoAEAAAAAxJMHjQGWTMRMrxkpCQrmq%2B5Tgvw%3DfKcg350KT0BHJnuYFktg2j8mJ5KJuFO5bMV2MyFfmBtSSCGYJ3"
access_token = "1668244310536622081-g1qbvQ8rjkDWfPLHWlppXcTmqF3Y4R"
access_token_secret = "YGuAObwBbwDhVZzMEvthEJHC6Ip3jJwGtT5zZfOYwQXJB"

# Connecting to Twitter API
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

file = open("harrypotter3.txt", 'r', encoding="utf-8")
f = file.readlines()

i = 1
l = 1
head = "The Philosopher's Stone CH-1 Lines of 551 lines\n"
while i < len(f):
    message = ""

    if f[i][:5] == "Book:":
    
        if l-1 != int(head[-11:-1][:4]):
            print("false", i)
        head = f[i][5:]
        l = 1
        i += 1
    else:
        c = 0
        for j in range(3):
            if i + j < len(f) and f[i + j][:5] != "Book:":
                cond1 = j == 0 and l == 1
                if cond1 or len(f[i + j]) <= 1:
                    message += f[i + j]
                else:
                    message += f[i + j].strip() + " " 
                c += 1
            else: 
                break
        
        if c == 1:
            head2 = head.replace("Lines", "Line " + str(l))
        else:
            head2 = head.replace("Lines", "Lines " + str(l) + '-' + str(l + c - 1))

        message = head2 + '\n' + message
        print(message)
        if i + j < len(f) and f[i + j][:5] != "Book:":
            i += 1
            l += 1
        i += j
        l += j
    if i > 555:
        break
    