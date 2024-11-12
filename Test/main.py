def run(points: str) -> str:
    A_points = 0
    B_points = 0
    game_A = 0
    game_B = 0
    set_A = 0
    set_B = 0
    result= ''
    point_index = 0
    for point in points:
        if point == 'A':
            if A_points == 30:
                A_points += 10
            else:
                A_points += 15
        else:
            if B_points == 30:
                B_points += 10
            else:
                B_points += 15
                
        if A_points == 40 and B_points < 40:
                game_A += 1
                A_points = 0
                B_points = 0
                point_index += 1
        elif B_points == 40 and A_points < 40:
                game_B += 1
                A_points = 0
                B_points = 0
                point_index += 1
        elif A_points == 40 and B_points == 40:
            if point_index + 1 < len(points):
                if points[point_index + 1] == 'A' and points[point_index + 2] == 'A':
                    game_A += 1
                    A_points = 0
                    B_points = 0
                elif points[point_index + 1] == 'B' and points[point_index + 2] == 'B':
                    game_B += 1
                    A_points = 0
                    B_points = 0
                    
        point_index += 1
        
    # Faltan contar sets y algunas cosas mas
             
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
