from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon_ru import LEXICON_RU
from keyboards import game_start_kb
router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                         reply_markup=game_start_kb)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=game_start_kb)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='cancel'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/cancel'], reply_markup=game_start_kb)