class SignalRouter:
    def __init__(self, bus):
        self.bus = bus

    def route(self, signal_type, payload):
        self.bus.publish(signal_type, payload)
