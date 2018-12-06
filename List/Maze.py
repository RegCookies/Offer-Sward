class Maze:
    def __init__(self):
        self.N = 4
    
    def printsol(self,sol):
        print(sol)
    
    def isSafe(self,maze,x,y):  
        return x>= 0 and y >= 0 and x < self.N and y < self.N and maze[x][y] == 1
    
    def getPath(self,maze,x,y,sol):
        if x == self.N -1 and y == self.N -1 :
            sol[x][y] = 1
            return True
        if self.isSafe(maze,x,y):
            sol[x][y] =1
            if self.getPath(maze,x+1,y,sol):
                return True
            if self.getPath(maze,x,y+1,sol):
                return True
            sol[x][y] = 0
            return False
        return False
    
if __name__ == "__main__":
    rat = Maze()

    maze = [[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,1,1,1]]

    sol = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    rat.getPath(maze,0,0,sol)

    rat.printsol(sol)