import random


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