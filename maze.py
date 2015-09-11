# it is symmetrical vertically we could save some value but the real
# pain here is to go through the all lines
class Maze(object):
    def __init__(self):
        self.maze = self.initialize()
    def get_maze(self):
        return self.maze
    def initialize(self):
        #0 is wall no walk
        #1 empty walk
        #NOTE the matrix is line, column which are y and x
        _maze = [ [0] * 56 for x in range(62)]
        # first path line line #3
        for i in range(3,26):
            _maze[3][i] = 1
        for i in range(31,54):
            _maze[3][i] = 1
        # line #4,5,6,7,8.9,10 allow just down/up on the intersection
        for i in range(4,11):
            _maze[i][3] = _maze[i][13] = _maze[i][25] = _maze[i][31] = \
                          _maze[i][43] = _maze[i][53] = 1
        # line 11 = all free
        for i in range(3,54):
            _maze[11][i] = 1
        #line 12, 13, 14, 15, 16            
        for i in range(11,17):
            _maze[i][3] = _maze[i][13] =  _maze[i][19] = _maze[i][37] = \
                          _maze[i][43] = _maze[i][53] =  1

        #line 17
        for i in [ x for x in range(3, 14)]:
            _maze[17][i] = 1
        for i in [ x for x in range(19, 26)]:
            _maze[17][i] = 1
        for i in [ x for x in range(31, 38)]:
            _maze[17][i] = 1
        for i in [ x for x in range(43, 54)]:
            _maze[17][i] = 1            
        #line 18 - 22 just down
        for i in range(18, 23):
            _maze[i][25] = _maze[i][13] = _maze[i][31] = _maze[i][43] = 1

        # line 23
        for i in range(19, 38):
            _maze[23][i] =1
        _maze[23][13] = _maze[23][43] = 1

        # line 24-28 just down
        for i in range(24,29):
            _maze[i][13] = _maze[i][19] = _maze[i][37] = _maze[i][43] = 1
        # line 29 The tunnel
        for i in range(0, 20):
            _maze[29][i] = 1
        for i in range(37, 56):
            _maze[29][i] = 1
            
           
        # line 30-34
        for i in range(30,35):
            _maze[i][13] = _maze[i][19] = _maze[i][37] = _maze[i][43] = 1
        # line 35
        for i in range(19, 38):
            _maze[35][i] =1
        _maze[35][13] = _maze[35][43] = 1

        # line 36-40 just down
        for i in range(36,41):
            _maze[i][13] = _maze[i][19] = _maze[i][37] = _maze[i][43] = 1

        # line 41
        for i in range(3, 26):
            _maze[41][i] = 1
        for i in range(31, 54):
            _maze[41][i] = 1

        # line 42-46
        for i in range(42, 47):
           _maze[i][3] = _maze[i][13] = _maze[i][25] = \
            _maze[i][31] = _maze[i][43] = _maze[i][53] = 1            

        # line 47
        for i in range(3, 8):
            _maze[47][i] = 1
        for i in range(13, 44):
            _maze[47][i] = 1
        for i in range(49, 54):
            _maze[47][i] = 1
        
        # line 48-52
        for i in range(48, 53):
           _maze[i][7] = _maze[i][13] = _maze[i][19] = \
            _maze[i][37] = _maze[i][43] = _maze[i][49] = 1

        #line 53
        for i in range(3, 14):
            _maze[53][i] = 1

        for i in range(19, 26):
            _maze[53][i] = 1
        for i in range(31, 38):
            _maze[53][i] = 1
        for i in range(43,54):
            _maze[53][i] = 1            

        #line 54-58
        for i in range(54, 59):
            _maze[i][3] = _maze[i][25] = _maze[i][31] = _maze[i][53] = 1

        #line 59 all free
        for i in range(3,54):
            _maze[59][i] = 1        
        
        return _maze
        
