def swap_case(s):
    string = ""
    for i in s:
        if i.isupper():
            string += (i.lower())
        else:
            string += (i.upper())
    return string


def split_join(string):
    a = string.split(" ")
    a = "-".join(a)
    return a


def mutable_string(string, position, character):
    lst = list(string)
    lst[position] = character
    string = "".join(lst)
    return string


def count_strings(string, substring):
    total = 0
    for i in range(len(string)):
        if string[i:len(string)].startswith(substring):
            total += 1
    return total


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_strings(string, sub_string)
    print(count)

    s = input("Enter your string")
    result = swap_case(s)
    print(result)

    line = input()
    result = split_join(line)
    print(result)

    stir = input()
    i, character = input()
    a = mutable_string(stir, i, character)
    print(a)


