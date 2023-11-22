at(door, monkey).
at(window, box).
at(ceiling, banana).

% Move actions
move(state(P, P, B), grasp, state(P, P, B)). % grab banana
move(state(P, M, B), climb, state(P, M, B)). % climb box
move(state(P1, M, B), push(P1, P2), state(P2, M, B)) :- opposite(P1, P2), at(P1, box). % push box

% Opposite sides of the room
opposite(door, window).
opposite(window, door).

% Goal state: monkey has banana
goal_state(state(ceiling, _, banana)).

% Solve the problem
solve(State, Actions) :-
    goal_state(State), % If already in goal state, no actions needed
    Actions = [].

solve(State, [Action | Rest]) :-
    move(State, Action, NextState),
    solve(NextState, Rest).