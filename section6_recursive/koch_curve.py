import math

def koch(n, p1, p2):
	if n == 0:
		return 0
	u = [0, 0]
	s, t, u = calculate(p1, p2, u)

	koch(n - 1, p1, s)
	print(' '.join([str(x) for x in s]))
	koch(n - 1, s, u)
	print(' '.join([str(x) for x in u]))
	koch(n - 1, u, t)
	print(' '.join([str(x) for x in t]))
	koch(n - 1, t, p2)


def calculate(a, b, u):
	th = math.radians(60)
	s, t = [0, 0], [0, 0]
	s[0] = (2.0 * a[0] + 1.0 * b[0]) / 3.0
	s[1] = (2.0 * a[1] + 1.0 * b[1]) / 3.0
	t[0] = (1.0 * a[0] + 2.0 * b[0]) / 3.0
	t[1] = (1.0 * a[1] + 2.0 * b[1]) / 3.0
	u[0] = (t[0] - s[0]) * math.cos(th) - (t[1] - s[1]) * math.sin(th) + s[0]
	u[1] = (t[0] - s[0]) * math.sin(th) + (t[1] - s[1]) * math.cos(th) + s[1]

	return s, t, u

if __name__ == "__main__":
	n = int(input())
	p1 = [0, 0]
	p2 = [100, 0]

	print(' '.join([str(x) for x in p1]))
	koch(n, p1, p2)
	print(' '.join([str(x) for x in p2]))