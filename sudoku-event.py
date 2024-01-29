import cv2
import numpy as np
import pytesseract
from ppadb.client import Client as AdbClient
from sudoku.sudoku_detect import process
from sudoku.sudoku import solve
import time


def connect_device():
    client = AdbClient()
    devices = client.devices()

    if len(devices) == 1:
        return devices[0]

    for index, device in enumerate(devices):
        print(f"{index}. {device.serial}")
    result = int(input(f"Choose device: "))

    return devices[result]
    

if __name__ == "__main__":
    device = connect_device()

    number_x_coords = {
        1: 72,
        2: 188,
        3: 308,
        4: 427,
        5: 533,
        6: 647,
        7: 770,
        8: 884,
        9: 1010
    }
    number_y_coord = 2046

    cont_btn = (545, 2145)
    play_btn = (547, 1645)

    while True:
        with open("./screen.png", "wb") as f:
            f.write(device.screencap())
        frame = cv2.imread("./screen.png")
        sudoku, pos, cell_pos = process(frame)
        sudoku_copy = np.copy(sudoku)
        solved = solve(sudoku_copy)

        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    digit = sudoku_copy[i][j]
                    device.input_tap(number_x_coords[digit], number_y_coord)
                    time.sleep(0.1)
                    x = pos[0] + cell_pos[i, j, 0]
                    y = pos[1] + cell_pos[i, j, 1]
                    device.input_tap(x, y)
                    time.sleep(0.02)

        time.sleep(5)
        device.input_tap(cont_btn[0], cont_btn[1])
        time.sleep(1)
        device.input_tap(play_btn[0], play_btn[1])
        time.sleep(2)
