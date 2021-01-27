# def longest_substring(string):
#     substrings = []
#     substring = []
#     dicti = {}
#     i = 0
#     while i < len(string):
#         if string[i] not in substring:
#             substring.append(string[i])
#             print(substring)
#             dicti[string[i]] = i
#             i += 1
#         else:
#             substrings.append(substring)
#             i = dicti[string[i]] + 1
#             substring = []
#             dicti = {}

#     print(substrings)

# longest_substring("acbdeggdkdjfjffjklhkgfc")

class chaplain:
    def __init__(self, name, weekly_hours):
        self.name = name
        self.weekly_hours = weekly_hours
    



chaplain_one = chaplain("Dan", [0] * 7) 

print(chaplain_one.name, chaplain_one.weekly_hours)

chaplain_two = chaplain("Glen", [0] * 7) 

for i in range (0, len(chaplain_one.weekly_hours)):
    if i < 5:
        chaplain_one.weekly_hours[i] += 8
print(chaplain_one.weekly_hours)

for i in range (0, len(chaplain_two.weekly_hours)):
    if i < 5:
        chaplain_one.weekly_hours[i] += 6

weekly_total = [0] * 7
for i in range(0, 7):
    weekly_total[i] = chaplain_one.weekly_hours[i] + chaplain_two.weekly_hours[i]

print(weekly_total[0])
print("hello")


