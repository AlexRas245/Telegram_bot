import random
from lexicon_ru import LEXICON_RU

def get_random_number() -> int:
    return random.randint(1, 100)


def get_num(file_t):
    with open(file_t, 'r') as f:
        start_num = int(f.read().strip())
    return start_num


def post_num(file_t, num):
    with open(file_t, 'w') as f:
        f.write(str(num))


def get_num_bot_choice():
    start = get_num('start.txt')
    end = get_num('end.txt')
    num = random.randint(start, end)
    post_num('last_num.txt', num)
    return num

def restart_data():
    post_num('end.txt', 100)
    post_num('start.txt', 1)


# Функция, возвращающая ключ из словаря, по которому
# хранится значение, передаваемое как аргумент - выбор пользователя
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
    return key


# Функция, возвращающая случайный выбор бота в игре
def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])

# Функция, определяющая победителя
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules = {'rock': 'scissors',
             'scissors': 'paper',
             'paper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    return 'bot_won'