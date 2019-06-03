#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#detects if destination is valid and is an integer
def can_move(matrix,destination):
    try:
        if isinstance(matrix[destination[1]][destination[0]],int):
            return True
    except:
        return False
    return False

#move_r and move_d detects if its possible to move and does if it is
def move_r(matrix,current_coord):
    next_coord = [current_coord[0] + 1,current_coord[1]]
    if can_move(matrix,next_coord):
        return next_coord
    return current_coord

def move_d(matrix,current_coord):
    next_coord = [current_coord[0],current_coord[1] + 1]
    if can_move(matrix,next_coord):
        return next_coord
    return current_coord

#creates a fresh grid. all unavailable coordinates will be marked out with "x"
def fresh_grid(length,width):
    grid = [[x
             for x in range(length)]
            for y in range(width)]
    #for this method, the points under the top left are useless
    #grid[1:][0] = "x"
    #why isnt that working?
    return grid

#for any given grid (except for those lengths or widths equal to 1) tells how many paths can be taken
def path_count(length,width):
    length += 1
    width += 1
    count = 0
    
    grid = fresh_grid(length,width)
    '''
    print("-----")
    print("\n".join([" ".join(["{:^2}".format(item) 
                               for item in row])
                     for row in grid]))
    print("-----")
    '''

    target_column = length - 1
    
    while target_column > 1:        
        for y_pos in range(width - 1):
            
            x_pos_list = []
            for i in range(length - target_column):
                if y_pos != 0:
                    x_pos_list.append((length - 1) - i)
                else:
                    x_pos_list.append(target_column)
                    break
            
            for x_pos in x_pos_list:
                
                #print("Pathing around ({},{})".format(x_pos,y_pos))
                
                #"mouse" placed at (0, 0) and moves to the right and when it cant moves down 1 and stops when it reaches (20, 20)
                mouse_coord = [0,0]
                while mouse_coord != [length - 1,width - 1]:
                    #print("Mouse is now at: {}".format(mouse_coord))
                    while can_move(grid,[mouse_coord[0] + 1,mouse_coord[1]]):
                        mouse_coord = move_r(grid,mouse_coord)
                        #print("Mouse is then at: {}".format(mouse_coord))
                    mouse_coord = move_d(grid,mouse_coord)
                
                count += 1
                #print("Count: {}".format(count))
                
                grid[y_pos][x_pos] = "x"
                '''
                print("-----")
                print("\n".join([" ".join(["{:^2}".format(item) 
                                           for item in row])
                                 for row in grid]))
                print("-----")
                '''
            
        target_column -= 1
        
        grid = fresh_grid(length,width)
        
    count += 1
    
    target_row = width - 1
    
    while target_row > 1:        
        for x_pos in range(length - 1):
            
            y_pos_list = []
            for i in range(width - target_row):
                if x_pos != 0:
                    y_pos_list.append((width - 1) - i)
                else:
                    y_pos_list.append(target_row)
                    break
            
            for y_pos in y_pos_list:
                
                #print("Pathing around ({},{})".format(x_pos,y_pos))
                
                #"mouse" placed at (0, 0) and moves down and when it cant moves right 1 and stops when it reaches (20, 20)
                mouse_coord = [0,0]
                while mouse_coord != [length - 1,width - 1]:
                    #print("Mouse is now at: {}".format(mouse_coord))
                    while can_move(grid,[mouse_coord[0],mouse_coord[1] + 1]):
                        mouse_coord = move_d(grid,mouse_coord)
                        #print("Mouse is then at: {}".format(mouse_coord))
                    mouse_coord = move_r(grid,mouse_coord)
                
                count += 1
                #print("Count: {}".format(count))
                
                grid[y_pos][x_pos] = "x"
                '''
                print("-----")
                print("\n".join([" ".join(["{:^2}".format(item) 
                                           for item in row])
                                 for row in grid]))
                print("-----")
                '''
            
        target_row -= 1
        
        grid = fresh_grid(length,width)
    
    count += 1
    
    return count
#this also works
def formula(n):
    n = 2 * (n + (n - 1) * (0.5 * n * (n - 1)))
    return n

for m in range(20):
    n = m + 1
    if path_count(n,n) == int(formula(n)):
        print("{}: {}".format(n,int(formula(n))))