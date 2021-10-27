class StringSearch:

    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern

    def p_length(self) -> int:
        return len(self.pattern)

    def t_length(self) -> int:
        return len(self.text)

    def find_full_scan(self) -> int:
        t = 0
        while t <= (self.t_length() - self.p_length()):
            p = 0

            while p < self.p_length() and self.text[t + p] == self.pattern[p]:
                p += 1
            if p == self.p_length():
                return t
            t += 1
        return -1

    def create_shift(self) -> list:
        shift = [x for x in range(129)]

        for i in range(len(shift)):
            shift[i] = len(self.pattern)

        for p in range(len(self.pattern) - 1):
            letter_order = ord(self.pattern[p])
            shift[letter_order] = len(self.pattern) - p - 1

        return shift

    def find_jumper(self) -> int:
        shift = self.create_shift()
        for t in range(self.t_length() - self.p_length() + 1):
            p = self.p_length() - 1

            while p >= 0 and self.text[t + p] == self.pattern[p]:
                p -= 1

            if p < 0:
                return t
            t += shift[ord(self.text[t + self.p_length() - 1])]

        return -1

    def boyer_moore_match(self) -> int:
        m = self.p_length()
        n = self.t_length()
        shift = self.create_shift()
        t = 0
        while t <= n - m:
            p = self.p_length() - 1
            while p >= 0 and self.pattern[p] == self.text[t + p]:
                p -= 1
            if p < 0:
                return t
            t += shift[ord(self.text[t + self.p_length() - 1])]

        return -1
