from loader import dp, bot
from aiogram.types import ContentType, Message
from pathlib import Path


download_path = Path().joinpath("downloads","caterogies")
download_path.mkdir(parents=True, exist_ok=True)

@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handler(message: Message):
    await message.document.download(destination=download_path)
    doc_id = message.document.file_id
    await message.reply("Siz hujjat yubordingiz!\n"
                        f"file_id = {doc_id}")

    @dp.message_handler(content_types='video')
    async def video_handler(message: Message):
        await message.video.download(destination=download_path)
        await message.reply("Video qabul qilindi\n"
                            f"file_id = {message.video.file_id}")

    @dp.message_handler(content_types='photo')
    async def video_handler(message: Message):
        await message.photo[-1].download(destination=download_path)
        await message.reply("Rasm qabul qilindi\n" )
