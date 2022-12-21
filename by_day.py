import json

with open('table.json', 'r') as fin:
    t = fin.read()
stats = json.loads(t)

def process(cday, task):
    best_time, pen_time = 10**20, 10**20
    records = []
    for _, member in stats['members'].items():
        for day, solutions in member['completion_day_level'].items():
            if int(day) != cday:
                continue
            if task in solutions:
                pen_time = solutions[task]['get_star_ts']
                records.append([pen_time, member['name'], member['id']])
            best_time = min(best_time, pen_time)
    return [[round((x[0] - best_time) / 60, 2), x[1], x[2]] for x in sorted(records)[:5]]


for cday in range(30):
    for task in ['1', '2']:
        res = process(cday, task)
        if len(res) == 0:
            continue
        print(cday, task, res)
    print()