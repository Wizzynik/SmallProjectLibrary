# Example file showing a circle moving on screen
import copy
import pygame

class Game:
    # Constants: standart (3,3) = 3x3
    FIELD_DIMENSIONS = (3, 3)
    SQUARE_SIZE_PX = None
    CIRCLE_COLOR = (0,0,200)
    CROSS_COLOR = (200,0,0)
    # Variables
    fields = []
    const_start_values = None
    
    # pygame setup
    running = True
    screen = None
    clock = None
    
    def __init__(self):
        pygame.init()
        # Screen setup
        print("Screen setup")
        self.cal_square_size()
        width = self.FIELD_DIMENSIONS[0] * self.SQUARE_SIZE_PX
        height = self.FIELD_DIMENSIONS[1] * self.SQUARE_SIZE_PX
        self.screen = pygame.display.set_mode((width, height))
        # Clock setup
        print("Clock setup")
        self.clock = pygame.time.Clock()
        self.running = True
        
    def cal_square_size(self):
        # Calculate square size in px based Dimensions and screen size
        x_dim = self.FIELD_DIMENSIONS[0]
        y_dim = self.FIELD_DIMENSIONS[1]
        # get screen size
        width = pygame.display.Info().current_w
        height = pygame.display.Info().current_h
        # calculate square size
        self.SQUARE_SIZE_PX = int(0.8 * min((width // x_dim), (height // y_dim)))
        
    def init_Map(self):
        x_dim = self.FIELD_DIMENSIONS[0]
        y_dim = self.FIELD_DIMENSIONS[1]
        self.fields = [[0 for x in range(x_dim)] for y in range(y_dim)]
        
    def draw_Map(self):
        x = 0
        y = 0
        for i in range(self.FIELD_DIMENSIONS[0]):
            for j in range(self.FIELD_DIMENSIONS[1]):
                x = i * self.SQUARE_SIZE_PX
                y = j * self.SQUARE_SIZE_PX
                pygame.draw.rect(self.screen, (0,0,0), (x,y,self.SQUARE_SIZE_PX,self.SQUARE_SIZE_PX), 1)
                
    def draw_Fields(self):
        for i in range(self.FIELD_DIMENSIONS[0]):
            for j in range(self.FIELD_DIMENSIONS[1]):
                x = i * self.SQUARE_SIZE_PX
                y = j * self.SQUARE_SIZE_PX
                if self.fields[i][j] == "o":
                    self.draw_Circle(x, y, self.CIRCLE_COLOR)
                elif self.fields[i][j] == "x":
                    self.draw_Cross(x, y, self.CROSS_COLOR)
                
    def draw_Circle(self, x, y, color=(0,0,0)):
        pad = 30 # padding in px
        width = 10
        size = self.SQUARE_SIZE_PX
        pygame.draw.circle(self.screen, color, (x+size//2, y+size//2), size//2-pad, width)
    
    def draw_Cross(self, x,y,color=(0,0,0)):
        pad = 30 # padding in px
        width = 12
        pygame.draw.line(self.screen, color, (x+pad,y+self.SQUARE_SIZE_PX-pad), (x+self.SQUARE_SIZE_PX-pad, y+pad), width)
        pygame.draw.line(self.screen, color, (x+pad,y+pad), (x+self.SQUARE_SIZE_PX-pad, y+self.SQUARE_SIZE_PX-pad), width)
        
    def search_connected_recursive(self, x, y, dx, dy, list=[]):
        if x < 0 or x >= self.FIELD_DIMENSIONS[0] or y < 0 or y >= self.FIELD_DIMENSIONS[1]:
            return []
        if self.fields[x][y] != 0:
            list.append(self.fields[x][y])
        return [(x,y)] + self.search_connected_recursive(x + dx, y + dy, dx, dy, list)    
        
    def check_win(self, players):
        for i in range(self.FIELD_DIMENSIONS[0]):
            for j in range(self.FIELD_DIMENSIONS[1]):
                if not (i == 0 or j == 0): continue
                # check rows
                for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                    connected = []
                    path = self.search_connected_recursive(i, j, dx, dy, connected)
                    # Count "x" and "o" in connected list
                    for player in players:
                        p_count = connected.count(player)
                        if len(path) == 3:
                            if p_count == 3:
                                return path
    
    def player_player(self, player_ox="o"):
        # register mouse clicks
        x, y = pygame.mouse.get_pos()
        x = x // self.SQUARE_SIZE_PX
        y = y // self.SQUARE_SIZE_PX
        if self.fields[x][y] == 0:
            self.fields[x][y] = player_ox
            return True
        return False
            
    def player_ai(self, player_ox="x"):
        start_values = copy.deepcopy(self.const_start_values)
        field_values, win_fields, lose_fields = self.calc_field_values()
        best_fields = []
        best_value = 0
        
        if len(win_fields) > 0:
            self.fields[win_fields[0][0]][win_fields[0][1]] = player_ox
            return
        if len(lose_fields) > 0:
            self.fields[lose_fields[0][0]][lose_fields[0][1]] = player_ox
            return
        
        for i in range(self.FIELD_DIMENSIONS[0]):
            for j in range(self.FIELD_DIMENSIONS[1]):
                if field_values[i][j] > best_value:
                    best_value = field_values[i][j]
                    best_fields.clear()
                    best_fields.append((i,j))
                elif field_values[i][j] == best_value:
                    best_fields.append((i,j))
        
        if len(best_fields) == 0: return None
        best_field = best_fields[0]
        best_value = field_values[best_field[0]][best_field[1]] - start_values[best_field[0]][best_field[1]]
        for field in best_fields:
            value = field_values[field[0]][field[1]] - start_values[field[0]][field[1]]
            if value < best_value:
                best_value = value
                best_field = field
                
        self.fields[best_field[0]][best_field[1]] = player_ox
        
    def calc_field_startvalues(self):
        start_values = [[0 for x in range(self.FIELD_DIMENSIONS[0])] for y in range(self.FIELD_DIMENSIONS[1])]
        
        for i in range(self.FIELD_DIMENSIONS[0]):
            for j in range(self.FIELD_DIMENSIONS[1]):
                if self.fields[i][j] != 0: continue
                if not (i == 0 or j == 0): continue
                # check rows
                possible_wins = 0
                for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                    path = self.search_connected_recursive(i, j, dx, dy)
                    if len(path) == 3:
                        for x, y in path:
                            start_values[x][y] += 1
        
        return start_values       
                    
    def calc_field_values(self, players=["x"], opponents=["o"]):
        win_fields = []
        lose_fields = []
        field_values = copy.deepcopy(self.const_start_values)
        
        for field in field_values:
            print(field)
        
        for i in range(self.FIELD_DIMENSIONS[0]):
            for j in range(self.FIELD_DIMENSIONS[1]):
                if self.fields[i][j] != 0: 
                    field_values[i][j] = -1
                    print ("Field", i, j, "set to -1")
                if not (i == 0 or j == 0): continue
                
                pathcount = 0
                
                for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                    connected = []
                    path = self.search_connected_recursive(i, j, dx, dy, connected)
                    # Count "x" and "o" in connected list
                    p_count = connected.count(players[0])
                    o_count = connected.count(opponents[0])
                    
                    pathcount += 1
                    
                    if len(path) == 3:
                        if p_count == 2:
                            for x, y in path:
                                if self.fields[x][y] == 0: 
                                    win_fields.append((x, y))
                        elif o_count == 2:
                            for x, y in path:
                                if self.fields[x][y] == 0: 
                                    lose_fields.append((x, y))
                        # Decrease value for lost line connections
                        elif o_count > 0:
                            for x, y in path:
                                if self.fields[x][y] == 0: 
                                    field_values[x][y] -= 1
                        # Increse value for more friendly line connections
                        elif p_count > 0:
                            for x, y in path:
                                if self.fields[x][y] == 0: 
                                    field_values[x][y] += 1
                                    
        for field in field_values:
            print(field)
            
        for field in self.fields:
            print(field)
        
        print ("Win fields: ", win_fields)
        print ("Lose fields: ", lose_fields)
        return field_values, win_fields, lose_fields
                
    def reset (self):
        self.init_Map()
                
    def run(self):
        # Initialize the map
        self.reset()

        frame_count = 0
        dt = 0  # delta time

        game_over = False
        players = ["o", "x"]
        player_state = 1
        mode = 0  # 0 = pvp, 1 = pvai
        self.const_start_values = self.calc_field_startvalues()

        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            turn_is_over = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset()
                        self.calc_field_startvalues()
                        game_over = False
                        player_state = 1
                    elif event.key == pygame.K_m:
                        mode = (mode + 1) % 2
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not game_over and mode == 0:
                        if event.button == 1:  # Linke Maustaste
                            if player_state % 2 == 0:
                                if self.player_player("o"):
                                    player_state += 1
                            else:
                                if self.player_player("x"):
                                    player_state += 1
                    if not game_over and not turn_is_over and mode == 1:
                        if not player_state % 2 == 0:
                            if self.player_player("o"):
                                player_state += 1
                                turn_is_over = True
                # AI call
                if not game_over and not turn_is_over and player_state % 2 == 0 and mode == 1:
                    self.player_ai("x")
                    player_state += 1
                    turn_is_over = True
                            
                            

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("white")

            # draw the map
            self.draw_Map()

            # draw the fields
            self.draw_Fields()

            # check for win
            for player in players:
                win = self.check_win(player)
                if win:
                    pygame.draw.line(self.screen, (0, 0, 0), 
                                     (win[0][0] * self.SQUARE_SIZE_PX + self.SQUARE_SIZE_PX // 2, 
                                      win[0][1] * self.SQUARE_SIZE_PX + self.SQUARE_SIZE_PX // 2), 
                                     (win[2][0] * self.SQUARE_SIZE_PX + self.SQUARE_SIZE_PX // 2, 
                                      win[2][1] * self.SQUARE_SIZE_PX + self.SQUARE_SIZE_PX // 2), 8)
                    game_over = True

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            dt = self.clock.tick(60) / 1000
                
        
# Start the game
if __name__ == "__main__":
    game = Game()
    game.run()