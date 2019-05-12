import Task_6_21.game.gameitem as gi


# load level
def load_level(filepath):
    field = []
    with open(filepath, 'r') as level:
        for row in level:
            tmpRow = []
            for i in row:
                if str.isdigit(i):
                    tmpRow.append(gi.GameItem(not bool(int(i))))
            field.append(tmpRow)
    return field


