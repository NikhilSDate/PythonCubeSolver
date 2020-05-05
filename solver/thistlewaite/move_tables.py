import queue
import solver.thistlewaite.move_table_node as mv
import solver.rubiks_cube as rc
import solver.thistlewaite.cube_encoder as enc


class MoveTables:
    phase_one_cases = 2048
    phase_two_cases = 1082565
    phase_three_cases = 352800

    move_inverses = dict()

    def __init__(self):
        self.phase_one_table = dict()
        self.phase_two_table = dict()
        self.phase_three_table = dict()
        self.phase_four_table = dict()

    def solve(self, cube):

        node = mv.MoveTableNode(corners=None, edges=None, cube=cube)

        phase_one_moves = self.phase_one_table[node.get_phase_one_key()]
        print(str(phase_one_moves))
        phase_one_moves.reverse()
        self.invert_moves(phase_one_moves)
        print("phaseOneMoves= " + str(phase_one_moves))
        for move in phase_one_moves:
            node.rubiks_cube.do_thistlewaite_move(move)

        phase_two_moves = self.phase_two_table[node.get_phase_two_key()]
        phase_two_moves.reverse()
        self.invert_moves(phase_two_moves)
        print("phaseTwoMoves= " + str(phase_two_moves))
        for move in phase_two_moves:
            node.rubiks_cube.do_thistlewaite_move(move)

        phase_three_moves = self.phase_three_table[node.get_phase_three_key()]
        phase_three_moves.reverse()
        self.invert_moves(phase_three_moves)
        print("phaseOneMoves= " + str(phase_three_moves))
        for move in phase_three_moves:
            node.rubiks_cube.do_thistlewaite_move(move)

        phase_four_moves = self.phase_four_table[node.get_phase_four_key()]
        phase_four_moves.reverse()
        self.invert_moves(phase_four_moves)
        print("phaseOneMoves= " + str(phase_four_moves))
        for move in phase_four_moves:
            node.rubiks_cube.do_thistlewaite_move(move)

        solution = ''
        for move in phase_one_moves:
            solution += rc.RubiksCube.get_move_string(move)
        for move in phase_two_moves:
            solution += rc.RubiksCube.get_move_string(move)
        for move in phase_three_moves:
            solution += rc.RubiksCube.get_move_string(move)
        for move in phase_four_moves:
            solution += rc.RubiksCube.get_move_string(move)
        return solution

    def generate_phase_one_table(self):
        search_queue = queue.Queue(0)
        starting_node = mv.MoveTableNode()
        search_queue.put(starting_node)
        self.phase_one_table[starting_node.get_phase_one_key()] = starting_node.moves
        number_cases = 1
        while (not search_queue.empty()) and (number_cases <= self.phase_one_cases):
            current_node = search_queue.get()
            for move in rc.RubiksCube.allowed_moves_map[current_node.moves[len(current_node.moves) - 1]]:
                new_node = current_node.do_move(move)
                if not (new_node.get_phase_one_key() in self.phase_one_table):
                    self.phase_one_table[new_node.get_phase_one_key()] = new_node.moves
                    search_queue.put(new_node)
                    number_cases = number_cases + 1
                    print(number_cases)

    def generate_phase_two_table(self):
        search_queue = queue.Queue(0)
        starting_node = mv.MoveTableNode()
        search_queue.put(starting_node)
        self.phase_two_table[starting_node.get_phase_two_key()] = starting_node.moves
        number_cases = 1
        while not search_queue.empty():
            current_node = search_queue.get()
            for move in rc.RubiksCube.phase_two_allowed_moves_map[current_node.moves[len(current_node.moves) - 1]]:
                new_node = current_node.do_move(move)
                if not (new_node.get_phase_two_key() in self.phase_two_table):
                    self.phase_two_table[new_node.get_phase_two_key()] = new_node.moves
                    search_queue.put(new_node)
                    number_cases = number_cases + 1
                    print(number_cases)

    def generate_phase_three_table(self):
        search_queue = queue.Queue(0)
        starting_node = mv.MoveTableNode()
        search_queue.put(starting_node)
        self.phase_three_table[starting_node.get_phase_three_key()] = starting_node.moves
        number_cases = 1
        while not search_queue.empty():
            current_node = search_queue.get()
            for move in rc.RubiksCube.phase_three_allowed_moves_map[current_node.moves[len(current_node.moves) - 1]]:
                new_node = current_node.do_move(move)
                if not (new_node.get_phase_three_key() in self.phase_three_table):
                    self.phase_three_table[new_node.get_phase_three_key()] = new_node.moves
                    search_queue.put(new_node)
                    number_cases = number_cases + 1
                    print(number_cases)

    def generate_phase_four_table(self):
        search_queue = queue.Queue(0)
        starting_node = mv.MoveTableNode()
        search_queue.put(starting_node)
        self.phase_four_table[starting_node.get_phase_four_key()] = starting_node.moves
        number_cases = 1
        while not search_queue.empty():
            current_node = search_queue.get()
            for move in rc.RubiksCube.phase_four_allowed_moves_map[current_node.moves[len(current_node.moves) - 1]]:
                new_node = current_node.do_move(move)
                if not (new_node.get_phase_four_key() in self.phase_four_table):
                    self.phase_four_table[new_node.get_phase_four_key()] = new_node.moves
                    search_queue.put(new_node)
                    number_cases = number_cases + 1
                    print(number_cases)

    def invert_moves(self, moves):
        for i in range(len(moves)):
            moves[i] = rc.RubiksCube.move_inverses_map[moves[i]]


rc.RubiksCube.initialize_allowed_moves_maps()
mv.MoveTableNode.initialize_parity_map()
rc.RubiksCube.initialize_move_inverses_map()
encoder = enc.CubeEncoder()
encoder.initialize_maps()
cube = encoder.get_cube()
print(cube)
tables = MoveTables()

tables.generate_phase_one_table()
tables.generate_phase_two_table()
tables.generate_phase_three_table()
tables.generate_phase_four_table()

print(tables.solve(cube))
