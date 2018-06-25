#Level classes for DUGA

import SETTINGS

class Level:
    
    def __init__(self, stats):
        self.stats = stats
        
        self.lvl_number = stats['lvl_number']
        self.sky_color = stats['sky_color']
        self.ground_color = stats['ground_color']
        self.npcs = stats['npcs']
        self.items = stats['items']
        self.player_pos = stats['player_pos']
        self.array = stats['array']
        self.shade = stats['shade'][0]
        self.shade_rgba = stats['shade'][1]
        self.shade_visibility = stats['shade'][2]


SETTINGS.levels_list.append(Level({
    'lvl_number' : 0,
    'sky_color' : SETTINGS.GRAY,
    'ground_color': SETTINGS.LIGHTGRAY,
    'npcs' : [([2,3], 270, 4), ([3,3], 270, 5)],#, ([3,3], 270, 3), ([4,3], 270, 3), ([1,3], 270, 3)],
    'items' : [([1,1], 2), ([2,1], 3), ([3,1], 7), ([4, 1], 6), ([4,2], 8), ([3,2], 9), ([1,2], 11)],
    'player_pos' : [2,2],
    'shade' : (False, (0,0,0,0), 0),
    'array' : [
        #0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8
        [1,1,1,1,1,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,1,4,1,1,1]
        ]}))

SETTINGS.levels_list.append(Level({
    'lvl_number' : 1,
    'sky_color' : SETTINGS.GRAY,
    'ground_color': SETTINGS.BROWN,
    'npcs' : [([2,6], 270, 4)],#, ([10,10], 180, 1), ([17, 9], 180, 0)],
    'items' : [([8,2], 8), ([2,7], 5), ([13,4], 0), ([10, 5], 2), ([12, 12], 2), ([16, 8], 1), ([16, 11], 0)],
    'player_pos' : [6,1],
    'shade' : (True, (0,0,0,0), 500),
    'array' : [
        #0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8
        [0,0,0,0,0,1,1,2,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,8,0,1,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,1,10,1,1,1,2,1,1,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0],
        [0,5,5,5,1,0,8,0,0,0,0,1,8,0,1,0,0,0,0],
        [1,0,0,0,1,0,0,1,1,10,1,1,10,1,0,0,0,0,0],
        [2,0,8,0,1,0,0,1,7,0,0,0,0,0,1,5,2,5,0],
        [1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,5],
        [0,1,1,0,1,0,0,1,1,1,3,1,1,1,1,0,0,0,3],
        [0,0,1,0,9,0,0,0,0,0,8,0,0,0,9,0,8,0,5],
        [0,0,1,1,1,7,0,1,1,1,1,1,1,10,1,0,0,0,5],
        [0,0,0,0,0,1,1,0,4,9,0,8,0,0,1,5,5,5,0],
        [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,2,1,1,0,0,0,0,0],
        ]}))
