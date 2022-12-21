import json

with open('table.json', 'r') as fin:
    t = fin.read()
stats = json.loads(t)

data = []
begin_day, end_day = 0, 30
best_stars = -1
best_time = 0

for id, member in stats['members'].items():
    stars = 0
    pen_time = 0
    for day, solutions in member['completion_day_level'].items():
        if int(day) < begin_day or int(day) > end_day:
            continue
        for task in ['1', '2']:
            if task in solutions:
                pen_time += solutions[task]['get_star_ts']
                stars += 1
    data.append([stars, pen_time, member['name'], member['id']])
    if best_stars < member['stars']:
        best_stars = member['stars']
        best_time = pen_time
    elif best_stars == member['stars']:
        best_time = min(best_time, pen_time)

data.sort(key=lambda x: (-x[0], x[1]))
for i, x in enumerate(data[:20]):
    print(i + 1, x[0], round((x[1] - best_time) / 60, 2), x[2], x[3])