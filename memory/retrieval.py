class RetrievalEngine:
    def retrieve_by_weight(self, archive, minimum_weight=1):
        return [m for m in archive.retrieve_all() if m.get("weight", 0) >= minimum_weight]

    def retrieve_by_stage(self, archive, stage):
        return [m for m in archive.retrieve_all() if m.get("stage") == stage]
