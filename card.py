
class Card:
    def __init__(self, front: str = "", back: str = ""):
        self.front = front
        self.back = back

    def __eq__(self, other):
        return isinstance(other, Card) and (
            self.front == other.front and
            self.back == other.back
        )

    def __repr__(self):
        return f"Card({self.front}, {self.back})"
