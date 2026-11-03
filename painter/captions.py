from options import WrappingMethod, WRAPPING_METHOD_MAPPER

class Captions:

    def __init__(self, wrapping_method: WrappingMethod) -> None:
        self.method = wrapping_method
    
    def get(self, caption: str) -> [str]:
        return [caption]