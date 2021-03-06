 #This is the player script. This is where the movement and collision detection of the player is.

import SETTINGS
import EFFECTS
import INVENTORY
import pygame
import math

class Player:

    def __init__(self, pos):
        self.max_speed = SETTINGS.player_speed
        self.speed = 0
        self.angle = SETTINGS.player_angle
        self.health = SETTINGS.player_health

        self.real_x = pos[0]
        self.real_y = pos[1]

        self.color = SETTINGS.BLUE
        self.sprite = pygame.Surface([SETTINGS.tile_size / 5, SETTINGS.tile_size / 5])
        self.sprite.fill(self.color)
        self.rect = self.sprite.get_rect()
        self.rect.x = self.real_x
        self.rect.y = self.real_y
        SETTINGS.player_rect = self.rect

        self.mouse = pygame.mouse
        self.mouse.set_visible(False)
        self.sensitivity = SETTINGS.sensitivity
        self.gun = 0
        self.gunsprites_aim = []
        self.gunsprites_shoot = []

        SETTINGS.player = self
        self.collide_list = SETTINGS.all_solid_tiles + SETTINGS.npc_list
        self.solid = True
        self.dead = False
        self.last_call = 0
        self.type = 'player'

        #input variables
        self.mouse2 = 0
        self.inventory = 0
        

    def direction(self, offset, distance):
        if distance == 0:
            direction = [math.cos(math.radians(self.angle + offset)), -math.sin(math.radians(self.angle + offset))]
        else:
            direction = [(math.cos(math.radians(self.angle + offset))) * distance, (-math.sin(math.radians(self.angle + offset))) * distance]
        return direction

    def control(self, canvas):
        #Make sure the collide list is complete
        if len(self.collide_list) != len(SETTINGS.all_solid_tiles + SETTINGS.npc_list):
            self.collide_list = SETTINGS.all_solid_tiles + SETTINGS.npc_list
        #Update health
        if self.health != SETTINGS.player_health and SETTINGS.player_states['heal']:
            self.health = SETTINGS.player_health
            
        key = pygame.key.get_pressed()

        #Movement controls (WASD)
        if not self.dead:
            #Inventory open
            if not SETTINGS.player_states['invopen']:

                if SETTINGS.aiming:
                    self.sensitivity = SETTINGS.sensitivity / 3
                    self.max_speed = SETTINGS.player_speed / 3
                    if self.speed > self.max_speed:
                        self.speed = self.max_speed
                else:
                    self.sensitivity = SETTINGS.sensitivity
                    self.max_speed = SETTINGS.player_speed

                if key[pygame.K_a] or key[pygame.K_d] or key[pygame.K_w] or key[pygame.K_s]:
                    if self.speed < self.max_speed:
                        self.speed += 50
                        if self.speed > self.max_speed:
                            self.speed = self.max_speed

                else:
                    if self.speed > 0:
                        if self.last_call == 0:
                            self.move(self.direction(90, self.speed * 0.8))
                        elif self.last_call == 1:
                            self.move(self.direction(-90, self.speed * 0.8))
                        elif self.last_call == 2:
                            self.move(self.direction(0, self.speed))
                        elif self.last_call == 3:
                            self.move(self.direction(0, -self.speed * 0.5))
                            
                        self.speed -= 80
                        
                        if self.speed < 1:
                            self.speed = 0
                    
                if key[pygame.K_a]:
                    self.move(self.direction(90, self.speed * 0.8))
                    self.last_call = 0
                if key[pygame.K_d]:
                    self.move(self.direction(-90, self.speed * 0.8))
                    self.last_call = 1
                if key[pygame.K_w]:
                    self.move(self.direction(0, self.speed))
                    self.last_call = 2
                if key[pygame.K_s]:
                    self.move(self.direction(0, -self.speed * 0.5))
                    self.last_call = 3

                SETTINGS.player_states['cspeed'] = self.speed


        #Shoot gun (Mouse input)
                if pygame.mouse.get_pressed()[2] and self.mouse2 < 1:
                    SETTINGS.mouse2_btn_active = True
                    self.mouse2 += 1
                elif self.mouse2 >= 1:
                    SETTINGS.mouse2_btn_active = False
                if not pygame.mouse.get_pressed()[2]:
                    self.mouse2 = 0
                
                if pygame.mouse.get_pressed()[0] and not SETTINGS.player_states['dead']:
                    SETTINGS.mouse_btn_active = True
                else:
                    SETTINGS.mouse_btn_active = False
                    
                if key[pygame.K_r]:
                    SETTINGS.reload_key_active = True
                else:
                    SETTINGS.reload_key_active = False

        #Change gun
                if key[pygame.K_1] and SETTINGS.inventory['primary']:
                    SETTINGS.next_gun = SETTINGS.inventory['primary']
                elif key[pygame.K_2] and SETTINGS.inventory['secondary']:
                    SETTINGS.next_gun = SETTINGS.inventory['secondary']
                elif key[pygame.K_3] and SETTINGS.inventory['melee']:
                    SETTINGS.next_gun = SETTINGS.inventory['melee']

        #Keep angle in place
                if self.angle >= 360:
                    self.angle = 0
                elif self.angle < 0:
                    self.angle = 359

        #Interact
                if key[pygame.K_e]:
                    if SETTINGS.middle_slice:
                        if SETTINGS.middle_slice_len <= SETTINGS.tile_size*1.5 and (SETTINGS.middle_slice.type == 'vdoor' or SETTINGS.middle_slice.type == 'hdoor'):
                            SETTINGS.middle_slice.sesam_luk_dig_op()
                        elif SETTINGS.middle_slice_len <= SETTINGS.tile_size and SETTINGS.middle_slice.type == 'end':
                            SETTINGS.player_states['fade'] = True
                            SETTINGS.changing_level = True
                            

                madd = self.mouse.get_rel()[0] * self.sensitivity
                if madd > 38:
                    madd = 38
                elif madd < -38:
                    madd = -38
                self.angle -= madd
                SETTINGS.player_angle = self.angle
                
        #Open inventory
            if key[pygame.K_i] and self.inventory < 1:
                if SETTINGS.player_states['invopen']:
                    SETTINGS.player_states['invopen'] = False
                    SETTINGS.inv_strings_updated = False
                else:
                    SETTINGS.player_states['invopen'] = True
                    
                self.inventory += 1
            elif not key[pygame.K_i]:
                self.inventory = 0
                
        #Is the player dead or taking damage?
        if self.health > SETTINGS.player_health:
            self.health = SETTINGS.player_health
            SETTINGS.player_states['hurt'] = True
        if SETTINGS.player_health <= 0 and not SETTINGS.godmode:
            self.dead = True
            SETTINGS.player_states['dead'] = True
        if SETTINGS.player_health < 0:
            SETTINGS.player_health = 0


    #========================================================

        #Lock mouse. (DEV)     Husk at inventory skal bruge mus. (playerstates[4])
        if not key[pygame.K_q]:
        #    pygame.event.set_grab(True)
        #    self.mouse.set_visible(False)
            pygame.event.set_grab(False)
            self.mouse.set_visible(True)
        else:
        #    pygame.event.set_grab(False)
        #    self.mouse.set_visible(True)
            pygame.event.set_grab(True)
            self.mouse.set_visible(False)

        #Change to map view (DEV)
        if key[pygame.K_m]:
            SETTINGS.switch_mode = True


        #Change FOV (DEV)
        if key[pygame.K_UP]:
            SETTINGS.fov += 2
        elif key[pygame.K_DOWN]:
            SETTINGS.fov -= 2
            
        #Screen shake (DEV)
        if key[pygame.K_p]:
            SETTINGS.screen_shake = 20
            SETTINGS.player_hurt = True

    #======================================================
            
    def move(self, pos):
        if SETTINGS.cfps > 5:
            if pos[0] != 0:
                self.update(pos[0], 0)
            if pos[1] != 0:
                self.update(0, pos[1])

    def update(self, x, y):        
        self.real_x += x * SETTINGS.dt
        self.real_y += y * SETTINGS.dt
        self.rect.x = self.real_x
        self.rect.y = self.real_y
        SETTINGS.player_rect = self.rect
        tile_hit_list = pygame.sprite.spritecollide(self, self.collide_list, False)
        
        #Actually there are not only tiles in the list. NPCs as well.
        for tile in tile_hit_list:
            if tile.solid:
                if x > 0:
                    self.rect.right = tile.rect.left
                    self.real_x = self.rect.x
                if x < 0:
                    self.rect.left = tile.rect.right
                    self.real_x = self.rect.x
                if y > 0:
                    self.rect.bottom = tile.rect.top
                    self.real_y = self.rect.y
                if y < 0:
                    self.rect.top = tile.rect.bottom
                    self.real_y = self.rect.y

        SETTINGS.player_map_pos = [int(self.rect.centerx / SETTINGS.tile_size), int(self.rect.centery / SETTINGS.tile_size)]

    def draw(self, canvas):
        pointer = self.direction(0, 10)
        p1 = pointer[0] + self.rect.center[0]
        p2 = pointer[1] + self.rect.center[1]
        canvas.blit(self.sprite, self.rect)
        pygame.draw.line(canvas, self.color, self.rect.center, (p1, p2))

        
        





        
