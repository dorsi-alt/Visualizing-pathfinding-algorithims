class Node:
#     def __init__(self, row, col, width, total_rows):
#         self.rows = row
#         self.col = col
#         self.width = width
#         self.x = col*width
#         self.y = row*width
#         self.color = White
#         self.neighbors = []
#         self.total_rows = total_rows

#     def getPosition(self):
#         return self.row, self.col
    
#     #different positions of the node
#     def is_closed(self):
#         return self.color == Red
    
#     def is_open(self):
#         return self.color == Green
    
#     def is_barrier(self):
#         return self.color == Black
    
#     def is_start(self):
#         return self.color == Orange

#     def is_end(self):
#         return self.color == Blue

#     def reset(self):
#         self.color == White

#     # setting nodes to specified colors

#     def make_closed(self):
#         self.color = Red
    
#     def make_open(self):
#         self.color = Green
    
#     def make_barrier(self):
#         self.color = Black
    
#     def make_start(self):
#         self.color = Orange

#     def make_end(self):
#         self.color = Blue

#     def make_path(self):
#         self.color = Purple

#     def draw(self, win):
#         py.draw.rect(win, self.color,(self.x, self.y, self.width, self.width))
    
#     def update_neighbors(self, grid):
#         pass




        




# def main():
#     pass


# if __name__ == "__main__":
#     main()