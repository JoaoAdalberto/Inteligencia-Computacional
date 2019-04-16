 
#Programa para a cadeira de IC para o problema dos missionários e canibais

class State():
	def __init__(self, missionary_left=0, missionary_right=0, cannibals_left=0, cannibals_right=0, side='left', move=None):
		self.n_missionary_left = missionary_left
		self.n_missionary_right= missionary_right
		self.n_cannibals_left = cannibals_left
		self.n_cannibals_right = cannibals_right
		self.current_side = side
		self.father = None		
		self.move = move
		self.sons = []
	
	def __str__(self):
		if self.move is None:
			return '({},{}) ----------- ({},{})'.format(self.n_missionary_left, self.n_cannibals_left, self.n_missionary_right, self.n_cannibals_right)
		if self.current_side == 'right':
			return 'Move ({},{}) para a direita'.format(self.move[0], self.move[1])
		else:
			return 'Move ({},{}) para a esquerda'.format(self.move[0], self.move[1])
		
	def isValid(self):
		if self.n_missionary_left < 0 or self.n_missionary_right < 0 or self.n_cannibals_left < 0 or self.n_cannibals_right < 0:		
			return False
			
		return ((self.n_missionary_left == 0 or self.n_missionary_left >= self.n_cannibals_left) and
                (self.n_missionary_right == 0 or self.n_missionary_right >= self.n_cannibals_right))	
	
	def isDesiredState(self):
		if self.n_missionary_left == 0 and self.n_missionary_right == 3	and self.n_cannibals_left == 0 and self.n_cannibals_right == 3:		
			return True
		else:
			return False
			
class Problem():
	def __init__(self):
            #todas as possibilidades
		self.moves_available = [(2,0), (1,0), (1,1), (0,1), (0,2)]

		
		self.initialState = State(3, 0, 3, 0)
		self.generateSons(self.initialState)
		
	def generateSons(self, father_state):
		for move in self.moves_available:
			new_state = State(move=move)
			
			if father_state.current_side == 'left':
				new_state.n_missionary_left = father_state.n_missionary_left - move[0]
				new_state.n_missionary_right= father_state.n_missionary_right + move[0]
				new_state.n_cannibals_left = father_state.n_cannibals_left - move[1]
				new_state.n_cannibals_right = father_state.n_cannibals_right + move[1]
				new_state.current_side = 'right'
			else:
				new_state.n_missionary_left = father_state.n_missionary_left + move[0]
				new_state.n_missionary_right = father_state.n_missionary_right - move[0]
				new_state.n_cannibals_left = father_state.n_cannibals_left + move[1]
				new_state.n_cannibals_right = father_state.n_cannibals_right - move[1]
				new_state.current_side = 'left'
			
			if new_state.isValid():
				new_state.father = father_state
				father_state.sons.append(new_state)
		

		
	def showPath(self, state):
		path = []		
		s = state
		while s:
			path.insert(0, s)
			s = s.father	
		print("Solução:")
		print("(#Missionarios, #Canibais)")
		for p in path:
			print(str(p))
		
	def solve_problem(self):
		edge = [self.initialState]
		for state in edge:
			if state.isDesiredState():
				self.showPath(state)
				break			
			self.generateSons(state)
			edge.extend(state.sons)
		
problem = Problem()
problem.solve_problem()
