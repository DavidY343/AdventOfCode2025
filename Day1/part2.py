max_dial = 100


def count_crossings(dial_pos, move, dir):

    if dir == "R":
        first_k = (max_dial - dial_pos) % max_dial
    else:  # "L"
        first_k = dial_pos % max_dial

    if first_k == 0:
        first_k = max_dial

    if move < first_k:
        return 0

    return 1 + (move - first_k) // max_dial


def password_decoder(line: str, dial_pos, times_at_zero):
    #Assuming the line has a fixed format like L53
    dir = line[0]
    move = int(line[1:])

    

    crossings = count_crossings(dial_pos, move, dir)
    times_at_zero += crossings
    if dir == "L":
        dial_pos = (dial_pos - move) % max_dial
    elif dir == "R":
        dial_pos = (dial_pos + move) % max_dial
    

    
    
    return dial_pos, times_at_zero

def main():
    
    dial_pos = 50
    times_at_zero = 0
    with open("input.txt", "r", encoding='utf-8') as input:
        for line in input:
            dial_pos, times_at_zero = password_decoder(line.strip(), dial_pos, times_at_zero)
    return times_at_zero
    
if __name__ == "__main__":
    times_at_zero = main()

    print(times_at_zero)