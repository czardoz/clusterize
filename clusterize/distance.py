from lcs import lcs


class _StringDistance(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.matches = None

    def measure(self):
        matches = sum([x[-1] for x in self.get_matches()])  # total matching length between two strings
        return 2.0 * matches / (len(self.first) + len(self.second))

    def get_matches(self):
        if self.matches is not None:
            return self.matches

        self.matches = []
        len_first, len_second = len(self.first), len(self.second)
        self._recurse(0, len_first, 0, len_second)
        return self.matches

    def _recurse(self, first_start, first_end, second_start, second_end):
        first_start_index, second_start_index, substr_len = self.get_longest_substr(first_start, first_end,
                                                                                    second_start, second_end)
        if substr_len > 0:
            if first_start < first_start_index:
                self._recurse(first_start, first_start_index, second_start, second_start_index)
            self.matches.append((first_start_index, second_start_index, substr_len))
            if first_start_index + substr_len < first_end and second_start_index + substr_len < second_end:
                self._recurse(first_start_index + substr_len, first_end, second_start_index + substr_len, second_end)

    def get_longest_substr(self, first_start, first_end, second_start, second_end):
        # alpha & beta are the substrings under consideration.
        alpha, beta = self.first[first_start:first_end], self.second[second_start:second_end]
        start, end, length = lcs(alpha, beta)
        return first_start + start, second_start + end, length


class RequestDistance(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second

if __name__ == '__main__':
    # Junk Code
    str1 = "http://10.11.148.56:9527/res/tutoresL"
    str2 = "http://109.74.197.46:60000/exesyscmds"

    print str1, str2

    d = _StringDistance(str1, str2)
    print d.measure()

