from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from req import print_books, add_book, search_books
from connection import db_connection

"""Telegram token and bot username"""

TOKEN = '6329352245:AAFBCc3YzljEs5ppudJSvrY2wZNhXVp9o7U'
BOT_USERNAME = '@bbsherifmanager_bot'


collection = db_connection()
BIO = 0
LOCATION = 1


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Function handles the start of a bot conversation,
     greeting new users or addressing existing ones based on the presence of their data in the database."""
    user = update.message.from_user
    id = user.id
    name = user.first_name
    data = collection.find_one({"user_id": id})
    if not data:
        await update.message.reply_text('Hello there! I\'m Book Manager. What\'s up?')
        await update.message.reply_text("What's your location ?")
        return LOCATION
    else:
        await update.message.reply_text('Hello there ' + name)
        return BIO


async def location(update:Update, context: ContextTypes.DEFAULT_TYPE):
    """A second state, comes after start state for completing user's information"""
    context.user_data['location_name'] = update.message.text
    await update.message.reply_text("Tell me about yourself")
    return BIO


async def bio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stores the info about the user If not exist in the database."""

    user = update.message.from_user
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    bio_text = update.message.text
    location_text = context.user_data['location_name']

    user_data = collection.find_one({"user_id": user_id})

    if not user_data:
        user_document = {
            "user_id": user_id,
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "location": location_text,
            "bio": bio_text
        }
        collection.insert_one(user_document)
        await update.message.reply_text("Thank you! Feel free to interact with me " + first_name + " !!!")


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cancels and ends the conversation."""

    await update.message.reply_text(
        "Bye! I hope we can talk again some day.")
    return ConversationHandler.END


async def list_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """function lists users from a collection in the database, including their ID, username, first name,
     lastname, location and bio, and then sends the list as a reply to the user."""

    users = ""
    for s in collection.find():
        users += f"ID: {s['user_id']} \n" \
                 f"Username: {s['username']}\n " \
                 f"First name: {s['first_name']} \n" \
                 f"Last name: {s['last_name']}\n " \
                 f"Location: {s['location']}\n" \
                 f"info: {s['bio']}\n---------------------------------\n"
    if not users:

        await update.message.reply_text("Users not found.")
    else:
        await update.message.reply_text(users)


async def list_books(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Lists books and sends the formatted book data as a reply to the user by calling the print_books() function."""

    await update.message.reply_text(print_books())


async def book_adder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """function handles adding books to the bot's collection by extracting the title and author from the user input and
     calling the add_book() function. It then sends the result as a reply to the user."""

    input = update.message.text.split(' ')[1].split('-')
    addtitle = input[0]
    addauthor = input[1]
    await update.message.reply_text(add_book(addtitle,addauthor))


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Function performs a search for a book using the book's ID
    and then sends the search result as a reply to the user."""
    input_search = update.message.text.split(' ')[1]
    await update.message.reply_text(search_books(input_search))
