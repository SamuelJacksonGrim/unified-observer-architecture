class Reinforcement:
    def strengthen(self, memory):
        memory["weight"] = memory.get("weight", 1) + 1
        return memory
