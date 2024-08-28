def naive_solution(prices):
    n = len(prices)
    result = [1] * n
    
    for i in range(n):
        count = 1
        for j in range(i - 1, -1, -1):
            if prices[j] <= prices[i]:
                count += 1
            else:
                break
        result[i] = count
    
    return result

def efficient_solution(prices):
    n = len(prices)
    result = [1] * n
    stack = []
    
    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            j = stack.pop()
            result[i] += result[j]
        stack.append(i)
    
    return result

# Test the algorithms
prices = [100, 80, 60, 70, 60, 75, 85]
print("Input prices:", prices)
print("Naive solution:", naive_solution(prices))
print("Efficient solution:", efficient_solution(prices))
