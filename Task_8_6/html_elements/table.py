def table(x,y):
    buff = '<table style="border-collapse: collapse;border: 1px solid black;"><tr style="border: 1px solid black;"><td style="border: 1px solid black;">x</td>{}</tr><tr style="border: 1px solid black;"><td style="border: 1px solid black;">y</td>{}</tr></table>'
    row1 = ''
    for _ in x:
        row1 += '<td style="border: 1px solid black;">{}</td>'.format(str(_))
    row2 = ''
    for _ in y:
        row2 += '<td style="border: 1px solid black;">{}</td>'.format(str(_))
    buff = buff.format(row1, row2)
    return buff


# Собирает html представление таблицы
def table2(t):
	return  '<table style="border-collapse: collapse;border: 1px solid black;"><tr style="border: 1px solid black;">{}</tr></table>'.format(
       '</tr><tr>'.join(
           '<td style="border: 1px solid black;">{}</td>'.format('</td><td style="border: 1px solid black;">'.join(str(_) for _ in row)) for row in t)
       )