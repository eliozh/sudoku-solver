# general parameters
MIN_BOARD_AREA = 1000 * 1000
MIN_CELL_AREA = 100 * 100           # approximate minimum area of a single cell (in pixel)
MAX_CELL_AREA = 150 * 150           # approximate maximum area of a single cell (in pixel)
OPERATION_INTERVAL = 0.02           # time interval between two continuous operations
LABELS_COORD = {
    1: (72, 2046), 
    2: (188, 2046), 
    3: (308, 2046), 
    4: (427, 2046), 
    5: (533, 2046), 
    6: (647, 2046), 
    7: (770, 2046), 
    8: (884, 2046), 
    9: (1010, 2046)
}                                   # coordinates of each label

# event mode related parameters
CONT_BTN_COORD = (545, 2145)        # coordinate of `continue` button
PLAY_BTN_COORD = (540, 1560)        # coordinate of `play` button
AFTER_DONE_INTERVAL = 5             # time to wait before tap `continue` button after game is done
AFTER_CONT_INTERVAL = 2             # time to wait before tap `play` button after tap `continue` button
AFTER_PLAY_INTERVAL = 2             # time to wait before capture screen shot after tap `play` button