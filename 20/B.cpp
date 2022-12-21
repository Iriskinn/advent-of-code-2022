#include <bits/stdc++.h>
using namespace std;

const int N = 1e4;

int n;
long long a[N];
int ind[N], st_pos[N];

int sign(long long x) {
	if (x < 0)
		return -1;
	else if (x > 0)
		return +1;
	else
		return 0;
}

void shift(int i) {
	long long v = abs(a[i]);
	int d = sign(a[i]);
	for (int j = 0; j < v % (n - 1); j++) {
		int x = (i + j*d + n) % n, y = (i + (j+1)*d + n) % n;
		swap(a[x], a[y]);
		swap(st_pos[x], st_pos[y]);
		ind[st_pos[x]] = x;
		ind[st_pos[y]] = y;
	}
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		a[i] *= 811589153ll;
		st_pos[i] = i, ind[i] = i;
	}
	
	for (int k = 0; k < 10; k++)
		for (int i = 0; i < n; i++)
			shift(ind[i]);

	int zp = 0;
	while (a[zp] != 0) zp++;
	cout << a[(zp + 1000) % n] + a[(zp + 2000) % n] + a[(zp + 3000) % n] << endl;

    return 0;
}