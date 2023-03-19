a = input().upper()
collector = {i:0 for i in a}
for i in a:
    collector[i] += 1

most = 0
for i in collector:
    if collector[i] > most:
        most = collector[i]

most_array = [i for i in collector if collector[i] == most]
if len(most_array) == 1:
    print(most_array[0])
else:
    print('?')