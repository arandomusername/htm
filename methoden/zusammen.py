import raum_methods

def raum(Input, region):
	print "		check overlap"
	region.set_overlap(Input)
	print "		get winners"
	winner = raum_methods.check_inhibition(region)
	print "		learning"
	print winner
	region.learning(winner)
	region.reset_overlaps()


	
