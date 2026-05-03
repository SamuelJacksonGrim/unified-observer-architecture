class FeedbackLoop:
    def reinforce(self, current, previous):
        return (current + previous) / 2.0
