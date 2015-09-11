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
        self.maze = [ [0] * 62 for x in range(56)]
        self.maze[3][3] = 1
        # first path line line #3
        for i in range(3,26):
            self.maze[i][3] = 0
        for i in range(31,54):
            self.maze[i][3] = 0
        # line #4,5,6,7,8.9,10 allow just down/up on the intersection
        for i in range(4,11)
            self.maze[3][i] = self.maze[13][i] = self.maze[25][i] = self.maze[31][i] = self.maze[43][i] = self.maze[53][i] = 1
        # line 11 = all free
        for i in range(3,54):
            self.maze[i][11] = 1
        print("MAZZZZZZZE")
        return self.maze
        
        
            
                
        
