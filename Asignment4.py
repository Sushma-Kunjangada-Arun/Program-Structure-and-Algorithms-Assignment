############################################################
# Exam.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2024
###########################################################


############################################################
#  NOTHING CAN BE CHANGED BELOW
###########################################################
class Solution:
    def isEscapePossible(self, b: 'List of list of size 2', s:'list of size 2', t:'list of size 2') -> bool:
        show = False
        R = 1000000
        C = 1000000
        dir = [[-1,0],[1,0],[0,-1],[0,1]]
        work = [0]
        ans = [] #all directions you explored
        is_escape_possible = [False] #True/False
        s = Exam(R,C,b,s,t,dir,is_escape_possible,ans,work,show)
        return is_escape_possible[0]


########################################
#Nothing can be changed in class Exam
########################################
class Exam:
    def __init__(self, 
          r:'int', #Max rows
          c:'int', #Max columns
          blocked: 'List of list of size 2', #[[0,1],[1,0]]
          source: 'list of size 2', #[0,0]
          target: 'list of size 2', #[0,2]
          dir:'list of list', #[[0,1],[1,0]] #Direction you can move from current position
          is_escape_possible:'List of size 1', #True/False
          ans:'list of list', #You fill all directions that you explored
          work:'List of size 1',#You fill number of steps
          show:'Bool',#if show is True, show each step of the algorithm
        )->'None':

        self._r = r
        self._c = c
        self._blocked = blocked
        self._dir = dir
        self._is_escape_possible = is_escape_possible
        self._ans = ans
        self._work = work
        self._show = show

        #YOU CAN HAVE your data structure. All must be private
        self._blocked_set = set(map(tuple, blocked))
        
        
        # MUST WRITE THIS ROUTINE
        self._alg(source, target) #this will fill self._is_escape_possible[0] True or False

        

    ############################################################
    # TIME: O(n2)
    # SPACE: O(n2)
    ############################################################
    def _alg(self, source, target) -> 'None':
        visited = set()
        self._is_escape_possible[0] = self._dfs(tuple(source), tuple(target), visited)

    def _dfs(self, source, target, visited) -> bool:
        if source == tuple(target):
            return True

        if source in visited or source in self._blocked_set or not (0 <= source[0] < self._r and 0 <= source[1] < self._c):
            return False

        visited.add(source)
        self._append_ans(list(source))
        self._increment_work()

        for val in self._dir:
            new_x, new_y = source[0] + val[0], source[1] + val[1]
            if self._dfs((new_x, new_y), target, visited):
                return True

        return False
  
       

    ############################################################
    # TIME: THETA(1)
    # SPACE: THETA(1)
    ############################################################
    def _increment_work(self)->'None':
        self._work[0] += 1

    ############################################################
    # TIME: THETA(1)
    # SPACE: THETA(1)
    ############################################################
    def _append_ans(self,n:'list of [x,y]'):
        self._ans.append(n)

          
############################################################
#  NOTHING CAN BE CHANGED BELOW. THIS MUST BE LAST
#
'''
    2
    4
    1 1 1 1
    1 1 1 1
    1 1 1 1
    1 1 1 1
    3
    1 0 0
    0 0 0
    0 0 1

    output
    POSSIBLE
    NOT POSSIBLE
'''
###########################################################
if (True): 
  n = int(input().strip()) #Number of testcase
  for i in range(n):
    b = [] #
    s = [0,0]        
    d = [[0,1],[1,0]] #Direction you can move from current position 
    N =  int(input().strip()) # size of matrix
    t = [N-1,N-1]
    for j in range(N):
      row = list(map(int, input().strip().split()))
      for k in range(N):
        if (row[k] == 0):
          #0 is blocked position
          b.append([j,k])
    work = [0]
    ans = [] #all directions you explored
    is_escape_possible = [False] #True/False
    s = Exam(N,N,b,s,t,d,is_escape_possible,ans,work,False)
    if (is_escape_possible[0]):
        print("POSSIBLE")
    else:
        print("NOT POSSIBLE")


