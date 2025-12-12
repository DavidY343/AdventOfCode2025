




def find_invalid_ids(id_range: str):

    start, end = id_range.split('-')
    n_start = int(start)
    n_end = int(end)

    total = 0
    while n_start <= n_end:
        
        start = str(n_start)

        if start[0] == '0':
            pass
        elif len(start) % 2 == 0:
            mitad = len(start) // 2
            first_half = start[:mitad]
            second_half = start[mitad:]
            if (int(first_half) == int(second_half)):
                total += n_start
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