class TextTransform:
    def run(self, s: str) -> str:
        raise NotImplementedError

class ReverseTransform(TextTransform):
    def run(self, s: str) -> str:
        return s[::-1]

class UppercaseTransform(TextTransform):
    def run(self, s: str) -> str:
        return s.upper()

class TransformFactory:
    @staticmethod
    def create(name: str) -> TextTransform:
        if name == "Reverse":
            return ReverseTransform()
        if name == "Uppercase":
            return UppercaseTransform()
        raise ValueError("Unknown transform")