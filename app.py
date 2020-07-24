
def simple_loop():
    items = (3, 2, 1)
    for item in items:
        print(item)

def variable(var):
    while var > 0:
        var -= 1
        print('wow')

variable(int(input('choose number between 1-10: ')))