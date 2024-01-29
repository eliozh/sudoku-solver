import cv2
import numpy as np
import pytesseract


def process(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 196 to 198 would work
    _, frame = cv2.threshold(frame, 196, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(
        image=cv2.bitwise_not(frame),
        mode=cv2.RETR_LIST,
        method=cv2.CHAIN_APPROX_SIMPLE
    )
    sudoku_area = 0
    sudoku_rect = None
    for cnt in contours:
        area = cv2.contourArea(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        if (0.7 < float(w) / h < 1.3
            and area > 1000 * 1000
                and area > sudoku_area):
            sudoku_area = area
            sudoku_rect = (x, y, w, h)

    if sudoku_area == 0:
        return False

    x, y, w, h = sudoku_rect
    frame = frame[y:y+h, x:x+w]
    sudoku_pos = (x, y)

    sudoku = np.zeros((9, 9))
    cell_pos = np.zeros((9, 9, 2))
    count = 0
    rect_avg_height = frame.shape[0] / 9.0
    rect_avg_width = frame.shape[1] / 9.0
    config = "--psm 10"
    contours, _ = cv2.findContours(
        image=cv2.bitwise_not(frame),
        mode=cv2.RETR_LIST,
        method=cv2.CHAIN_APPROX_SIMPLE
    )
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        rect_size = w * h
        if rect_size <= 150 * 150 and rect_size > 100 * 100:
            tmp = frame[y+2:y+h-2, x+2:x+w-2]
            digit = pytesseract.image_to_string(tmp, config=config).strip()

            x_center = x + w // 2
            y_center = y + h // 2
            x_coord = int(x_center / rect_avg_width)
            y_coord = int(y_center / rect_avg_height)

            cell_pos[y_coord, x_coord][0] = x_center
            cell_pos[y_coord, x_coord][1] = y_center

            try:
                sudoku[y_coord, x_coord] = int(digit)
            except Exception as e:
                pass

    return sudoku, sudoku_pos, cell_pos
