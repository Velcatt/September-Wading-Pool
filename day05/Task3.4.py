numbers = {
    " dalmatians ": 101,
    " pi ": 3.14,
    " beast ": 3 * 2 * 111,
    " life ": 42,
    " googol ": 10 ^ 100,
}

result = ""
highest = 0
for key in numbers:
    if numbers[key] > highest:
        result = key
print(result)
