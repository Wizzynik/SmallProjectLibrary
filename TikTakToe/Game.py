# Example file showing a circle moving on screen
from turtle import pos
from attr import field
import pygame

class Game:
    # Constants: standart (3,3) = 3x3
    FIELD_DIMENSIONS = (3, 3)
    SQUARE_SIZE_PX = 300
    CIRCLE_COLOR = (0,0,200)
    CROSS_COLOR = (200,0,0)
    # Variables
    fields = []
    
    # pygame setup
    running = True
    screen = None
    clock = None
    
    def __init__(self):
        pygame.init()
        # Screen setup
        print("Screen setup")
        width = self.FIELD_DIMENSIONS[0] * self.SQUARE_SIZE_PX
        height = self.FIELD_DIMENSIONS[1] * self.SQUARE_SIZE_PX
        self.screen = pygame.display.set_mode((width, height))
        # Clock setup
        print("Clock setup")
        self.clock = pygame.time.Clock()
        self.running = True
        
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
        return [(x,y)] + self.search_connected_recursive(list, x + dx, y + dy, dx, dy)    
        
    def check_win(self, players):
        for i in range(self.FIELD_DIMENSIONS[0]):
            for j in range(self.FIELD_DIMENSIONS[1]):
                if not (i == 0 or j == 0): continue
                # check rows
                for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                    connected = []
                    path = self.search_connected_recursive(connected, i, j, dx, dy)
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
        pass
        # TODO: Implement AI
        
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
                    
    def calc_field_values(self, player_ox="x", opponent_ox="o"):
        win_fields = []
        lose_fields = []
        field_values = self.calc_field_startvalues()
        
        for i in range(self.FIELD_DIMENSIONS[0]):
            for j in range(self.FIELD_DIMENSIONS[1]):
                if not (i == 0 or j == 0): continue
                # check rows
                for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                    connected = []
                    path = self.search_connected_recursive(i, j, dx, dy, connected)
                    # Count "x" and "o" in connected list
                    p_count = connected.count(player_ox)
                    o_count = connected.count(opponent_ox)
                    
                    if len(path) == 3:
                        if p_count == 2:
                            for x, y in path:
                                if self.fields[x][y] == 0: 
                                    win_fields.append((x, y))
                        elif o_count == 2:
                            for x, y in path:
                                if self.fields[x][y] == 0: 
                                    lose_fields.append((x, y))
                    
                        
        print ("Win fields: ", win_fields)
        print ("Lose fields: ", lose_fields)
                
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

        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
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
                                    self.calc_field_values()
                            else:
                                if self.player_player("x"):
                                    player_state += 1
                                    self.calc_field_values()
                            
                            

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