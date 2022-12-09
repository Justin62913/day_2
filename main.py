# This opens the data.txt file and reads it line by line.
with open('data.txt') as file:
    data = [line for line in file.read().strip().split('\n')]
# print(data)

# A for Rock = 1, B for Paper = 2, C for Scissors = 3.
# X = lose 0, Y = draw 3, Z = win 6.
game_1 = {

}
game = {
    "A X": 3, "A Y": 4, "A Z": 8,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 2, "C Y": 6, "C Z": 7,
}

total_points = 0
for item in data:
    total_points += game[item]

print(total_points)

