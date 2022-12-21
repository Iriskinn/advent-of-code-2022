with open('input.txt', 'r') as fin:
    t = fin.read().split('\n')[:-1]

fout = open('prep_input.txt', 'w')
fout.write(str(len(t)) + '\n')
for tt in t:
    tt = tt.replace(' valve ', ' valves ').replace('tunnel ', 'tunnels ').replace(' leads ', ' lead ')
    print(tt.split('; tunnels lead to valves '))
    c = len(tt.split('; tunnels lead to valves ')[1].split(', '))
    tt = tt.replace('Valve ', '').replace(' has flow rate=', ' ').split('; tunnels lead to valves ')
    fout.write(tt[0] + ' ' + str(c) + ' ' + ' '.join(tt[1].split(', ')) +  '\n')

fout.close()