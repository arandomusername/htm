import cla_colloumn

class region():

	coll_groesse = 4
	max_groesse  = 20
	min_overlap  = 7
	inhibition_radius = 5
    
	def __init__(self,groesse,input_groesse):
		self.colloums      = []
		self.input_groesse = input_groesse
		self.max_groesse = groesse
	
		for x in range(0,self.max_groesse):
			for y in range(0,self.max_groesse):
				pos = (x,y)
				self.add_Colloum(pos)

	#starts the regional learning
	def raum(self,Input):
		self.set_overlap(Input)
		winner = self.check_inhibition()
		self.learning(winner)
		self.reset_overlaps()
	
	#activate cell based on their prediction state
	def activate_cells(self,winners):
		for winner in winners:
			coloumn 	= self.coll_by_position(winner)
			coloumn.activate_cells()

	# checks if a coloum "wins" based on his own overlap score and the score of its neighbours 
	def check_inhibition(self):
		winner = []
		for coll in self.colloums:
			nachbarliste 	   = self.nachbaren(coll.position)
			min_local_activity = self.n_smallest_overlap(nachbarliste)
			
			if coll.dendrit_segment.overlap > 0 and coll.dendrit_segment.overlap > min_local_activity:
				winner.append(coll.position)
		return winner

	# add a coloumn at a certain position and initializes a dendrit_segment
	def add_Colloum(self,pos):
		coll = cla_colloumn.colloum(self.coll_groesse,pos)
		coll.dendrit_segment.initialize_proximale_dendriten(self.input_groesse)
		self.colloums.append(coll)

	# returns a colloum by its position
	def coll_by_position(self,pos):
		for coll in self.colloums:
			if coll.position == pos:
				return coll

	# resets the overlap score of the colloums
	def reset_overlaps(self):		
		for coll in self.colloums:
			coll.dendrit_segment.overlap = 0

	# returns a list of which cells are in the active state
	def get_active_cells(self):
		active_cells = []
		for coll in self.colloums:
			for neuron in coll.neurons:
				if neuron.is_active():
					active_cells.append(neuron.pos)
		return activate_cells

	# lets the winnercolloumn learn from their connections
	def learning(self,winners):
		for pos in winners:
			coll = self.coll_by_position(pos)
			coll.dendrit_segment.learning()

	#searches the neighbours of a coloumn for the n-te overlap score
	def n_smallest_overlap(self,nachbarliste):
		overlap_measures = []
		for position in nachbarliste:
			coll  = self.coll_by_position(position)
			overlap_measures.append(coll.dendrit_segment.overlap)
		overlap_measures.sort(key=int)
		return overlap_measures[len(overlap_measures) - region.min_overlap]

	def predict_activation(self):
		active_cells = self.get_active_cells()
		for coll in self.colloums:
			for neuron in coll.neurons:
				print "something"				

	# returns position of coll in the radius (the radius is a square not a circle)
	def nachbaren(self,pos): 	
		nachbarlist = []
		pos_x 		= pos[0]
		pos_y 		= pos[1]
	
		x1 = pos_x - region.inhibition_radius
		x2 = pos_x + region.inhibition_radius
		y1 = pos_y - region.inhibition_radius
		y2 = pos_y + region.inhibition_radius

		if x1 < 0:
			x1 = 0
		if y1 < 0:
			y1 = 0

		if x2 > self.max_groesse:
			x2 = self.max_groesse
		if y2 > self.max_groesse:
			y2 = self.max_groesse
		
		for x in range(x1,x2):
			for y in range(y1,y2):
				position = (x,y)
				nachbarlist.append(position)

		return nachbarlist

	# sets the overlap score for each colloumn
	def set_overlap(self,Input):
		for coll in self.colloums:
			coll.dendrit_segment.set_overlap(Input)

