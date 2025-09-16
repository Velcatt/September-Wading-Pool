def sevenate9(s):
    result = ""
    for i in range(len(s)):
        if i > 0 and s[i] == "9":
            if s[i - 1] != "7" or s[i + 1] != "7":
                result += "9"
        else:
            result += s[i]
    return result


print(sevenate9("79712312"))

print(sevenate9("7912312"))

print(sevenate9("79797"))
