#!/home/user/.local/bin/checkio --domain=py run find-enemy

# Find the distance and relative direction to the enemy in a HEX-grid.
# 
# HEX-grid (hexagonal grid) is a coordinate system, like square grid. To find distancebetween two cells you don't need to find exact path from one to another, but correctly work with their coordinates.Another approach to calculate distance isto notice that all cells strict around your cell form a kind of circle and are ondistance 1 from your cell, the cells around all previous cells (next "circle") areon distance 2 etc.In this mission the field from "A1" to "Z9" is used for placing youand enemy, but you may need to use coordinates "outside" this field for your calculations.Be attentive to cases when your position is on the edge of the field.
# 
# 
# 
# Absolute Directions. If we take any cell, the cell above it is always to the    north ("N"), below - to the south ("S") etc.
# 
# 
# 
# Relative Directions depends of your absolute direction. if your absolute direction is "N",    relative directions are the following. So all cells around specific cell form    4 "sectors": forward, right, back and left. Cells considered as present in this    sectors, even if they are "outside" of our field.
# 
# 
# 
# But when your absolute direction is for example "SE" these "sectors" rotate and the cell    in front of your cell will be to the south-east, and the north absolute    direction will be in left sector.
# 
# Input:Three arguments: your current coordinates, your current absolute directions, and enemy's coordinates.
# 
# Output:A list with relative direction and distance to the enemy.
# 
# 
# 
# 
# How it is used:War-game design uses hex-grid.
# 
# 
# 
# Preconditions:'A1' ≤ coordinates ≤ 'Z9';direction in ('N', 'NE', 'SE', 'S', 'SW', 'NW');your coordinates ≠ enemy's coordinates.
# 
# 
# END_DESC

def find_enemy(you, dir, enemy):
    pass


if __name__ == '__main__':
    assert find_enemy('G5', 'N', 'G4') == ['F', 1], "N-1"
    assert find_enemy('G5', 'N', 'I4') == ['R', 2], "NE-2"
    assert find_enemy('G5', 'N', 'J6') == ['R', 3], "SE-3"
    assert find_enemy('G5', 'N', 'G9') == ['B', 4], "S-4"
    assert find_enemy('G5', 'N', 'B7') == ['L', 5], "SW-5"
    assert find_enemy('G5', 'N', 'A2') == ['L', 6], "NW-6"
    assert find_enemy('G3', 'NE', 'C5') == ['B', 4], "[watch your six!]"
    assert find_enemy('H3', 'SW', 'E2') == ['R', 3], "right"
    assert find_enemy('A4', 'S', 'M4') == ['L', 12], "true left"
    print("You are good to go!")