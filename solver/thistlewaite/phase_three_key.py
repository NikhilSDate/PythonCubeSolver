class PhaseThreeKey:
    def __init__(self, corner_encoding, edge_encoding, parity):
        self.corner_encoding = corner_encoding
        self.edge_encoding = edge_encoding
        self.parity = parity

    def __eq__(self, other):
        return self.corner_encoding == other.corner_encoding and self.edge_encoding == other.edge_encoding and self.parity == other.parity

    def __hash__(self):
        c_result = 0
        for corner_code in self.corner_encoding:
            c_result = 31 * c_result + corner_code
        e_result = 0
        for edge_code in self.edge_encoding:
            e_result = 31 * e_result + edge_code
        result = c_result
        result = 31 * result + e_result
        result = 31 * result + hash(self.parity)
        return result

    def __str__(self):
        pass
