#include <iostream>

int power_level (int x, int y, int serial)
{
	int p = (y*(x+10)+serial)*(x+10);
	p = ((int)(p/100)) % 10;
	return p-5;
}

int* build_grid (int serial, int n)
{
	int* grid = new int [n*n];
	for (int i=0; i<n; ++i)
		for (int j=0; j<n; ++j)
			grid[i+j*n] = power_level(i+1, j+1, serial);
	return grid;
}

int find_max (int* g, int g_size, int n, int& spot_x, int& spot_y)
{
	int max_p = 0;
	int x, y, i, j, p;
	for (x = 0; x < g_size-n; ++x)
		for (y = 0; y < g_size-n; ++y)
		{
			p = 0;
			for (i = 0; i < n; ++i)
				for (j = 0; j<n; ++j)
					p += g[(x+i) + (y+j) * g_size];
			if (p > max_p)
			{
				max_p = p;
				spot_x = x;
				spot_y = y;
			}
		}
	std::cout << "func: max for " << n << " is " << max_p << " at " << spot_x << " " << spot_y << std::endl;
	return max_p;
}

int find_all_max (int* g, int g_size, int& spot_x, int& spot_y)
{
	int p, max_p = 0, max_s = 0;
	int spot_xi, spot_yi;
	for (int s = 1; s < g_size; ++s)
	{
		p = find_max (g, g_size, s, spot_xi, spot_yi);
		if (p > max_p)
		{
			max_p = p;
			max_s = s;
			spot_x = spot_xi;
			spot_y = spot_yi;
		}
		std::cout << "max for size " << s << " is " << p << " at " << spot_xi+1 << ", " << spot_yi+1
				  << " max: (" << spot_x+1 << "," << spot_y+1 << "," << max_s << ")" << std::endl;
	}
	return 0;
}

int main (int argc, char** argv)
{
	int serial = atoi (argv[1]);
	std::cout << "serial is " << serial << std::endl;
	int* g = build_grid (serial, 300);
	int spot_x, spot_y, power;
	power = find_all_max (g, 300, spot_x, spot_y);
	return 0;
}