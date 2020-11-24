class Pistolet:

    def __init__(self, weight, max_capacity, color):
        self.weight = weight
        self.color = color
        self.max_capacity = max_capacity

    def __call__(self, *args, **kwargs):
        print(self._shoot())

    def _shoot(self):
        return "ОГОНЬ НА ПОРАЖЕНИЕ!"


class Automat:
    def __init__(self, bps):
        self.bps = bps

    def _shoot(self):
        return "АВТОМАТИЧЕСКИЙ ОГОНЬ НА ПОРАЖЕНИЕ!"


class ToyPistol(Pistolet):
    def __init__(self, new_field, weight, max_capacity, color):
        super().__init__(weight, max_capacity, color)
        self.new_field = new_field

    def _shoot(self):
        print(super()._shoot())
        return "АВТОМАТИЧЕСКИЙ ОГОНЬ НА ПОРАЖЕНИЕ!"

toy_pistol = ToyPistol("water", 1, 12, "water")
toy_pistol()
