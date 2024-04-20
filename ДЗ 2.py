import random 
def get_numbers_ticket(min_num, max_num, quantity):
    if not (1 <= min_num <= max_num <= 1000 and quantity <= max_num - min_num + 1):
        return []
    unique_numbers = set()
    while len(unique_numbers) < quantity:
        unique_numbers.add(random.randint(min_num, max_num))
    return sorted(list(unique_numbers))
numbers_random = get_numbers_ticket(1, 49, 6)
print('Ваші рандомні числа: ',numbers_random)