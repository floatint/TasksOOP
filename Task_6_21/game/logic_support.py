# Функции выделяющие максимально большой блок итемов относительно выбранного


def get_available_row(field, y, x):
    # Найдем наибольшую часть, относительно x
    left_edge = x
    while left_edge >= 0:
        if (left_edge - 1 >= 0) and field[y][left_edge - 1].is_available:
            left_edge -= 1
        else:
            break
    right_edge = x
    while right_edge < len(field[0]):
        if (right_edge + 1 < len(field[0])) and field[y][right_edge + 1].is_available:
            right_edge += 1
        else:
            break

    # не удается выделить последовательность
    if (left_edge == 0) and (right_edge == 0):
        return None

    return tuple([left_edge, right_edge])


def get_available_column(field, y, x):
    # Найдем наибольшую часть, относительно y
    top_edge = y
    while top_edge >= 0:
        if (top_edge - 1 >= 0) and field[top_edge - 1][x].is_available:
            top_edge -= 1
        else:
            break
    bottom_edge = y
    while bottom_edge < len(field):
        if (bottom_edge + 1 < len(field)) and field[bottom_edge + 1][x].is_available:
            bottom_edge += 1
        else:
            break

    # не удается выделить последовательность
    if (top_edge == 0) and (bottom_edge == 0):
        return None

    return tuple([top_edge, bottom_edge])
