from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def main():
    return ReplyKeyboardMarkup(
        input_field_placeholder="Отправь доп. информацию!!!",
        resize_keyboard=True,
        keyboard=[
            [ KeyboardButton(text="Телефон", request_contact=1) ]
        ]
    )