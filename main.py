from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, Application, ConversationHandler
import commands


def main() -> None:
    """Run the bot"""
    # Creating the Application and passing bot's token.
    application = Application.builder().token(commands.TOKEN).build()

    """Conversation handler with an entry point for the /start command,
     a state for the user to input their bio, and a fallback for the "/cancel command to end
     the conversation"""

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", commands.start)],
        states={
            commands.LOCATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, commands.location)],
            commands.BIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, commands.bio)]
        },
        fallbacks=[CommandHandler("cancel", commands.cancel)],
    )

    application.add_handler(conv_handler)
    application.add_handler(CommandHandler('listusers', commands.list_user))
    application.add_handler(CommandHandler('listbooks',commands.list_books))
    application.add_handler(CommandHandler('addbook', commands.book_adder))
    application.add_handler(CommandHandler('search', commands.search))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()