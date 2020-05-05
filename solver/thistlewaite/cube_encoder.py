import solver.rubiks_cube as rc
import cv2
class CubeEncoder:
    corner_positions = dict()
    edge_positions = dict()

    corner_encoding=dict()
    edge_encoding=dict()

    cube_faces=['R','O','W','Y','G','B']

    def __init__(self):
        self.cube_colors=dict()

    class CubeColor:
        def __init__(self, face, position):
            self.face=face
            self.position=position
        def __eq__(self, other):
            return (self.face==other.face) and (self.position==other.position)
        def __hash__(self):
            result=hash(self.face)
            result=31*result+hash(self.position)
            return result
    class CornerPosition:
        def __init__(self, face1, position1, face2, position2, face3, position3):
            self.first_color=CubeEncoder.CubeColor(face1,position1)
            self.second_color = CubeEncoder.CubeColor(face2, position2)
            self.third_color = CubeEncoder.CubeColor(face3, position3)
    class EdgePosition:
        def __init__(self, face1, position1, face2, position2):
            self.first_color=CubeEncoder.CubeColor(face1,position1)
            self.second_color = CubeEncoder.CubeColor(face2, position2)

    def initialize_maps(self):
        self.initialize_corner_encoding()
        self.initialize_edge_encoding()
        self.initialize_corner_positions()
        self.initialize_edge_positions()

    def initialize_corner_positions(self):
        self.corner_positions[0]= self.CornerPosition('R', 2, 'G', 6, 'W', 0)
        self.corner_positions[1]= self.CornerPosition('O', 0, 'W', 2, 'G', 4)
        self.corner_positions[2]= self.CornerPosition('O', 6, 'B', 2, 'W', 4)
        self.corner_positions[3]= self.CornerPosition('R', 4, 'W', 6, 'B', 0)
        self.corner_positions[4]= self.CornerPosition('O', 4, 'Y', 2, 'B', 4)
        self.corner_positions[5]= self.CornerPosition('O', 2, 'G', 2, 'Y', 4)
        self.corner_positions[6]= self.CornerPosition('R', 0, 'Y', 6, 'G', 0)
        self.corner_positions[7]= self.CornerPosition('R', 6, 'B', 6, 'Y', 0)
    def initialize_edge_positions(self):
        self.edge_positions[0]=self.EdgePosition('W', 1, 'G', 5)
        self.edge_positions[1]=self.EdgePosition('O', 7, 'W', 3)
        self.edge_positions[2]=self.EdgePosition('W', 5, 'B', 1)
        self.edge_positions[3]=self.EdgePosition('R', 3, 'W', 7)
        self.edge_positions[4]=self.EdgePosition('R', 1, 'G', 7)
        self.edge_positions[5]=self.EdgePosition('O', 1, 'G', 3)
        self.edge_positions[6]=self.EdgePosition('O', 5, 'B', 3)
        self.edge_positions[7]=self.EdgePosition('R', 5, 'B', 7)
        self.edge_positions[8]=self.EdgePosition('Y', 1, 'B', 5)
        self.edge_positions[9]=self.EdgePosition('O', 3, 'Y', 3)
        self.edge_positions[10]=self.EdgePosition('Y', 5, 'G', 1)
        self.edge_positions[11]=self.EdgePosition('R', 7, 'Y', 7)

    def initialize_corner_encoding(self):
        self.corner_encoding["RGW"]=0
        self.corner_encoding["WRG"]=1
        self.corner_encoding["GWR"]=2

        self.corner_encoding["OWG"]=3
        self.corner_encoding["GOW"]=4
        self.corner_encoding["WGO"]=5

        self.corner_encoding["OBW"]=6
        self.corner_encoding["WOB"]=7
        self.corner_encoding["BWO"]=8

        self.corner_encoding["RWB"]=9
        self.corner_encoding["BRW"]=10
        self.corner_encoding["WBR"]=11

        self.corner_encoding["OYB"]=12
        self.corner_encoding["BOY"]=13
        self.corner_encoding["YBO"]=14

        self.corner_encoding["OGY"]=15
        self.corner_encoding["YOG"]=16
        self.corner_encoding["GYO"]=17

        self.corner_encoding["RYG"]=18
        self.corner_encoding["GRY"]=19
        self.corner_encoding["YGR"]=20

        self.corner_encoding["RBY"]=21
        self.corner_encoding["YRB"]=22
        self.corner_encoding["BYR"]=23

    def initialize_edge_encoding(self):
        self.edge_encoding["WG"]= 0
        self.edge_encoding["GW"]= 1

        self.edge_encoding["OW"]= 2
        self.edge_encoding["WO"]= 3

        self.edge_encoding["WB"]= 4
        self.edge_encoding["BW"]= 5

        self.edge_encoding["RW"]= 6
        self.edge_encoding["WR"]= 7

        self.edge_encoding["RG"]= 8
        self.edge_encoding["GR"]= 9

        self.edge_encoding["OG"]= 10
        self.edge_encoding["GO"]= 11

        self.edge_encoding["OB"]= 12
        self.edge_encoding["BO"]= 13

        self.edge_encoding["RB"]= 14
        self.edge_encoding["BR"]= 15

        self.edge_encoding["YB"]= 16
        self.edge_encoding["BY"]= 17

        self.edge_encoding["OY"]= 18
        self.edge_encoding["YO"]= 19

        self.edge_encoding["YG"]= 20
        self.edge_encoding["GY"]= 21

        self.edge_encoding["RY"]= 22
        self.edge_encoding["YR"]= 23

    def get_cube(self):
        for face in self.cube_faces:
            print('Enter colors for '+face+' face')
            for position in range(8):
                print(str(position)+":", end='')
                color=input()
                self.cube_colors[self.CubeColor(face,position)]=color
        cube=rc.RubiksCube()
        for position, colors in self.corner_positions.items():
            corner=self.cube_colors[colors.first_color]+self.cube_colors[colors.second_color]+self.cube_colors[colors.third_color]
            encoding=self.corner_encoding[corner]
            cube.corners[position]=encoding
        for position, colors in self.edge_positions.items():
            edge=self.cube_colors[colors.first_color]+self.cube_colors[colors.second_color]
            encoding=self.edge_encoding[edge]
            cube.edges[position]=encoding
        return cube



