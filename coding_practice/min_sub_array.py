def min_sub_array(arr, n):
	p1 = 0
	p2 = 0
	arr_len = len(arr)
	target_length = arr_len
	temp_sum = 0
	while p1 < arr_len and p2 < arr_len:
		# add to n
		print(f"target: {target_length}, p1: {p1}, p2: {p2}, arr: {arr[p1:p2+1]}")
		# temp_sum = sum(arr[p1:p2+1])
		if temp_sum < n:
			print("< n")
			p2 += 1
			temp_sum += arr[p2]
			continue
		print("> n")
		# temp_sum >= n
		# assign length
		if target_length > (p2 - p1 + 1):
			#print(target_length)
			target_length = p2 - p1 + 1
		temp_sum -= arr[p1]
		p1 += 1
	return target_length

if __name__ == '__main__':
    print('test')
    print(min_sub_array([8,1,6,15,3,16,5,7,14,30,12], 60))