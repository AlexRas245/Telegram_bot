from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon_ru import LEXICON_RU
from keyboards import game_start_kb, game1_step_kb, game1_kb, game1_1_kb, game1_2_kb, yes_no_kb1
from services import get_num, post_num, get_random_number, get_num_bot_choice

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


# Этот хэндлер срабатывает на выбор игры Угадай число
@router.message(F.text == LEXICON_RU['game1'])
async def game_1(message: Message):
    await message.answer(text=LEXICON_RU['yes1_1'], reply_markup=game1_step_kb)


# Этот хэндлер срабатывает на согласие пользователя играть в игру
@router.message(F.text == LEXICON_RU['yes_button1'])
async def process_yes1_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes1_1'], reply_markup=game1_step_kb)


# Этот хэндлер срабатывает на выбор кто загадывает число в Угадай число
@router.message(F.text.in_(['Я загадываю', 'Ты загадываешь']))
async def process_game_button1_1(message: Message):
    if message.text == 'Я загадываю':
        await message.answer(text=LEXICON_RU['yes1'], reply_markup=game1_kb)
    elif message.text == 'Ты загадываешь':
        await message.answer(text=LEXICON_RU['Ты загадываешь'], reply_markup=game1_2_kb)
        num = get_random_number()
        post_num('num_bot.txt', num)


# Этот хэндлер будет срабатывать на отправку пользователем чисел от 1 до 100
@router.message(F.text.in_([f'0{num}' if num < 10 else str(num) for num in range(1, 101)]))
async def process_numbers_answer(message: Message):
    ans = int(get_num('num_bot.txt'))
    num_user = int(message.text)
    if ans == num_user:
        await message.answer(text=LEXICON_RU['user_guessed'], reply_markup=yes_no_kb1)
    elif ans > num_user:
        await message.answer(text=LEXICON_RU['user_less'], reply_markup=game1_2_kb)
    elif ans < num_user:
        await message.answer(text=LEXICON_RU['user_unless'], reply_markup=game1_2_kb)


# Этот хэндлер срабатывает на любую из игровых кнопок
@router.message(F.text.in_(['Загадал', 'Больше', 'Меньше', 'Ты угадал!']))
async def process_game_button1(message: Message):
    if message.text == 'Загадал':
        await message.answer(text=f'{LEXICON_RU["Загадал"]}')
        bot_choice = get_num_bot_choice()
        await message.answer(text=f'{LEXICON_RU["bot_ans"]} - {bot_choice}?', reply_markup=game1_1_kb)
    elif message.text == 'Больше':
        last_num = get_num('last_num.txt')
        post_num('start.txt', last_num)
        await message.answer(text=f'{LEXICON_RU["Больше"]}')
        bot_choice = get_num_bot_choice()
        await message.answer(text=f'{LEXICON_RU["bot_ans"]} - {bot_choice}?', reply_markup=game1_1_kb)
    elif message.text == 'Меньше':
        last_num = get_num('last_num.txt')
        post_num('end.txt', last_num)
        await message.answer(text=f'{LEXICON_RU["Больше"]}')
        bot_choice = get_num_bot_choice()
        await message.answer(text=f'{LEXICON_RU["bot_ans"]} - {bot_choice}?', reply_markup=game1_1_kb)
    elif message.text == 'Ты угадал!':
        await message.answer(text=f'{LEXICON_RU["Ты угадал!"]}', reply_markup=yes_no_kb1)