##
##SETTINGS.levels_list.append(Level({
##    'lvl_number' : 2,
##    'sky_color': SETTINGS.LIGHTGRAY,
##    'ground_color': SETTINGS.LIGHTGRAY,
##    'npcs' : [([3,15], 90, 0), ([8,8], 0, 0), ([17,14], 270, 0), ([17, 11], 0, 1), ([5,11], 270, 3)],
##    'items' : [([5,15],2), ([6,5], 1), ([10, 1], 6),([9,1], 2), ([11,1], 2), ([1, 10], 2), ([2, 19], 2), ([10, 9], 0), ([15, 6], 1), ([15, 7], 3), ([7, 18], 0), ([7, 19], 2)],
##    'player_pos' : [6,2],
##    'array' : [
##        #0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
##        [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
##        [0,0,0,0,0,0,1,0,1,0,8,0,1,0,0,0,0,0,0,0,0],
##        [0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0],
##        [0,1,1,1,1,1,10,1,1,1,10,1,0,0,0,0,0,0,0,0,0],
##        [1,0,0,0,0,0,0,0,0,0,0,7,1,0,1,1,0,0,0,0,0],
##        [1,0,8,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],
##        [1,0,0,1,1,1,1,1,1,1,10,1,1,1,0,0,1,0,0,0,0],
##        [1,0,0,1,0,0,1,0,0,0,0,0,0,9,0,0,1,0,0,0,0],
##        [1,0,0,1,0,0,9,0,0,0,8,0,0,1,0,0,1,0,0,0,0],
##        [1,0,0,1,0,0,1,7,0,0,0,0,0,1,1,1,0,0,4,0,0],
##        [1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,10,1,0],
##        [1,0,8,0,0,0,0,0,0,8,0,0,0,0,1,1,0,0,0,0,1],
##        [1,0,0,0,0,0,0,0,0,0,0,0,0,7,1,1,0,0,0,0,1],
##        [0,1,1,10,1,1,1,1,1,1,1,1,10,1,1,0,1,1,10,1,0],
##        [1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1],
##        [1,0,0,8,0,0,1,0,0,1,0,0,8,0,0,1,0,0,8,0,1],
##        [0,1,10,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,1],
##        [1,0,0,0,0,7,1,0,0,9,0,0,0,0,0,0,0,0,0,0,1],
##        [1,0,0,8,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0],
##        [1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
##        [0,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
##        ]}))
##
##SETTINGS.levels_list.append(Level({
##    'lvl_number' : 3,
##    'sky_color' : SETTINGS.GRAY,
##    'ground_color' : SETTINGS.DARKRED,
##    'npcs' : [([5,18], 90, 4), ([4,2], 270, 0), ([5,7], 180, 3)],
##    'items' : [([10,3],1), ([8,2],4), ([5,10],7), ([1,9],3), ([1,10],3), ([1,11],3), ([10,9],2), ([10,10],2), ([10,11],2), ([5,14],0), ([2,10],0), ([9,10],1),([1,18],0),([9,18],0)],
##    'player_pos' : [1,2],
##    'array' : [
##        #0 1 2 3 4 5 6 7 8 9 0 11
##        [0,0,0,1,2,1,0,1,1,0,5,0],#0
##        [0,1,1,0,0,0,1,0,0,1,0,5],#1
##        [1,0,9,0,8,0,9,0,0,9,0,5],#2
##        [0,1,1,0,0,0,1,0,0,1,0,5],#3
##        [0,0,0,1,1,1,1,0,0,1,5,0],#4
##        [0,0,0,1,7,0,0,0,0,1,0,0],#5
##        [0,0,0,2,0,8,0,1,1,0,0,0],#6
##        [0,0,0,1,0,0,0,1,0,0,0,0],#7
##        [0,1,1,0,1,10,1,0,1,1,1,0],#8
##        [1,0,0,1,0,0,0,1,0,0,0,1],#9
##        [3,0,8,9,0,8,0,9,0,8,0,2],#10
##        [1,0,0,1,0,0,0,1,0,0,0,1],#11
##        [0,1,1,0,1,10,1,0,1,3,1,0],#12
##        [0,0,0,1,0,0,0,1,0,0,0,0],#13
##        [0,0,0,1,0,8,0,1,0,0,0,0],#14
##        [0,0,0,1,1,10,1,1,0,0,0,0],#15
##        [0,1,1,0,0,8,0,0,1,1,0,0],#16
##        [1,0,1,0,6,0,6,0,1,0,1,0],#17
##        [2,0,9,8,0,8,0,8,9,0,3,0],#18
##        [1,0,1,0,6,0,6,0,1,0,1,0],#19
##        [0,1,1,0,0,8,0,0,1,1,0,0],#20
##        [0,0,0,1,1,10,1,1,0,0,0,0],#21
##        [0,0,0,5,0,0,0,5,0,0,0,0],#22
##        [0,0,0,5,0,8,0,5,0,0,0,0],#23
##        [0,0,0,0,1,10,1,0,0,0,0,0],#24
##        [0,0,0,0,1,0,1,0,0,0,0,0],#25
##        [0,0,0,0,0,4,0,0,0,0,0,0],#26
##        ]}))
##
##SETTINGS.levels_list.append(Level({
##'items' : [((1, 1), 2), ((2, 1), 6), ((3, 1), 2)],
##'npcs' : [((8, 8), 180, 0), ((3, 10), 90, 2), ((8, 10), 180, 0)],
##'player_pos' : [3, 2],
##'sky_color' : SETTINGS.LIGHTGRAY,
##'array' : [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 2, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 1, 10, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 7, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 8, 0, 0, 0, 0, 0, 0, 1], [3, 0, 0, 0, 1, 1, 1, 2, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 5], [1, 0, 0, 0, 9, 0, 0, 8, 0, 4], [1, 0, 0, 0, 1, 0, 0, 0, 0, 5], [1, 2, 1, 1, 1, 5, 5, 5, 5, 5]],
##'ground_color' : SETTINGS.DARKGRAY,
##'lvl_number' : 4,
##}))



#NPC spawn syntax: [([map pos], face, id)]
#Item spawn syntax: [([map pos], id)]







                                  
