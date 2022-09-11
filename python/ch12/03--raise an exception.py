def inc(num):
    try:
        return int(num) + 1

    except:
        raise ValueError ('Error')

# a=inc(5)
a=inc('uyt')

print(a)
     








