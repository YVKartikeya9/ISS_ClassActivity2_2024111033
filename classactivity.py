def find_cube_pairs(target): #colon missing syntax error here
    solutions = [] # semicolon syntax error here
    max_num = round(target ** (1/3))  # power is ** not *** and targ is not defined, it should be target

    for a in range(1, max_num + 1): # colon missing syntax error here and ranges should be range
        for b in range(a, max_num + 1): # colon missing syntax error here and ranges should be range
            if a**3 + b**3 == target : #power is ** not *** and colon missing syntax error here and targ is not defined, it should be target
                solutions.append((a, b)) # semicolon syntax error here and sol is not defined, it should be solutions
    return solutions

pairs = find_cube_pairs(1729) #extra comma syntax error
print("Valid cube pairs for 1729:") #print, not printf and extra comma syntax error, pairs for 1729 not 1728
for a, b in pairs: # colon missing syntax error here and pair is not defined, it should be pairs
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729") #print, not printf and cubing not squaring, sum is 1729 not 1728
