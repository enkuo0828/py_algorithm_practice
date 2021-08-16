def recurcive_function(n):
	if n == 1:
		return 10
	else:
		return recurcive_function(n-1) + 15

if __name__ == "__main__":
    print(recurcive_function(1000))