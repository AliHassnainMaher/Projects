import random

dice_patterns = {
    1: ["     ",
        "  *  ",
        "     "],
    2: ["*    ",
        "     ",
        "    *"],
    3: ["*    ",
        "  *  ",
        "    *"],
    4: ["*   *",
        "     ",
        "*   *"],
    5: ["*   *",
        "  *  ",
        "*   *"],
    6: ["*   *",
        "*   *",
        "*   *"]
}

def roll_dice():
    return random.randint(1, 6)

def print_dice_pattern(number):
    pattern = dice_patterns[number]
    for line in pattern:
        print(line)

if __name__ == "__main__":
    while True:
        input("Press Enter to roll the dice...")
        result = roll_dice()
        print(f"You rolled a {result}!")
        print_dice_pattern(result)
        if input("Roll again? (y/n): ").lower() != 'y':
            break