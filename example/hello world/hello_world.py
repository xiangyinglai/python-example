#this program says hello and adks for my name.

def spam(input):
        try:
                return 42 / input
        except ZeroDivisionError:
                print('error: Invalid argument.')

print(spam(2))
print(spam(2),spam(3),spam(0))

