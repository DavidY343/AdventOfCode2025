




def find_invalid_ids(id_range: str):

    start, end = id_range.split('-')
    n_start = int(start)
    n_end = int(end)

    total = 0
    id_invalid = False
    while n_start <= n_end:
        
        start = str(n_start)

        if start[0] == '0':
            id_invalid = False
        else: 
            length = len(start)

            for long_patron in range(1, length // 2 + 1):
                if length % long_patron == 0:
                    patron = start[:long_patron]
                    repetitions = length // long_patron
                    if patron * repetitions == start and repetitions > 1:
                        id_invalid = True
                        break

        if id_invalid == True:
            total += n_start
        id_invalid = False
        n_start += 1

    return total
def main():

    total_acumulative = 0
    with open("input.txt", "r", encoding='utf8') as input:
        for line in input:
            id_ranges = line.strip().split(',')
            for id_range in id_ranges:
                total_acumulative += find_invalid_ids(id_range)

    print(total_acumulative)

if __name__ == "__main__":
    main()