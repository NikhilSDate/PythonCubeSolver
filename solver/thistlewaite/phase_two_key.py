class PhaseTwoKey:
    def __init__(self, corner_orientations, middle_edge_positions):
        self.corner_orientations=corner_orientations
        self.middle_edge_positions=middle_edge_positions
    def __eq__(self, other):
        return  self.corner_orientations==other.corner_orientations and self.middle_edge_positions==other.middle_edge_positions
    def __hash__(self):
        c_result=0
        for corner_orientation in self.corner_orientations:
            c_result=31*c_result+corner_orientation
        e_result=0
        for middle_edge_position in self.middle_edge_positions:
            e_result=31*e_result+middle_edge_position
        return 31*c_result+e_result
    def __str__(self):
        pass
