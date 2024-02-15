from aiogram.types.photo_size import PhotoSize
from aiogram.types import (Message)
from aiogram import (Bot)

async def get_path(m: Message, bot: Bot) -> str:
    profile_photos = await bot.get_user_profile_photos(m.from_user.id)
    photo: PhotoSize = profile_photos.photos[0][-1]
    file = await bot.get_file(photo.file_id)
    return file.file_path