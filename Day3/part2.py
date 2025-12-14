



def max_joltage_12(bank: str):
    max_joltage = 0

    k = 12
    length = len(bank)
    to_eliminate = length - k

    stack = []

    for i in range(length):

        while stack and (bank[i] > stack[-1]) and to_eliminate:
            stack.pop()
            to_eliminate -= 1

        stack.append(bank[i])
    
    joltage_str = ''.join(stack[:k])
    max_joltage = int(joltage_str)
    return max_joltage

        
        

    return max_joltage


def main():

    overall_max_joltage = 0
    with open("input.txt", "r", encoding='utf8') as input:
        for line in input:
            overall_max_joltage += max_joltage_12(line.strip())

    print(overall_max_joltage)

if __name__ == "__main__":
    main()