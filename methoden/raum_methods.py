inhibition_radius = 5 # shouldn't be 0
min_overlap       = 7 # starts with 0
minlocalactivity  = 5

def check_inhibition(region):
	winner = []
	
	for coll in region.colloums:
		nachbarliste 	 = region.nachbaren(coll.position,inhibition_radius)
		minlocalactivity = n_kleinste_ueberlappung(nachbarliste,region)

		if coll.overlap > 0 and coll.overlap > minlocalactivity:
			winner.append(coll.position)

	return winner

def learning(winners,region):
	for pos in winners:
		coll = region.coll_by_position(pos)
		coll.dendrit_segment.learning()

	
def n_kleinste_ueberlappung(nachbarliste,region):
	overlap_measures = []

	for position in nachbarliste:
		coll  = region.coll_by_position(position)
		overlap_measures.append(coll.overlap)
	
	overlap_measures.sort(key=int)

	return overlap_measures[len(overlap_measures) - min_overlap]
	

