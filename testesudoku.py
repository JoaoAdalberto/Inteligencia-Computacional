
from pulp import *

Sequence = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

Vals = Sequence
Rows = Sequence
Cols = Sequence

Boxes =[]
for i in range(3):
    for j in range(3):
        Boxes += [[(Rows[3*i+k],Cols[3*j+l]) for k in range(3) for l in range(3)]]
  
prob = LpProblem("Sudoku Problem",LpMinimize)

choices = LpVariable.dicts("Choice",(Vals,Rows,Cols),0,1,LpInteger)

prob += 0, "Arbitrary Objective Function"

# Uma restrição para que cada quadrado possa ter somente um número é criada
for r in Rows:
    for c in Cols:
        prob += lpSum([choices[v][r][c] for v in Vals]) == 1, ""

# As restrições de linha, coluna e caixa são criadas para cada número 
for v in Vals:
    for r in Rows:
        prob += lpSum([choices[v][r][c] for c in Cols]) == 1,""
        
    for c in Cols:
        prob += lpSum([choices[v][r][c] for r in Rows]) == 1,""

    for b in Boxes:
        prob += lpSum([choices[v][r][c] for (r,c) in b]) == 1,""

# Aqui iniciamos o sudoku com alguns números como restrição. Ordem : número, linha e coluna.
prob += choices["1"]["3"]["3"] == 1,""
prob += choices["3"]["2"]["6"] == 1,""
prob += choices["2"]["3"]["5"] == 1,""
prob += choices["8"]["2"]["8"] == 1,""
prob += choices["5"]["2"]["8"] == 1,""
prob += choices["5"]["4"]["4"] == 1,""
prob += choices["7"]["4"]["6"] == 1,""
prob += choices["4"]["5"]["3"] == 1,""
prob += choices["1"]["5"]["7"] == 1,""
prob += choices["9"]["6"]["2"] == 1,""
prob += choices["5"]["7"]["1"] == 1,""
prob += choices["7"]["7"]["8"] == 1,""
prob += choices["3"]["7"]["9"] == 1,""
prob += choices["2"]["8"]["3"] == 1,""
prob += choices["1"]["8"]["5"] == 1,""
prob += choices["4"]["9"]["5"] == 1,""
prob += choices["9"]["9"]["9"] == 1,""


prob.writeLP("Sudoku.lp")

prob.solve()

print("Status:", LpStatus[prob.status])

sudokuresolvido = open('sudokuresolvido.txt','w')

for r in Rows:
    if r == "1" or r == "4" or r == "7":
                    sudokuresolvido.write("+-------+-------+-------+\n")
    for c in Cols:
        for v in Vals:
            if value(choices[v][r][c])==1:
                               
                if c == "1" or c == "4" or c =="7":
                    sudokuresolvido.write("| ")
                    
                sudokuresolvido.write(v + " ")
                
                if c == "9":
                    sudokuresolvido.write("|\n")
sudokuresolvido.write("+-------+-------+-------+")                    
sudokuresolvido.close()

print("Solução salva em sudokuresolvido.txt")
