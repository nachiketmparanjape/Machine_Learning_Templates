S = input("Please enter a list of denominations (Separated by comma, no spaces) - ")
n = int(input("Please enter an ammount - "))

numlist = S.split(',')

S = sorted([int(i) for i in numlist],reverse=True)
m = len(S)



# We need n+1 rows as the table is consturcted in bottom up
# manner using the base case 0 value case (n = 0)
table = [[0 for x in range(m)] for y in range(n+1)]
 
# Fill the enteries for 0 value case (n = 0)
for i in range(m):
    table[0][i] = 1
 
# Fill rest of the table enteries in bottom up manner
for i in range(1, n+1):
    for j in range(m):
        # Count of solutions including S[j]
        x = table[i - S[j]][j] if i-S[j] >= 0 else 0
 
        # Count of solutions excluding S[j]
        y = table[i][j-1] if j >= 1 else 0
 
        # total count
        table[i][j] = x + y
             
print (table[n][m-1])