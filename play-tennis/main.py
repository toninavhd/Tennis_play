def run(points: str) -> str:
    # Poner constantes en vez de números.

    game_a = 0
    game_b = 0
    set_A = 0
    set_B = 0
    points_a = 0
    points_b = 0
    result = ''

    for point in points:
        if point == 'A':
            points_a += 1
        else:
            points_b += 1
        # Aqui se van contando los juegos antes de que sea el fin del partido

        if points_a >= 4 and points_a - points_b >= 2:
            game_a += 1
            points_a = 0
            points_b = 0
        elif points_b >= 4 and points_b - points_a >= 2:
            game_b += 1
            points_a = 0
            points_b = 0

    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
