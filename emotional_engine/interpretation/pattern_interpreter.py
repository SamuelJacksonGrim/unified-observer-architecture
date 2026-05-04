class PatternInterpreter:
    def interpret(self, pattern, colour):
        magnitude = float(sum(abs(x) for x in pattern))
        if magnitude > 2.5:
            state = "expansion"
        elif magnitude > 1.5:
            state = "oscillation"
        elif magnitude > 0.75:
            state = "softening"
        else:
            state = "stillness"
        return f"{state}::{colour['base']}::{colour['intensity']:.2f}"
