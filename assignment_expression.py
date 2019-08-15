#Now
some_list = [
    generate_expensive_element(value)
    for value in some_iterable 
        if meets_condition(generate_expensive_element(value))
    ]


#In python 3.8
some_list = [
    (elem := generate_expensive_element(value)) #Element gets memoized
    for value in some_iterable 
        if meets_condition(elem)
    ]
