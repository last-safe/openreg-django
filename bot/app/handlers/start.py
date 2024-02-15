from aiogram.types import (Message)
from aiogram.filters.command import (CommandStart)
from aiogram import (F, Bot)

from .. import router, logger
from app.models import Users
from ..keyboards.info import main as info_kb
from ..functions.image import get_path

@router.message(CommandStart(), F.chat.type == "private")
async def start_func(m: Message, bot: Bot) -> None:

    target_user = await Users.objects.filter(telegram_id=m.from_user.id).afirst()

    if (target_user):
        logger.info("cancel")
        target_user.image_telegram_path = await get_path(m, bot)
        await target_user.asave()
        return await m.answer("cancel", reply_markup = await info_kb())


    data = {k: v 
        for k, v in zip(m.from_user.dict(), m.from_user.dict().values())
        if k in map(lambda x: x.name, Users._meta.fields)
    }

    
    data["telegram_id"] = data.pop("id")

    await Users(**data, image_telegram_path = await get_path(m, bot)).asave()
    logger.success("New user")
    
    return await m.answer("successful", reply_markup = await info_kb())