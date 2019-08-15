#All the even natural numbers
def all_even():
    n = 0
    while True:
        yield n
        n += 2

#Circular lists
def circular(start,end):
    current = start
    while True:
        yield current
        if current == end:
           current = start
        else:
           current += 1
