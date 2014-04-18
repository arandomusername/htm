import raum_methods

def raum(Input, region):
	print "		check overlap"
	region.get_overlap_onedim(Input)
	print "		get winners"
	winner = raum_methods.check_inhibition(region)
	print "		learning"
	raum_methods.learning(winner,region)


	
