



def find_max_joltage(bank: str):
    max_joltage = 0

    lenght = len(bank)
    for i in range(lenght - 1):
        first_batterie = bank[i]
        second_batterie = max(bank[i+1:], default='0')
        if second_batterie:
            joltage = int(first_batterie + second_batterie)
            if joltage > max_joltage:
                max_joltage = joltage

    return max_joltage


def main():

    overall_max_joltage = 0
    with open("input.txt", "r", encoding='utf8') as input:
        for line in input:
            overall_max_joltage += find_max_joltage(line.strip())

    print(overall_max_joltage)

if __name__ == "__main__":
    main()