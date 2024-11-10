def run(points: str) -> str:
    game_A = 0
    game_B = 0
    set_A = 0
    set_B = 0
    A_points = 0
    B_points = 0
    result= ''

    for point in points:
        if point == 'A':
            A_points += 1
        else:
            B_points += 1
# Aqui se van contando los juegos antes de que sea el fin del partido 

        if A_points >= 4 and A_points - B_points >= 2:
            game_A += 1
            A_points = 0
            B_points = 0
        elif B_points >= 4 and B_points - A_points >= 2:
            game_B += 1
            A_points = 0
            B_points = 0




    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
