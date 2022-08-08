# Instagram Automation Using Python

from instabot import Bot

bot = Bot()
bot.login(username=" ",password=" ") #paste username & password

#bot.follow(' ') # follow people (paste their username)

#bot.upload_photo(" ",caption = " ") # image path and caption if you want

#bot.unfollow('') # unfollow people (paste their username)


# Mesage with help of Bot

#bot.send_message(" ", [" "," "]) # ("Write message", ["username","username",......])


#followers list

# followers = bot.get_user_followers(" ") #username

# for follower in followers:
#     print(bot.get_user_info(follower))
    
#following list

# following = bot.get_user_following(" ") #username

# for Following in following:
#     print(bot.get_user_info(following))    


# Yash Sanjeev Halwai