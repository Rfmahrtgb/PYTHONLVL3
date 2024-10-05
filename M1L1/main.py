def solve_rid():
    for candies in range(100):
        if candies % 2 == 1 and candies % 3 == 1:
            return candies 
    
    result = solve_rid
    print(f"У гнома {result} конфеты(ы)")