#A nice alternative to map
squares = (x*x for x in values)

#Useful for filtering
even_squares = (x*x for x in values if x % 2 == 0)

#Can be iterated right away
for address in (a in addresses if 'wes' in a):
    print(address)

#Can be fed to builtins right away
{ x: x*x for x in values }
