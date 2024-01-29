import argparse
import sys
import cv2
from sudoku.device import connect_device
from sudoku.sudoku_detect import process
from sudoku.params import LABELS_COORD, OPERATION_INTERVAL, CONT_BTN_COORD, PLAY_BTN_COORD, AFTER_CONT_INTERVAL, AFTER_DONE_INTERVAL, AFTER_PLAY_INTERVAL, CONT_BTN_COORD, PLAY_BTN_COORD


def sudoku_normal(device):
    with open("./screen.png", "wb") as f:
        f.write(device.screencap())
    frame = cv2.imread("./screen.png")
    sudoku, pos, cell_pos = process(frame)
    sudoku_copy = np.copy(sudoku)
    solved = solve(sudoku_copy)
    if solved == False:
        print("No solution found!")
        return
    print_board(sudoku_copy)
    print("Done. Start operating...")
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                digit = sudoku_copy[i][j]
                label_coord = LABELS_COORD[digit]
                device.input_tap(*label_coord)
                time.sleep(OPERATION_INTERVAL)
                x = pos[0] + cell_pos[i, j, 0]
                y = pos[1] + cell_pos[i, j, 1]
                device.input_tap(x, y)
                time.sleep(OPERATION_INTERVAL)


def sudoku_event(device):
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
                    time.sleep(OPERATION_INTERVAL)
                    x = pos[0] + cell_pos[i, j, 0]
                    y = pos[1] + cell_pos[i, j, 1]
                    device.input_tap(x, y)
                    time.sleep(OPERATION_INTERVAL)

        time.sleep(AFTER_DONE_INTERVAL)
        device.input_tap(*CONT_BTN_COORD)
        time.sleep(AFTER_CONT_INTERVAL)
        device.input_tap(*PLAY_BTN_COORD)
        time.sleep(AFTER_PLAY_INTERVAL)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sudoku auto solver with adb")
    parser.add_argument("--mode", choices=["normal", "event"])
    args = parser.parse_args(sys.argv[1:])
    
    mode = args.mode[0]
    device = connect_device(device)
    if mode == "normal":
        sudoku_normal(device)
    elif mode == "event":
        sudoku_event(device)
