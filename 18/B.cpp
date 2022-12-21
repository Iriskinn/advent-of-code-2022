#include <bits/stdc++.h>
using namespace std;

const int N = 3000, D = 40;

int n, res = 0;
int used[D][D][D];
int x[N], y[N], z[N];
int dx[] = {-1, 1, 0, 0, 0, 0},
    dy[] = {0, 0, -1, 1, 0, 0},
    dz[] = {0, 0, 0, 0, -1, 1};


bool valid(int x, int y, int z) {
    return 0 <= x && x < D && 0 <= y && y < D && 0 <= z && z < D;
}

void dfs(int cx, int cy, int cz) {
    used[cx][cy][cz] = 2;
    for (int i = 0; i < 6; i++) {
        int nx = cx + dx[i], ny = cy + dy[i], nz = cz + dz[i];
        if (valid(nx, ny, nz) && used[nx][ny][nz] == 0)
            dfs(nx, ny, nz);
    }
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		scanf("%d,%d,%d\n", x + i, y + i, z + i);
		x[i] += 10, y[i] += 10, z[i] += 10;
		used[x[i]][y[i]][z[i]] = 1;
	}
	dfs(0, 0, 0);
	for (int i = 0; i < n; i++) {
        for (int j = 0; j < 6; j++) {
            int nx = x[i] + dx[j], ny = y[i] + dy[j], nz = z[i] + dz[j];
            if (valid(nx, ny, nz) && used[nx][ny][nz] == 2)
                res++;
        }
	}
	cout << res << endl;
 	return 0;
}