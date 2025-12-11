max_dial = 100


def password_decoder(line: str, dial_pos, times_at_zero):
    #Assuming the line has a fixed format like L53
    dir = line[0]
    move = int(line[1:])

    
    if dir == "L":
        dial_pos = (dial_pos - move) % max_dial
    elif dir == "R":
        dial_pos = (dial_pos + move) % max_dial
    
    if dial_pos == 0:
        times_at_zero += 1
    
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