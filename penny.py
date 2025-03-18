from card import Card
import random

_MODE_FRONT = 0
_MODE_BACK = 1

class Penny:
    def __init__(self):
        self._cards: list[Card] = []

    def cards(self):
        return self._cards

    def read(self, lines: list[str]):
        mode = None

        for i in range(len(lines)):
            line = lines[i].strip()
            if line.lower() == '[front]':
                mode = _MODE_FRONT
            elif line.lower() == '[back]':
                mode = _MODE_BACK
            elif line != '':
                # A card's front can only be one line
                if mode == _MODE_FRONT:
                    self._cards.append(Card(front=line))
                elif mode == _MODE_BACK:
                    # Only add a trailing newline if the current line is not the last line of the
                    # card's back and not the last line of the lines list
                    end = '\n'
                    if i + 1 >= len(lines) or lines[i+1].strip() == '[front]':
                        end = ''
                    self._cards[len(self._cards)-1].back += line + end

    def shuffled(self):
        """Yields a shuffled copy of the cards"""
        shuffled_cards = self._cards.copy()
        random.shuffle(shuffled_cards)
        yield from shuffled_cards
