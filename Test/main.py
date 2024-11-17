def run(points: str) -> str:
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

    for point in points:
        
        if tiebreak:
            if point == 'A':
                points_a += 1
            else:
                points_b += 1

            if points_a == TIEBREAK_WIN:
                set_A += 1
                result += f'{points_a}-{points_b} '
                game_a = 0
                game_b = 0
                points_a = 0
                points_b = 0
                tiebreak = False
            elif points_b == TIEBREAK_WIN:
                set_B += 1
                result += f'{points_a}-{points_b} '
                game_a = 0
                game_b = 0
                points_a = 0
                points_b = 0
                tiebreak = False
                
        else:
            if point == 'A':
                points_a += 1
            else:
                points_b += 1

            if points_a >= GAME_WIN_POINTS and points_a - points_b >= 2:
                game_a += 1
                points_a = 0
                points_b = 0
            elif points_b >= GAME_WIN_POINTS and points_b - points_a >= 2:
                game_b += 1
                points_a = 0
                points_b = 0

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

            if game_a == SET_WIN_GAMES and game_b == SET_WIN_GAMES:
                tiebreak = True
                
    result = result.strip()
    return result

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)