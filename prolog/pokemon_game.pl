:-ensure_loaded("pokemon_list.pl").
:-ensure_loaded("pokemon_info_attacks.pl").
:-ensure_loaded("pokemon_route.pl").

player_starts(0,0).

% TO DO-Feito
next_rooms(X, Y, Rooms) :-
    route(M),
    findall(Room, obter_room(X, Y, M, Room), Rooms).

elemento_zero(0, [X|_], X).
elemento_zero(N, [_|T], Y) :- 
    M is N-1, 
    elemento_zero(M, T, Y).

% 2. Como verificar as 4 direções e não sair do mapa
% Direita
vizinho_valido(X, Y, M, NextX, NextY, Id, Level) :-
    NextX is X + 1, NextY is Y,
    elemento_zero(NextY, M, Linha),
    elemento_zero(NextX, Linha, (Id, Level)).

% Esquerda
vizinho_valido(X, Y, M, NextX, NextY, Id, Level) :-
    NextX is X - 1, NextY is Y,
    elemento_zero(NextY, M, Linha),
    elemento_zero(NextX, Linha, (Id, Level)).

% Baixo
vizinho_valido(X, Y, M, NextX, NextY, Id, Level) :-
    NextX is X, NextY is Y + 1,
    elemento_zero(NextY, M, Linha),
    elemento_zero(NextX, Linha, (Id, Level)).

% Cima
vizinho_valido(X, Y, M, NextX, NextY, Id, Level) :-
    NextX is X, NextY is Y - 1,
    elemento_zero(NextY, M, Linha),
    elemento_zero(NextX, Linha, (Id, Level)).

% 3. Como juntar os dados do quarto e os dados do Pokémon
obter_quarto(X, Y, M, [Id, Name, Level, NextX, NextY, Types]) :-
    vizinho_valido(X, Y, M, NextX, NextY, Id, Level),
    pokemon(Id, Name, Types).