def open_file(file):
    lines = open(file,'r').read().split()
    return lines

# +8117696,0.83
def number_and_cost(string_array):
    pairs = []
    for string in string_array:
        string = string[1:len(string)]
        pair = string.split(',')
        pairs.append((pair[0], pair[1]))

    return pairs



if __name__ == '__main__':
    data = open_file('route-costs-1000000.txt')
    number_and_cost(data)
