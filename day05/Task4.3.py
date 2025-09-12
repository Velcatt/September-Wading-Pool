meetings = [
    [" Monday ", " 3:30 PM ", "Joe", "Sam"],
    [" Monday ", " 4:30 PM ", "Bob", "Alice"],
    [" Tuesday ", " 3:30 PM ", "Joe", "Bob", "Alice", "Sam"],
    [" Tuesday ", " 9:30 AM ", "Joe", "Bob"],
]

name = input("Enter a name : ")
meetinglist = []
for instance in meetings:
    if name in instance:
        meetinglist += (instance[0], instance[1])

print(meetinglist)
