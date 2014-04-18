import random
import cla_region

min_connection = 0.2
perm_schritt   = 0.01 

class dendrit():

	def __init__(self,zi_pos,permanenz):
		self.permanenz = 0.
		self.ziel_pos = zi_pos
		self.permanenz = permanenz
		self.aktiver_input = False

	def uebertraegt_signal(self,Input):
		if Input == "1":
			self.aktiver_input = True

		if Input == "1" and self.permanenz > min_connection :
			return True
			
		else:
			return False
			
	def permanenz_erhoehen(self):
		self.permanenz = self.permanenz + perm_schritt

		if self.permanenz > 1:
			self.permanenz = 1

	def permanenz_senken(self):
		self.permanenz = self.permanenz + perm_schritt
		
		if self.permanenz < 0 :
			self.permanenz = 0
	

class dendrit_segment():
	def __init__(self,ur_pos):
		self.ursprungs_position = ur_pos
		self.dendrite     = []
		self.input_groesse= 0

	def reset_aktivitaet(self):
		for dendrit in self.dendrite:
			dendrit.aktiv = False

	def reset_aktiver_input(self):
		for dendrit in self.dendrite:
			dendrit.aktiver_input = False

	def learning(self):
		for dendrit in self.dendrite:
			if dendrit.aktiver_input:
				dendrit.permanenz_erhoehen()
			else:
				dendrit.permanenz_senken()

		self.reset_aktiver_input()

	def initialize_distrale_dendriten(self,reg_groesse):
		anzahl_kolloumnen      = cla_region.region.coll_groesse
		gesamt_anzahl_neuronen = (reg_groesse * 2) * anzahl_kolloumnen
		anzahl_dendrite        = (gesamt_anzahl_neuronen/4) -(gesamt_anzahl_neuronen % 4)
		self.input_groesse	   = reg_groesse
		self.dendrite_hinzufuegen(anzahl_dendrite,reg_groesse)

	def initialize_proximale_dendriten(self,input_groesse):
		self.input_groesse 	   = input_groesse
		anzahl_dendrite        = (input_groesse/2) -(input_groesse % 2)
		self.dendrite_hinzufuegen(anzahl_dendrite,input_groesse)

	def zweidim_zu_eindim(self,(pos1,pos2)):
		pos1_dim = pos1 * (self.input_groesse - 1) + pos2
		return pos1_dim	
		
	def dendrite_hinzufuegen(self,anzahl_dendrite,bereich):
		List = []
		for x in range(0,anzahl_dendrite):
			test = False
			while not test :	
				x_pos = random.randrange(0,bereich)				
				if x_pos not in List:
					perm = zufalls_permanenz()
					den = dendrit(x_pos,perm)
					self.dendrite.append(den)
					List.append(x_pos)
					test = True
	
	def get_overlap_onedim(Input):
		overlap = 0
		for dendrit in self.dendrite:
			if dendrit.uebertraegt_signal(Input[dendrit.ziel_pos])
				overlap = overlap + 1
		return overlap
			
	
def zufalls_permanenz():
	z1 = random.randrange(0,20)
	z2 = random.randrange(0,20)
	z3 = z1 * perm_schritt
	z4 = z2 * perm_schritt
	perm = min_connection -z3 + z4
	return perm
	
