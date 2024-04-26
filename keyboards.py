from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon_ru import LEXICON_RU
from config import games_list

# --------- Старт ------------
# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем список с кнопками
buttons: list[KeyboardButton] = [
    KeyboardButton(text=f'{game}') for game in games_list
]
kb_builder.row(*buttons, width=2)
game_start_kb: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем список с кнопками
buttons: list[KeyboardButton] = [
    KeyboardButton(text=f'Я загадываю'),
    KeyboardButton(text=f'Ты загадываешь'),
    KeyboardButton(text=f'Выйти из игры')
]
kb_builder.row(*buttons, width=2)
game1_step_kb: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем список с кнопками
buttons: list[KeyboardButton] = [
    KeyboardButton(text=f'Загадал'),
    KeyboardButton(text=f'Выйти из игры')
]
kb_builder.row(*buttons, width=2)
game1_kb: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем список с кнопками
buttons: list[KeyboardButton] = [
    KeyboardButton(text=f'Больше'),
    KeyboardButton(text=f'Меньше'),
    KeyboardButton(text=f'Ты угадал!'),
    KeyboardButton(text=f'Выйти из игры')
]
kb_builder.row(*buttons, width=2)
game1_1_kb: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем список с кнопками
buttons: list[KeyboardButton] = [
    KeyboardButton(text=f'0{num}') for num in range(1, 10)] + [
    KeyboardButton(text=f'{num}') for num in range(10, 101)] + [
    KeyboardButton(text='Выйти из игры')
]
kb_builder.row(*buttons, width=10)
game1_2_kb: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

# Создаем кнопки игровой клавиатуры
button_1 = KeyboardButton(text=LEXICON_RU['rock'])
button_2 = KeyboardButton(text=LEXICON_RU['scissors'])
button_3 = KeyboardButton(text=LEXICON_RU['paper'])
button_4 = KeyboardButton(text=f'Выйти из игры')
# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
game2_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1],
              [button_2],
              [button_3],
              [button_4]],
    resize_keyboard=True
)

button_yes = KeyboardButton(text=LEXICON_RU['yes_button1'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb1: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# Создаем кнопки с ответами согласия и отказа
button_yes = KeyboardButton(text=LEXICON_RU['yes_button2'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb2: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)