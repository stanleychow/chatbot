from random import choice

def get_bot_response(user_response):
    bot_response_yes = ["happy coding!", "have fun!", "hello world!"]
    bot_response_no = ["take a break!", "maybe next time!"]
    
    if user_response == "yes":
        return choice(bot_reponse_yes)
    elif user_response == "no":
        return choice(bot_response_no)
    else:
        return "See you later!"

