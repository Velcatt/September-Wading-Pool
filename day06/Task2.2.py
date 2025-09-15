def palindrome(text=""):
    if text == "":
        text = input("Enter a text : ")
        text = (
            text.lower()
            .replace(".", "")
            .replace(" ", "")
            .replace(",", "")
            .replace("'", "")
        )
        return palindrome(text)
    elif text[0] == text[-1] and len(text) < 3:
        return True
    elif text[0] == text[-1]:
        return palindrome(text[1 : len(text) - 1])
    else:
        return False


print(palindrome())
