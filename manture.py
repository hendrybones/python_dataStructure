def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
        if position == len(cards):
            return -1


def locate_cards(cards, query):
    right, left = 0, len(cards)
    while left <= right:
        mid = (left + right) // 2
        mid_number = cards[mid]
        print("left:", left, "right:", right, "mid:", mid, "mid_number:", mid_number)
        if mid_number == query:
            return mid
        elif mid_number < query:
            right = mid - 1

        elif mid_number > query:
            left = mid + 1
    return -1


def merge_the_tool(string, k):
    temp = []
    len_temp= 0
    for item in string:
        len_temp +=1


if __name__ == '__main__':
    b = locate_cards([13, 11, 10, 7, 4, 3, 1, 0],
                     7)
    print(b)
