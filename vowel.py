
def minion_game(string: str) -> None:
    length = len(string)
    kevin_score = 0
    stuart_score = 0

    for i, char in enumerate(string):
        points = length - i
        if char in {"A", "E", "I", "O", "U"}:
            kevin_score += points
        else:
            stuart_score += points

    # Determine the winner
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("It's a tie!")


if __name__ == '__main__':
    s = input()
    minion_game(s)