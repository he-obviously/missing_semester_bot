import random

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

jokes = [
    'В театре была заложена бомба реагирующая на громкий шум. По окончанию спектакля зрительный зал взорвался аплодисментами.',
    'Фотограф снимал целый день и всю ночь смотрел целый день.',
    'Влюблённая пара стояла у пылесоса. Потом они засосались.',
    'Группа «микроволновка» никак не может стать хедлайнером, потому что на всех концертах выступает всегда на разогреве.',
    'Мама дала денег на дорожку. Хватило на две.'
]

photos = [
    'https://avatars.mds.yandex.net/i?id=48347fc2f4e0dc2bf24955f4b9eb5a901b30321a-5279994-images-thumbs&n=13',
    'https://avatars.mds.yandex.net/i?id=7eb28ccbaec1c8193b1c83ce361bbc38cfa096ec-6071858-images-thumbs&n=13',
    'https://avatars.mds.yandex.net/i?id=da05761ef91b647ef743811add20ab6b5f4984d2-8210620-images-thumbs&n=13',
    'https://avatars.mds.yandex.net/i?id=f789be89541898da7e0a578d3cca35b5f8af6b14-7662004-images-thumbs&n=13',
    'https://pbs.twimg.com/media/FDJn0LzXoAAOAw7.jpg'
]

videos = [
    'BAACAgIAAxkBAAMkY6bLZFYamAx_kyUVpyYdQNghRcsAAtgqAALsyTFJLeyox2_AtBUsBA',
    'BAACAgIAAxkBAAMlY6bLe8aSOHb_7NyyOa4kbDAQhk0AAiQhAAJwOiBJVBd18m11SsosBA',
    'BAACAgIAAxkBAAMmY6bLkV1-4ROtamQFkAY5yKr-EpEAAi4lAAKsHwlJT74S5xPxsessBA',
    'BAACAgIAAxkBAAMnY6bLojd8_q5mJs_c6XG46NjDkB0AAs0jAAKsHwFJ0ytv-fi26pgsBA',
    'BAACAgIAAxkBAAMoY6bLv8VAiE3-oLf7GSPrzzqCAAGkAAK-IgACvHI5SQABed1Qr3qorCwE'
]

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("/joke - получить рандомный каламбур,\n/photo - получить рандомную пикчу,\n/video - получить рандомный тикток")

@dp.message_handler(commands=['joke'])
async def process_joke_command(message: types.Message):
    await message.reply(random.choice(jokes))

@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    await bot.send_photo(message.chat.id, photo=random.choice(photos))

@dp.message_handler(commands=['video'])
async def process_video_command(message: types.Message):
    await bot.send_video(message.chat.id, video=random.choice(videos))

@dp.message_handler(content_types='text')
async def wrong_message(message: types.Message):
    await message.reply("эээ, слыш, такой команды нет.\n/help - список команд")

if __name__ == '__main__':
    executor.start_polling(dp)