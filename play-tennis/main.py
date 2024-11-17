def run(points: str) -> str:
# Pista de Sergio: Los tail breaks (cuando se llega a 7) son un juego nuevo
    GAME_WIN_POINTS = 4
    SET_WIN_GAMES = 6
    TIEBREAK_WIN = 7

    game_a = 0
    game_b = 0
    set_A = 0
    set_B = 0
    points_a = 0
    points_b = 0
    result = ''
    tiebreak = False
    
    # Aqui abajo se cuentan los puntos

    for point in points:
        if point == 'A':
            points_a += 1
        else:
            points_b += 1

    # aqui se cuentan los juegos (game_a y game_b)

        if points_a >= GAME_WIN_POINTS and points_a - points_b >= 2:
            game_a += 1
            points_a = 0
            points_b = 0
        elif points_b >= GAME_WIN_POINTS and points_b - points_a >= 2:
            game_b += 1
            points_a = 0
            points_b = 0
       
    # aqui los sets(set_A y set_B)
                 
        if game_a >= SET_WIN_GAMES and game_a - game_b >= 2:
            set_A += 1
            result += f'{game_a}-{game_b} '
            game_a = 0
            game_b = 0
        elif game_b >= SET_WIN_GAMES and game_b - game_a >= 2:
            set_B += 1
            result += f'{game_a}-{game_b} '
            game_a = 0
            game_b = 0

    # Tiebreak (Esto no va pero no se me ocurre nada mas)
        if points_a >= TIEBREAK_WIN and points_a - points_b >= 2:
                set_a += 1
                result += f'{game_a}-{game_b} '
                game_a = 0
                game_b = 0
                points_a = 0
                points_b = 0
                tiebreak = False
        elif points_b >= TIEBREAK_WIN and points_b - points_a >= 2:
                set_b += 1
                result += f'{game_a}-{game_b} '
                game_a = 0
                game_b = 0
                points_a = 0
                points_b = 0
                tiebreak = False

        
    if game_a > 0 or game_b > 0:
        result += f'{game_a}-{game_b} '

    return result

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)