


def get_maxes(input):

    i = 0
    j = 0
    for line in input:
        if i == 0:
            line = line.strip()
            for c in line:
                j += 1
        i += 1

    return i, j

def count_neighbours(cell, i, j):
    pass

def solve_puzzle(input):

    max_height, max_width = get_maxes(input)
    i, j = 0
    print(max_height, max_width)
    for line in input:
        for c in line:
            neighbours = count_neighbours(c, i, j, in)



def main():

    accesible_roll_papers = 0
    with open("dummy.txt", "r", encoding='utf8') as input:
        print(input)
        accesible_roll_papers = solve_puzzle(input)

    print(accesible_roll_papers)


if __name__ == "__main__":
    main()