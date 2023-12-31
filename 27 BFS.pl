edge(a, b, 4).
edge(a, c, 2).
edge(b, d, 5).
edge(c, e, 7).
edge(d, e, 3).

% Best-First Search algorithm
best_first_search(Start, Goal, Path) :-
    bfs([Start], Goal, Path).

% Helper predicate for Best-First Search
bfs([Goal | _], Goal, [Goal]) :- !.

bfs([Current | Rest], Goal, [Current | Path]) :-
    findall(
        Next,
        (edge(Current, Next, _), \+ member(Next, Rest)),
        Children
    ),
    append(Rest, Children, NewQueue),
    bfs(NewQueue, Goal, Path).