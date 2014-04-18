activate_cells(winners, region):
	for winner in winners:
		column          = region.coll_by_position(winner)
		column.activate_cells()

predict_activation(region):
	
