import cla_dendrite

class neuron():

	active  = False
	predic  = False
	position= ()

	def __init__(self,pos):
		self.active = False
		self.predic = False
		self.position = pos
		self.dendritsegment = cla_dendrite.dendritsegment(self.position)


class colloum():
	position = ()
	neurons  = []
	active   = False
	overlap  = 0
	dendrit_segment = cla_dendrite.dendritsegment(0)

	def __init__(self,coll_groesse,Position):       
		self.position = Position
		self.add_Neurones(coll_groesse,self.neurons)
		self.dendrit_segment = cla_dendrite.dendritsegment(Position)

	def add_Neurones(self,neur_quantity,neurs):
		for x in range(0,neur_quantity):
			pos = (x,) + self.position
			neur = neuron(pos)
			self.neurons.append(neur)
