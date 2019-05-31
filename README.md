# N-Queens
A solution to the N-Queens problem by applying the minimum conflicts heuristic.

The N-Queens problem is defined as finding
the locations for _n_ number of queen chess pieces on a board of size n*n such that no one queen could capture any
other in a single legal move (A queens can legally move _up_, _down_, _left_, _right_, or on any _diagonal_ (45°) an
indefinite number of spaces). The minimum conflicts heuristic is applied using two steps; the initialization of a board with an
incomplete solution and fixing that partial solution by repeatedly moving queens along their row to one of
the positions with the lowest number of _conflicts_ (instances where queens can capture one another). This solution also uses a greedy algorithm to initialize the board in O(n) time and results in a constant number (independant of n) of fixing steps for the min-conflicts heuristic. This solution is O(n) overall.
