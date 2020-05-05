import solver.rubiks_cube as rc
import solver.list_wrapper as wrap
import solver.thistlewaite.phase_two_key as p2k
import solver.thistlewaite.phase_three_key as p3k
import solver.thistlewaite.phase_four_key as p4k
import queue


class MoveTableNode():
    parity_map = dict()

    def __init__(self, corners=None, edges=None, cube=None):
        if (corners is None) and (cube is None):
            self.rubiks_cube = rc.RubiksCube()
            self.moves = list()
            self.moves.append(rc.RubiksCube.I)
        elif cube is not None:
            self.rubiks_cube = cube
            self.moves = list()
            self.moves.append(rc.RubiksCube.I)
        else:
            self.rubiks_cube = rc.RubiksCube(corners, edges)
            self.moves = list()
            self.moves.append(rc.RubiksCube.I)

    def __copy__(self):
        node = MoveTableNode()
        node.rubiks_cube = self.rubiks_cube.__copy__()
        node.moves = self.moves.copy()
        return node

    def __eq__(self, other):
        return self.rubiks_cube.__eq__(other.rubiks_cube) and self.moves.__eq__(other.moves)

    def do_move(self, move):
        node = self.__copy__()
        node.rubiks_cube.do_thistlewaite_move(move)
        node.moves.append(move)
        return node

    def get_phase_one_key(self):
        key = list()
        for edge in self.rubiks_cube.edges:
            key.append(edge % 2)
        return wrap.ListWrapper(key)

    def get_phase_two_key(self):
        corner_orientations = list()
        middle_edge_positions = list()

        for corner in self.rubiks_cube.corners:
            corner_orientations.append(corner % 3)
        for edge in self.rubiks_cube.edges:
            if (edge == 0) or (edge == 4) or (edge == 16) or (edge == 20):
                middle_edge_positions.append(1)
            else:
                middle_edge_positions.append(0)

        return p2k.PhaseTwoKey(corner_orientations, middle_edge_positions)

    def get_phase_three_key(self):
        corner_encoding = list()
        for corner in self.rubiks_cube.corners:
            if (corner == 0) or (corner == 6):
                corner_encoding.append(0)
            elif (corner == 15) or (corner == 21):
                corner_encoding.append(1)
            elif (corner == 3) or (corner == 9):
                corner_encoding.append(2)
            elif (corner == 12) or (corner == 18):
                corner_encoding.append(3)
        edge_encoding = list()
        for edge in self.rubiks_cube.edges:
            if (edge == 0) or (edge == 4) or (edge == 16) or (edge == 20):
                edge_encoding.append(0)
            elif (edge == 2) or (edge == 6) or (edge == 18) or (edge == 22):
                edge_encoding.append(1)
            elif (edge == 8) or (edge == 10) or (edge == 12) or (edge == 14):
                edge_encoding.append(2)
        parity = self.parity_map[self.get_corner_permutation_key()]
        return p3k.PhaseThreeKey(corner_encoding, edge_encoding, parity)

    def get_phase_four_key(self):
        return p4k.PhaseFourKey(self.rubiks_cube.corners.copy(), self.rubiks_cube.edges.copy())

    def get_corner_permutation_key(self):
        key = list()
        for corner in self.rubiks_cube.corners:
            permutation = corner - corner % 3
            key.append(permutation)

        return wrap.ListWrapper(key)

    @classmethod
    def initialize_parity_map(cls):
        search_queue = queue.Queue(0)
        starting_node = MoveTableNode()
        search_queue.put(starting_node)
        cls.parity_map[starting_node.get_corner_permutation_key()] = starting_node.get_parity()
        number_cases = 1
        while not search_queue.empty():
            current_node = search_queue.get()
            for move in rc.RubiksCube.allowed_moves_map[current_node.moves[len(current_node.moves) - 1]]:
                new_node = current_node.do_move(move)
                if not (new_node.get_corner_permutation_key() in cls.parity_map):
                    cls.parity_map[new_node.get_corner_permutation_key()] = new_node.get_parity()
                    search_queue.put(new_node)
                    number_cases += 1
                    print(number_cases)

    def get_parity(self):
        move_count = 0
        for move in self.moves:
            if (move == rc.RubiksCube.R2) or (move == rc.RubiksCube.L2) or (move == rc.RubiksCube.U2) or (
                    move == rc.RubiksCube.D2) or (move == rc.RubiksCube.F2) or (move == rc.RubiksCube.B2):
                move_count += 2
                # print(move_count)
                # print(move_count)
            elif move != rc.RubiksCube.I:
                move_count += 1
                # print(move_count)
        return move_count % 2 == 0
