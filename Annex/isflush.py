def isflush(hand):
    return (
        hand[0][-1] == hand[1][-1]
        and hand[0][-1] == hand[2][-1]
        and hand[0][-1] == hand[3][-1]
        and hand[0][-1] == hand[4][-1]
    )


print(isflush(["AS", "3S", "9S", "KS", "4S"]))
print(isflush(["AD", "4S", "7H", "KS", "10S"]))
print(isflush(["AS", "3S", "9S", "KS", "10S"]))
