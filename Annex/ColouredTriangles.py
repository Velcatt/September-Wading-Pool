def excluded(c1, c2):
    li = ["R", "G", "B"]
    li.remove(c1)
    li.remove(c2)
    return li[0]


def nextrow(row):
    newrow = ""
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            newrow += row[i]
        else:
            newrow += excluded(row[i], row[i + 1])
    return newrow


def lastrow(row):
    if len(row) == 1:
        return row
    else:
        return lastrow(nextrow(row))


print(lastrow("RRGBRGBB"))
