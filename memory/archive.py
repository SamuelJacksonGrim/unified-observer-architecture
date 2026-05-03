class MemoryArchive:
    def __init__(self):
        self.storage = []

    def store(self, experience):
        self.storage.append(experience)

    def retrieve_all(self):
        return self.storage
