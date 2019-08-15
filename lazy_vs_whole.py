import time
import random

possibles = [False, False, False, True, False, False]

class Expensive:
    def __init__(self, value=False):
        if value:
            self.value = value
        else:
            self.value = possibles[random.randint(0, len(possibles) - 1)]
        time.sleep(1)

def compute_all():
    start_time = time.time()
    whole_list = [Expensive(x) for x in possibles]
    for element in whole_list:
        if element.value:
            print('Found')
            break
    else:
        print('No elements found')
    end_time = time.time()
    print(f'took: {end_time - start_time}ms')

def generate_expensives(array):
    for elem in array:
        yield Expensive(elem)

def compute_until_true():
    start_time = time.time()
    for element in generate_expensives(possibles):
        if element.value:
            print('Found')
            break
    else:
        print('No elements found')
    end_time = time.time()
    print(f'took: {end_time - start_time}ms')

