def locate_card(cards, query):
    position = 0
    while True:
        if cards[position] == query:
            return position
        position +=1
        if position ==len(cards):
            return -1


if __name__ == '__main__':
    b = locate_card(cards=[13, 11, 10, 7, 4, 3, 1, 0],
                    query=7)
    print(b)
