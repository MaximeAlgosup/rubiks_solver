def to_face(cube, new_face):
    # Check if the cube is already complete with the new face
    if is_cube_complete(cube, new_face):
        return

    # Set edges to make the cross
    for i in [1, 7, 3, 5]:
        match i:
            case 1:
                # Set the top edge color
                set_top_edge_color(cube, new_face[1])
            case 3:
                # Set the left edge color
                set_left_edge_color(cube, new_face[3])
            case 5:
                # Set the right edge color
                set_right_edge_color(cube, new_face[5])
            case 7:
                # Set the bottom edge color
                set_bottom_edge_color(cube, new_face[7])

        # Check if the cube is complete after setting an edge
        if is_cube_complete(cube, new_face):
            return

    # Set corners to finish the face
    for i in [0, 2, 6, 8]:
        match i:
            case 0:
                # Set the top-left corner color
                set_top_left_corner_color(cube, new_face[0])
            case 2:
                # Set the top-right corner color
                set_top_right_corner_color(cube, new_face[2])
            case 6:
                # Set the bottom-left corner color
                set_bottom_left_corner_color(cube, new_face[6])
            case 8:
                # Set the bottom-right corner color
                set_bottom_right_corner_color(cube, new_face[8])

        # Print the current corner index
        print(i)
        # Print the moves performed after setting a corner
        print(cube.get_moves())

        # Check if the cube is complete with the new face
        if is_cube_complete(cube, new_face):
            return


def set_top_edge_color(cube, color):
    if cube.get_matrix_cube()[2][1] == color:
        return True
    top_edges = cube.get_top_crown_edges()
    for edge in top_edges:
        if edge["color"] == color:
            moves_executor(cube, edge["moves"])
            return True


def set_bottom_edge_color(cube, color):
    if cube.get_matrix_cube()[2][7] == color:
        return True
    bottom_edges = cube.get_bottom_crown_edges()
    for edge in bottom_edges:
        if edge["color"] == color:
            moves_executor(cube, edge["moves"])
            return True


def set_left_edge_color(cube, color):
    if cube.get_matrix_cube()[2][3] == color:
        return True
    left_edges = cube.get_left_crown_edges()
    for edge in left_edges:
        if edge["color"] == color:
            moves_executor(cube, edge["moves"])
            return True


def set_right_edge_color(cube, color):
    if cube.get_matrix_cube()[2][5] == color:
        return True
    right_edges = cube.get_right_crown_edges()
    for edge in right_edges:
        if edge["color"] == color:
            moves_executor(cube, edge["moves"])
            return True


def set_top_left_corner_color(cube, color):
    if cube.get_matrix_cube()[2][0] == color:
        return True
    top_left_corners = cube.get_top_left_corners()
    for corner in top_left_corners:
        if corner["color"] == color:
            moves_executor(cube, corner["moves"])
            return True


def set_top_right_corner_color(cube, color):
    if cube.get_matrix_cube()[2][2] == color:
        return True
    top_right_corners = cube.get_top_right_corners()
    for corner in top_right_corners:
        if corner["color"] == color:
            moves_executor(cube, corner["moves"])
            return True


def set_bottom_left_corner_color(cube, color):
    if cube.get_matrix_cube()[2][6] == color:
        return True
    bottom_left_corners = cube.get_bottom_left_corners()
    for corner in bottom_left_corners:
        if corner["color"] == color:
            moves_executor(cube, corner["moves"])
            return True


def set_bottom_right_corner_color(cube, color):
    if cube.get_matrix_cube()[2][8] == color:
        return True
    bottom_right_corners = cube.get_bottom_right_corners()
    for corner in bottom_right_corners:
        if corner["color"] == color:
            moves_executor(cube, corner["moves"])
            return True


def is_cube_complete(cube, new_face):
    return all(cube.get_matrix_cube()[2][i] == new_face[i] for i in range(9))


def moves_executor(cube, moves):
    for move in moves:
        match move[0]:
            case "U":
                cube.move_u(move[1])
            case "U'":
                cube.move_u_p(move[1])
            case "D":
                cube.move_d(move[1])
            case "D'":
                cube.move_d_p(move[1])
            case "L":
                cube.move_l(move[1])
            case "L'":
                cube.move_l_p(move[1])
            case "R":
                cube.move_r(move[1])
            case "R'":
                cube.move_r_p(move[1])
            case "F":
                cube.move_f(move[1])
            case "F'":
                cube.move_f_p(move[1])
            case "B":
                cube.move_b(move[1])
            case "B'":
                cube.move_b_p(move[1])
