from dendrite_segment import dendrite_segment as dendrites


class neuron:
    def __init__(self, input_shape):
        self.dendrites = dendrites(input_shape)

    def get_activity_score(self):
        # This is incomplete. The activity equals the regions activity.
        return self.dendrites.get_activity_score()
