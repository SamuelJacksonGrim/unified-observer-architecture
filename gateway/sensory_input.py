class SensoryInput:
    def receive(self, raw_data):
        return {"sensory_signal": raw_data}
