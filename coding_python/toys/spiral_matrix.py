

class spiral:

    def solve_spiral_b(self, solved, to_solve, section, m, n, start):
        if(not(start == to_solve[m-1][n-1])):
            print('yes')
            solved = self.solve_spiral_b(solved, to_solve, section+1, m, n, start+n)
        
        reversed = []
        for i in range(n):
            reversed.append(to_solve[section][i])
            
        return solved.append(reversed.reverse()) 

def main():
    spire = spiral()
    to_solve = [[1,2,3],[4,5,6],[7,8,9]]
    solved = []
    m = len(to_solve)
    n = len(to_solve[0])

    print(str(spire.solve_spiral_b(solved, to_solve, 0, m, n, to_solve[0][n-1])))

if(__name__ == "__main__"):
    main()