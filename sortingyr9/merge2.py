def func1(l, r):
	if not len(l) or not len(r):
		return l or r

	result = []
	i, j = 0, 0
	while (len(result) < len(l) + len(r)):
		if l[i] < r[j]:
			result.append(l[i])
			i+= 1
		else:
			result.append(r[j])
			j+= 1
		if i == len(l) or j == len(r):
			result.extend(l[i:] or r[j:])
			break

	return result

def func2(list):
	if len(list) < 2:
		return list

	mid = int(len(list)/2)
	l = func2(list[:middle])
	r = func2(list[middle:])

	return func1(l, r)


if __name__ == "__main__":
    print(func2([3, 4, 5, 1, 2, 8, 3, 7, 6]))