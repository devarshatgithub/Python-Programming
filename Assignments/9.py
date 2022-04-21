class Point(object):
    pass
class Rectangle(object):
    pass
top_right=Point()
top_right.x=10.0
top_right.y=5.0
bottom_left=Point()
bottom_left.x=7.0
bottom_left.y=4.0
rect = Rectangle()
rect.corner_tr = top_right
rect.corner_bl = bottom_left
def move_rectangle(rect, x, y):
    print(f"Rectangle Initial coordinates:\n\ttop-right: ({rect.corner_tr.x},{rect.corner_tr.y})\n\tbottom-left: ({rect.corner_bl.x},{rect.corner_bl.y})")
    rect.corner_tr.x += x
    rect.corner_bl.x += x
    rect.corner_tr.y += y
    rect.corner_bl.y += y
    print(f"Rectangle Moved to the coordinates:\n\ttop-right: ({rect.corner_tr.x},{rect.corner_tr.y})\n\tbottom-left: ({rect.corner_bl.x},{rect.corner_bl.y})")
dx,dy = map(int, input().split())
move_rectangle(rect, dx, dy)