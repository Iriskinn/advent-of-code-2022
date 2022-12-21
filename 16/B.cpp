#include <bits/stdc++.h>
using namespace std;

const int N = 60;
const int T = 27;

int n, m;
vector < int > g[N];
map < string, int > num;
int nzn[N];
int cntr = 0, nzcntr = 0;
int val[100];
map < int, map < int, int > > dp[1<<16][T];
int best = 1474; // part 1 solution


int proc(int mask, int v, int v2, int t, int acc) {
	if (dp[mask][t].count(v) != 0 && dp[mask][t][v].count(v2) != 0) {
		return dp[mask][t][v][v2];
    }
    if (t == 0) {
		if (acc > best) {
			best = acc;
			cout << best << endl;
		}
		dp[mask][t][v][v2] = 0;
		return 0;
	}

    int best_add = 0;
    for (int i = 0; i < cntr; i++)
        if (val[i] > 0 && (mask & (1 << nzn[i])) == 0)
            best_add += val[i] * (t-1);
    if (acc + best_add < best) {
        dp[mask][t][v][v2] = 0;
        return 0;
    }

	int res = 0;
    if (v != v2 && val[v] != 0 && val[v2] != 0 && ((mask & (1 << nzn[v])) == 0) && ((mask & (1 << nzn[v2])) == 0)) {
        res = proc(mask + (1 << nzn[v]) + (1 << nzn[v2]), v, v2, t-1, acc + val[v]*(t-1) + val[v2]*(t-1))  + val[v]*(t-1) + val[v2]*(t-1);
    }
	if (val[v] != 0 && ((mask & (1 << nzn[v])) == 0)) {
        for (int i = 0; i < g[v2].size(); i++) {
            int w2 = g[v2][i];
            res = max(res, proc(mask + (1 << nzn[v]), v, w2, t-1, acc + val[v]*(t-1)) + val[v]*(t-1));
        }
	}
    if (val[v2] != 0 && ((mask & (1 << nzn[v2])) == 0)) {
        for (int i = 0; i < g[v].size(); i++) {
            int w = g[v][i];
            res = max(res, proc(mask + (1 << nzn[v2]), w, v2, t-1, acc + val[v2]*(t-1)) + val[v2]*(t-1));
        }
    }
    for (int i = 0; i < g[v].size(); i++) {
        for (int j = 0; j < g[v2].size(); j++) {
            int w = g[v][i], w2 = g[v2][j];
            res = max(res, proc(mask, w, w2, t-1, acc));
        }
    }

	dp[mask][t][v][v2] = res;
	return res;
}

int get_num(string v) {
	if (num.count(v) == 0)
		num[v] = cntr++;
	return num[v];
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		string v, w;
		cin >> v;
		cin >> val[get_num(v)];
		cin >> m;
		for (int j = 0; j < m; j++) {
			cin >> w;
			g[get_num(v)].push_back(get_num(w));
		}
	}

	for (int i = 0; i < cntr; i++)
		if (val[i] > 0)
			nzn[i] = nzcntr++;

	cout << proc(0, get_num("AA"), get_num("AA"), 26, 0) << endl;

	return 0;
}
