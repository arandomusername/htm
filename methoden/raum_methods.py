inhibition_radius = 2 # shouldn't be 0
min_overlap       = 1 # starts with 0
minlocalactivity  = 1



def get_overlap_onedim(Input,region):
	overlap_list = []

	for coll in region.colloums:
		overlap = 0
		for dendrit in coll.dendrit_segment.dendrite:
			#Umwandeln von den "2-dimensionalen"-Dendriten auf den eindimensionalen Input	
			#position = coll.dendrit_segment.zweidim_zu_eindim((dendrit.ziel_pos[0],dendrit.ziel_pos[1]))
			 
			if dendrit.uebertraegt_signal(Input[dendrit.ziel_pos]):
					overlap = overlap + 1
		
		coll.overlap = overlap

def check_inhibition(region):
	winner = []

	for coll in region.colloums:
		nachbarliste 	 = region.nachbaren(coll.position,inhibition_radius)
		minlocalactivity = n_kleinste_ueberlappung(nachbarliste,region)

		if coll.overlap > 0 and coll.overlap >= minlocalactivity:
			winner.append(coll.position)

	return winner

def learning(winners,region):
	print len(winners)
	for pos in winners:
		coll = coll_by_position(pos)
		coll.dendrit_segment.learning()

	
def n_kleinste_ueberlappung(nachbarliste,region):
	overlap_measures = []

	for position in nachbarliste:
		coll  = region.coll_by_position(position)
		overlap_measures.append(coll.overlap)
	
	overlap_measures.sort(key=int)
	print str(overlap_measures[min_overlap])
	return overlap_measures[min_overlap]
	

