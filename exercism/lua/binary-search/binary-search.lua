return function(array, target)
	left = 1
	right = #array

	while left <= right do
		m = (left + right) // 2

        if array[m] == target then
            return m
        end

        if array[m] < target then
            left = m + 1
        else
            right = m - 1
        end
	end

	return -1
end
