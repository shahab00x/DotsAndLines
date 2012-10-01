player = 0
other = { 0:1, 1:0}
player_sign = { 0:'a', 1:'b'}
score = {0:0 , 1:0}
game_over = False
GameMatrix = [i for i in range(10**2)]
GameGraph = {}
CompletedSquares = []
def new_board(n = 10, p1='a', p2='b'):
    global GameMatrix, GameGraph, CompletedSquares, player_sign, score, game_over
    player_sign = {0:p1, 1:p2}
    score = {0:0, 1:0}
    game_over = False
    GameMatrix = [i for i in range(n**2)]
    GameGraph = dict( (i, {}) for i in range(n**2))
    CompletedSquares = [None for _ in range(n**2)]
    
def connect(node1, node2, G=None, M=None):
    if not G:
        global GameGraph
        G = GameGraph
    if not M:
        global GameMatrix
        M = GameMatrix
    G[node1][node2] = node1
    G[node2][node1] = node2

def connected(node1, node2, G=None):
    if not G: 
        global GameGraph
        G = GameGraph
    return node1 in G[node2]

def check_board(G=None):
    global GameGraph, CompletedSquares, game_over, score
    if not G:
        G = GameGraph
    
    n = len(GameGraph.keys()) ** (1/2.); n = int(n)
    game_over = True
    for i in range(n**2-n):
        if not (i+1)%n: continue # to skip the edges
        if connected(i,i+1) and connected(i, i+n) and\
         connected(i+n, i+n+1) and connected(i+1, i+n+1):
            CompletedSquares[i] = player_sign[player]
            score[player]+=1
        if not CompletedSquares[i] and game_over: game_over = False # check all squares, if all have been filled the game is over
    return CompletedSquares    

def play(node1, node2, G=None):
    global GameGraph, player
    if not G: G = GameGraph
    connect(node1, node2)
    check_board(G)
    player = other[player]
    return game_over


def test():
    new_board() 
    C = [None for _ in range(10**2)]
    C[1] = player_sign[player]
    connect(1,2)
    connect(1,11)
    connect(11,12)
    connect(2,12)
    assert connected(1,2)
    assert connected(2,1)
    assert connected(4,5) == False   
    
    assert check_board() == C
    
    new_board(2)
    assert play(0, 1) == False
    assert play(0, 2) == False
    assert play(1, 3) == False
    assert play(2, 3)
    return "tests passed"
print test()