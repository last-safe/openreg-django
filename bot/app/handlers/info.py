from aiogram.types import (Message)
from aiogram import (F)

from .. import router, logger
from app.models import Users


@router.message(F.contact, F.chat.type == "private")
async def on_user_shared(m: Message):
    target_user = await Users.objects.aget(telegram_id=m.from_user.id)
    target_user.phone = m.contact.phone_number
    await target_user.asave()

    logger.success("save phone")
    return await m.answer("zbs")