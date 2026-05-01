import random

def main():
    dice_sides = int(input("How many sides does your dice have? "))
    roll = random.randint(1,dice_sides)
    print(f"Your roll is {roll}")

if __name__ == '__main__':
    main()