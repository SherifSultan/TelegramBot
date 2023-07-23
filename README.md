# TelegramBot
The Telegram bot acts as a book manager by starting a conversation with it. The bot starts checking whether your data exists in the database or not. The bot is using MongoDB as storage for user data. If you already introduced yourself, the bot should welcome you with your actual profile name; if not, the bot will ask you to provide information about yourself. Moreover, the Telegram bot has some commands that can be used for certain actions. The commands are detailed in retriving user data if found in the database, retrieving books details from an API (title only retrieved), adding a book by providing its title and author, and a command that searches for the created book by its ID.

### Prerequisites


To run the project, you will need to install some packages:

* pip install python-telegram-bot

* pip install requests

* pip install pymongo


### Quick Start

1- Run the project through "main.py" python file

2- Open telegram across laptop/mobile and search for " @bbsherifmanager_bot "

![Capture](https://github.com/SherifSultan/TelegramBot/assets/122619738/61491379-09bd-4669-a4f0-1aa0c60bb3f0)

3- Start the conversation with the bot and interact with the following mentioned commands in "usage" topic.

![Capture2](https://github.com/SherifSultan/TelegramBot/assets/122619738/d799bd40-821c-4ed4-8499-4e4461a77280)


## Usage

/start                         ---> to start a conversation with the bot

/cancel                        ---> end the conversation with the bot

/listusers                     ---> retreive the users who are stored in the database

/listbooks                     ---> retrieve books from an API

/addbook {title}-{author}      ---> add a book by setting its title and author

/search {bookID}               ---> retrieve an added book by its ID
