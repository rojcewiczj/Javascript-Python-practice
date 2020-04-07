function findFrequent(arr) {
	index_count = 0
	arr_len = arr.length
	collect = []
	most_frequent = null
	while (arr_len > 0) {
		current = arr[index_count]
		collect.push(current)
		if(collect.includes(current)){
			most_frequent = current
		}
		index_count += 1
		arr_len -= 1
		
	}
	 return most_frequent
}

findFrequent(["superman", "superman", "batman"])