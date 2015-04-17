from dendrite_segment import dendrite_segment as dendrites


class neuron:
    def __init__(self, input_shape):
        self.dendrites = dendrites(input_shape)
        self.dendrites.connect_to_all()

    def get_activity_score(self, region_score):
        return self.dendrites.get_activity_score(region_score)
        # This is incomplete. The activity equals the regions activity.
