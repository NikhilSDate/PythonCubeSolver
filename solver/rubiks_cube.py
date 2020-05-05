class RubiksCube:
    urf = 0
    ufl = 1
    ulb = 2
    ubr = 3
    dbl = 4
    dlf = 5
    dfr = 6
    drb = 7

    uf = 0
    ul = 1
    ub = 2
    ur = 3
    fr = 4
    fl = 5
    bl = 6
    br = 7
    db = 8
    dl = 9
    df = 10
    dr = 11

    I = 255
    R = 0
    R_PRIME = 1
    R2 = 2
    L = 3
    L_PRIME = 4
    L2 = 5
    U = 6
    U_PRIME = 7
    U2 = 8
    D = 9
    D_PRIME = 10
    D2 = 11
    F = 12
    F_PRIME = 13
    F2 = 14
    B = 15
    B_PRIME = 16
    B2 = 17

    allowed_moves_map = dict()
    phase_two_allowed_moves_map = dict()
    phase_three_allowed_moves_map = dict()
    phase_four_allowed_moves_map = dict()

    move_inverses_map=dict()

    def __init__(self,corners=None,edges=None):
        if corners is None or edges is None:
            self.corners =[0, 3, 6, 9, 12, 15, 18, 21]
            self.edges = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
        else:
            self.corners = corners
            self.edges = edges





    def do_thistlewaite_algorithm(self, algorithm):
        for move in algorithm:
            self.do_thistlewaite_move(move)

    def do_thistlewaite_move(self, move):

        if move == self.R:
            self.do_generic_corner_move(self.urf, self.ubr, self.drb, self.dfr,
                                        self.dfr, self.urf, self.ubr, self.drb,
                                        0, 0, 0, 0)
            self.do_generic_edge_move(self.ur, self.br, self.dr, self.fr,
                                      self.fr, self.ur, self.br, self.dr,
                                      0)


        elif move == self.R_PRIME:
            self.do_generic_corner_move(self.urf, self.ubr, self.drb, self.dfr,
                                        self.ubr, self.drb, self.dfr, self.urf,
                                        0, 0, 0, 0)
            self.do_generic_edge_move(self.ur, self.br, self.dr, self.fr,
                                      self.br, self.dr, self.fr, self.ur,
                                      0)



        elif move == self.R2:
            self.do_generic_corner_move(self.urf, self.ubr, self.drb, self.dfr,
                                        self.drb, self.dfr, self.urf, self.ubr,
                                        0, 0, 0, 0)
            self.do_generic_edge_move(self.ur, self.br, self.dr, self.fr,
                                      self.dr, self.fr, self.ur, self.br,
                                      0)




        elif move == self.L:
            self.do_generic_corner_move(self.ufl, self.dlf, self.dbl, self.ulb,
                                        self.ulb, self.ufl, self.dlf, self.dbl,
                                        0, 0, 0, 0
                                        )
            self.do_generic_edge_move(self.ul, self.fl, self.dl, self.bl,
                                      self.bl, self.ul, self.fl, self.dl,
                                      0)


        elif move == self.L_PRIME:
            self.do_generic_corner_move(self.ufl, self.dlf, self.dbl, self.ulb,
                                        self.dlf, self.dbl, self.ulb, self.ufl,
                                        0, 0, 0, 0)
            self.do_generic_edge_move(self.ul, self.fl, self.dl, self.bl,
                                      self.fl, self.dl, self.bl, self.ul,
                                      0)

        elif move == self.L2:
            self.do_generic_corner_move(self.ufl, self.dlf, self.dbl, self.ulb,
                                        self.dbl, self.ulb, self.ufl, self.dlf,
                                        0, 0, 0, 0)
            self.do_generic_edge_move(self.ul, self.fl, self.dl, self.bl,
                                      self.dl, self.bl, self.ul, self.fl,
                                      0)

        elif move == self.U:
            self.do_generic_corner_move(self.urf, self.ufl, self.ulb, self.ubr,
                                        self.ubr, self.urf, self.ufl, self.ulb,
                                        1, 2, 1, 2)
            self.do_generic_edge_move(self.uf, self.ul, self.ub, self.ur,
                                      self.ur, self.uf, self.ul, self.ub,
                                      1)

        elif move == self.U_PRIME:
            self.do_generic_corner_move(self.urf, self.ufl, self.ulb, self.ubr,
                                        self.ufl, self.ulb, self.ubr, self.urf,
                                        1, 2, 1, 2)
            self.do_generic_edge_move(self.uf, self.ul, self.ub, self.ur,
                                      self.ul, self.ub, self.ur, self.uf,
                                      1)

        elif move == self.U2:
            self.do_generic_corner_move(self.urf, self.ufl, self.ulb, self.ubr,
                                        self.ulb, self.ubr, self.urf, self.ufl,
                                        0, 0, 0, 0)
            self.do_generic_edge_move(self.uf, self.ul, self.ub, self.ur,
                                      self.ub, self.ur, self.uf, self.ul,
                                      0)

        elif move == self.D:
            self.do_generic_corner_move(self.dbl, self.dlf, self.dfr, self.drb,
                                        self.drb, self.dbl, self.dlf, self.dfr,
                                        2, 1, 2, 1)
            self.do_generic_edge_move(self.db, self.dl, self.df, self.dr,
                                      self.dr, self.db, self.dl, self.df,
                                      1)

        elif move == self.D_PRIME:
            self.do_generic_corner_move(self.dbl, self.dlf, self.dfr, self.drb,
                                        self.dlf, self.dfr, self.drb, self.dbl,
                                        2, 1, 2, 1)
            self.do_generic_edge_move(self.db, self.dl, self.df, self.dr,
                                      self.dl, self.df, self.dr, self.db,
                                      1)

        elif move == self.D2:
            self.do_generic_corner_move(self.dbl, self.dlf, self.dfr, self.drb,
                                        self.dfr, self.drb, self.dbl, self.dlf,
                                        0, 0, 0, 0)
            self.do_generic_edge_move(self.db, self.dl, self.df, self.dr,
                                      self.df, self.dr, self.db, self.dl,
                                      0)

        elif move == self.F:
            self.do_generic_corner_move(self.urf, self.dfr, self.dlf, self.ufl,
                                        self.ufl, self.urf, self.dfr, self.dlf,
                                        2, 1, 2, 1)
            self.do_generic_edge_move(self.uf, self.fr, self.df, self.fl,
                                      self.fl, self.uf, self.fr, self.df,
                                      0)

        elif move == self.F_PRIME:
            self.do_generic_corner_move(self.urf, self.dfr, self.dlf, self.ufl,
                                        self.dfr, self.dlf, self.ufl, self.urf,
                                        2, 1, 2, 1)
            self.do_generic_edge_move(self.uf, self.fr, self.df, self.fl,
                                      self.fr, self.df, self.fl, self.uf,
                                      0)

        elif move == self.F2:
            self.do_generic_corner_move(self.urf, self.dfr, self.dlf, self.ufl,
                                        self.dlf, self.ufl, self.urf, self.dfr,
                                        0, 0, 0, 0)
            self.do_generic_edge_move(self.uf, self.fr, self.df, self.fl,
                                      self.df, self.fl, self.uf, self.fr,
                                      0)

        elif move == self.B:
            self.do_generic_corner_move(self.dbl, self.drb, self.ubr, self.ulb,
                                        self.ulb, self.dbl, self.drb, self.ubr,
                                        1, 2, 1, 2)
            self.do_generic_edge_move(self.db, self.br, self.ub, self.bl,
                                      self.bl, self.db, self.br, self.ub,
                                      0)

        elif move == self.B_PRIME:
            self.do_generic_corner_move(self.dbl, self.drb, self.ubr, self.ulb,
                                        self.drb, self.ubr, self.ulb, self.dbl,
                                        1, 2, 1, 2)
            self.do_generic_edge_move(self.db, self.br, self.ub, self.bl,
                                      self.br, self.ub, self.bl, self.db,
                                      0)

        elif move == self.B2:
            self.do_generic_corner_move(self.dbl, self.drb, self.ubr, self.ulb,
                                        self.ubr, self.ulb, self.dbl, self.drb,
                                        0, 0, 0, 0)
            self.do_generic_edge_move(self.db, self.br, self.ub, self.bl,
                                      self.ub, self.bl, self.db, self.br,
                                      0)

        elif move == self.I:
            pass
        else:
            print('wrong move')

    def do_generic_corner_move(self, d1, d2, d3, d4,
                               s1, s2, s3, s4,
                               o1, o2, o3, o4):
        old_corners = self.corners.copy()
        self.corners[d1] = (old_corners[s1] - old_corners[s1] % 3) + ((old_corners[s1] % 3 + o1) % 3)
        self.corners[d2] = (old_corners[s2] - old_corners[s2] % 3) + ((old_corners[s2] % 3 + o2) % 3)
        self.corners[d3] = (old_corners[s3] - old_corners[s3] % 3) + ((old_corners[s3] % 3 + o3) % 3)
        self.corners[d4] = (old_corners[s4] - old_corners[s4] % 3) + ((old_corners[s4] % 3 + o4) % 3)

    def do_generic_edge_move(self, d1, d2, d3, d4,
                             s1, s2, s3, s4,
                             o):
        old_edges = self.edges.copy()
        self.edges[d1] = (old_edges[s1] - old_edges[s1] % 2) + ((old_edges[s1] % 2 + o) % 2)
        self.edges[d2] = (old_edges[s2] - old_edges[s2] % 2) + ((old_edges[s2] % 2 + o) % 2)
        self.edges[d3] = (old_edges[s3] - old_edges[s3] % 2) + ((old_edges[s3] % 2 + o) % 2)
        self.edges[d4] = (old_edges[s4] - old_edges[s4] % 2) + ((old_edges[s4] % 2 + o) % 2)

    def __copy__(self):
        cube = RubiksCube()
        cube.corners = self.corners.copy()
        cube.edges = self.edges.copy()
        return cube

    def __str__(self) -> str:
        return 'solver.RubiksCube{' + \
               ' corners = ' + str(list(self.corners)) + \
               ' edges = ' + str(list(self.edges)) + \
               '}'

    @classmethod
    def initialize_allowed_moves_maps(cls):
        cls.allowed_moves_map[cls.R] = [cls.L, cls.L_PRIME, cls.L2, cls.U, cls.U_PRIME, cls.U2, cls.D,
                                        cls.D_PRIME, cls.D2, cls.F, cls.F_PRIME, cls.F2, cls.B, cls.B_PRIME,
                                        cls.B2]
        cls.allowed_moves_map[cls.R_PRIME] = [cls.L, cls.L_PRIME, cls.L2, cls.U, cls.U_PRIME, cls.U2, cls.D,
                                              cls.D_PRIME, cls.D2, cls.F, cls.F_PRIME, cls.F2, cls.B,
                                              cls.B_PRIME, cls.B2]
        cls.allowed_moves_map[cls.R2] = [cls.L, cls.L_PRIME, cls.L2, cls.U, cls.U_PRIME, cls.U2, cls.D,
                                         cls.D_PRIME, cls.D2, cls.F, cls.F_PRIME, cls.F2, cls.B, cls.B_PRIME,
                                         cls.B2]

        cls.allowed_moves_map[cls.L] = [cls.U, cls.U_PRIME, cls.U2, cls.D, cls.D_PRIME, cls.D2, cls.F,
                                        cls.F_PRIME, cls.F2, cls.B, cls.B_PRIME, cls.B2]
        cls.allowed_moves_map[cls.L_PRIME] = [cls.U, cls.U_PRIME, cls.U2, cls.D, cls.D_PRIME, cls.D2, cls.F,
                                              cls.F_PRIME, cls.F2, cls.B, cls.B_PRIME, cls.B2]
        cls.allowed_moves_map[cls.L2] = [cls.U, cls.U_PRIME, cls.U2, cls.D, cls.D_PRIME, cls.D2, cls.F,
                                         cls.F_PRIME, cls.F2, cls.B, cls.B_PRIME, cls.B2]

        cls.allowed_moves_map[cls.U] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2, cls.D,
                                        cls.D_PRIME, cls.D2, cls.F, cls.F_PRIME, cls.F2, cls.B, cls.B_PRIME,
                                        cls.B2]
        cls.allowed_moves_map[cls.U_PRIME] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2, cls.D,
                                              cls.D_PRIME, cls.D2, cls.F, cls.F_PRIME, cls.F2, cls.B,
                                              cls.B_PRIME, cls.B2]
        cls.allowed_moves_map[cls.U2] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2, cls.D,
                                         cls.D_PRIME, cls.D2, cls.F, cls.F_PRIME, cls.F2, cls.B, cls.B_PRIME,
                                         cls.B2]

        cls.allowed_moves_map[cls.D] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2, cls.F,
                                        cls.F_PRIME, cls.F2, cls.B, cls.B_PRIME, cls.B2]
        cls.allowed_moves_map[cls.D_PRIME] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2, cls.F,
                                              cls.F_PRIME, cls.F2, cls.B, cls.B_PRIME, cls.B2]
        cls.allowed_moves_map[cls.D2] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2, cls.F,
                                         cls.F_PRIME, cls.F2, cls.B, cls.B_PRIME, cls.B2]

        cls.allowed_moves_map[cls.F] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2, cls.U,
                                        cls.U_PRIME, cls.U2, cls.D, cls.D_PRIME, cls.D2, cls.B, cls.B_PRIME,
                                        cls.B2]
        cls.allowed_moves_map[cls.F_PRIME] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2, cls.U,
                                              cls.U_PRIME, cls.U2, cls.D, cls.D_PRIME, cls.D2, cls.B,
                                              cls.B_PRIME, cls.B2]
        cls.allowed_moves_map[cls.F2] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2, cls.U,
                                         cls.U_PRIME, cls.U2, cls.D, cls.D_PRIME, cls.D2, cls.B, cls.B_PRIME,
                                         cls.B2]

        cls.allowed_moves_map[cls.B] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2, cls.U,
                                        cls.U_PRIME, cls.U2, cls.D, cls.D_PRIME, cls.D2]
        cls.allowed_moves_map[cls.B_PRIME] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2, cls.U,
                                              cls.U_PRIME, cls.U2, cls.D, cls.D_PRIME, cls.D2]
        cls.allowed_moves_map[cls.B2] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2, cls.U,
                                         cls.U_PRIME, cls.U2, cls.D, cls.D_PRIME, cls.D2]

        cls.allowed_moves_map[cls.I] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2, cls.U,
                                        cls.U_PRIME, cls.U2, cls.D, cls.D_PRIME, cls.D2, cls.F, cls.F_PRIME,
                                        cls.F2, cls.B, cls.B_PRIME, cls.B2]

        cls.phase_two_allowed_moves_map[cls.R] = [cls.L, cls.L_PRIME, cls.L2, cls.U2, cls.D2, cls.F,
                                                  cls.F_PRIME, cls.F2, cls.B, cls.B_PRIME, cls.B2]
        cls.phase_two_allowed_moves_map[cls.R_PRIME] = [cls.L, cls.L_PRIME, cls.L2, cls.U2, cls.D2, cls.F,
                                                        cls.F_PRIME, cls.F2, cls.B, cls.B_PRIME, cls.B2]
        cls.phase_two_allowed_moves_map[cls.R2] = [cls.L, cls.L_PRIME, cls.L2, cls.U2, cls.D2, cls.F,
                                                   cls.F_PRIME, cls.F2, cls.B, cls.B_PRIME, cls.B2]

        cls.phase_two_allowed_moves_map[cls.L] = [cls.U2, cls.D2, cls.F, cls.F_PRIME, cls.F2, cls.B,
                                                  cls.B_PRIME, cls.B2]
        cls.phase_two_allowed_moves_map[cls.L_PRIME] = [cls.U2, cls.D2, cls.F, cls.F_PRIME, cls.F2, cls.B,
                                                        cls.B_PRIME, cls.B2]
        cls.phase_two_allowed_moves_map[cls.L2] = [cls.U2, cls.D2, cls.F, cls.F_PRIME, cls.F2, cls.B,
                                                   cls.B_PRIME, cls.B2]

        cls.phase_two_allowed_moves_map[cls.U2] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2,
                                                   cls.D2, cls.F, cls.F_PRIME, cls.F2, cls.B, cls.B_PRIME,
                                                   cls.B2]

        cls.phase_two_allowed_moves_map[cls.D2] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2,
                                                   cls.F, cls.F_PRIME, cls.F2, cls.B, cls.B_PRIME, cls.B2]

        cls.phase_two_allowed_moves_map[cls.F] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2,
                                                  cls.U2, cls.D2, cls.B, cls.B_PRIME, cls.B2]
        cls.phase_two_allowed_moves_map[cls.F_PRIME] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2,
                                                        cls.U2, cls.D2, cls.B, cls.B_PRIME, cls.B2]
        cls.phase_two_allowed_moves_map[cls.F2] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2,
                                                   cls.U2, cls.D2, cls.B, cls.B_PRIME, cls.B2]

        cls.phase_two_allowed_moves_map[cls.B] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2,
                                                  cls.U2, cls.D2]
        cls.phase_two_allowed_moves_map[cls.B_PRIME] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2,
                                                        cls.U2, cls.D2]
        cls.phase_two_allowed_moves_map[cls.B2] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2,
                                                   cls.U2, cls.D2]

        cls.phase_two_allowed_moves_map[cls.I] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2,
                                                  cls.U2, cls.D2, cls.F, cls.F_PRIME, cls.F2, cls.B,
                                                  cls.B_PRIME, cls.B2]

        cls.phase_three_allowed_moves_map[cls.R] = [cls.L, cls.L_PRIME, cls.L2, cls.U2, cls.D2, cls.F2, cls.B2]
        cls.phase_three_allowed_moves_map[cls.R_PRIME] = [cls.L, cls.L_PRIME, cls.L2, cls.U2, cls.D2, cls.F2,
                                                          cls.B2]
        cls.phase_three_allowed_moves_map[cls.R2] = [cls.L, cls.L_PRIME, cls.L2, cls.U2, cls.D2, cls.F2,
                                                     cls.B2]

        cls.phase_three_allowed_moves_map[cls.L] = [cls.U2, cls.D2, cls.F2, cls.B2]
        cls.phase_three_allowed_moves_map[cls.L_PRIME] = [cls.U2, cls.D2, cls.F2, cls.B2]
        cls.phase_three_allowed_moves_map[cls.L2] = [cls.U2, cls.D2, cls.F2, cls.B2]

        cls.phase_three_allowed_moves_map[cls.U2] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2,
                                                     cls.D2, cls.F2, cls.B2]

        cls.phase_three_allowed_moves_map[cls.D2] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2,
                                                     cls.F2, cls.B2]

        cls.phase_three_allowed_moves_map[cls.F2] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2,
                                                     cls.U2, cls.D2, cls.B2]

        cls.phase_three_allowed_moves_map[cls.B2] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2,
                                                     cls.U2, cls.D2]

        cls.phase_three_allowed_moves_map[cls.I] = [cls.R, cls.R_PRIME, cls.R2, cls.L, cls.L_PRIME, cls.L2,
                                                    cls.U2, cls.D2, cls.F2, cls.B2]

        cls.phase_four_allowed_moves_map[cls.R2] = [cls.L2, cls.U2, cls.D2, cls.F2, cls.B2]

        cls.phase_four_allowed_moves_map[cls.L2] = [cls.U2, cls.D2, cls.F2, cls.B2]

        cls.phase_four_allowed_moves_map[cls.U2] = [cls.R2, cls.L2, cls.D2, cls.F2, cls.B2]

        cls.phase_four_allowed_moves_map[cls.D2] = [cls.R2, cls.L2, cls.F2, cls.B2]

        cls.phase_four_allowed_moves_map[cls.F2] = [cls.R2, cls.L2, cls.U2, cls.D2, cls.B2]

        cls.phase_four_allowed_moves_map[cls.B2] = [cls.R2, cls.L2, cls.U2, cls.D2]

        cls.phase_four_allowed_moves_map[cls.I] = [cls.R2, cls.L2, cls.U2, cls.D2, cls.F2, cls.B2]
    @classmethod
    def get_move_string(cls,move):
        if move == cls.R:
           return 'R'
        elif move == cls.R_PRIME:
            return "R'"
        elif move == cls.R2:
            return 'R2'
        elif move == cls.L:
            return 'L'
        elif move == cls.L_PRIME:
            return "L'"
        elif move == cls.L2:
            return 'L2'
        elif move == cls.U:
            return 'U'
        elif move == cls.U_PRIME:
            return "U'"
        elif move == cls.U2:
            return 'U2'
        elif move == cls.D:
            return 'D'
        elif move == cls.D_PRIME:
            return "D'"
        elif move == cls.D2:
            return 'D2'
        elif move == cls.F:
            return 'F'
        elif move == cls.F_PRIME:
            return "F'"
        elif move == cls.F2:
            return 'F2'
        elif move == cls.B:
            return 'B'
        elif move == cls.B_PRIME:
            return "B'"
        elif move == cls.B2:
            return 'B2'
        elif move == cls.I:
            return ''
        else:
            return 'wrong move'
    @classmethod
    def initialize_move_inverses_map(cls):
        cls.move_inverses_map[cls.R]=cls.R_PRIME
        cls.move_inverses_map[cls.R_PRIME] = cls.R
        cls.move_inverses_map[cls.R2] = cls.R2

        cls.move_inverses_map[cls.L] = cls.L_PRIME
        cls.move_inverses_map[cls.L_PRIME] = cls.L
        cls.move_inverses_map[cls.L2] = cls.L2

        cls.move_inverses_map[cls.U] = cls.U_PRIME
        cls.move_inverses_map[cls.U_PRIME] = cls.U
        cls.move_inverses_map[cls.U2] = cls.U2

        cls.move_inverses_map[cls.D] = cls.D_PRIME
        cls.move_inverses_map[cls.D_PRIME] = cls.D
        cls.move_inverses_map[cls.D2] = cls.D2

        cls.move_inverses_map[cls.F] = cls.F_PRIME
        cls.move_inverses_map[cls.F_PRIME] = cls.F
        cls.move_inverses_map[cls.F2] = cls.F2

        cls.move_inverses_map[cls.B] = cls.B_PRIME
        cls.move_inverses_map[cls.B_PRIME] = cls.B
        cls.move_inverses_map[cls.B2] = cls.B2

        cls.move_inverses_map[cls.I]=cls.I

    def __eq__(self, other):
        return self.corners.__eq__(other.corners) and self.edges.__eq__(other.edges)
