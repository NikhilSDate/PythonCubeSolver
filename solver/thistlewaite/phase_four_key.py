class PhaseFourKey:
    def __init__(self, corners, edges):
        self.corners=corners
        self.edges=edges
    def __eq__(self, other):
        return  self.corners==other.corners and self.edges==other.edges
    def __hash__(self):
        c_result=0
        for corner in self.corners:
            c_result=31*c_result+corner
        e_result=0
        for edge in self.edges:
            e_result=31*e_result+edge
        return 31*c_result+e_result
    def __str__(self):
        pass
