# Sudoku solver
sudoku solver for [Sudoku Game on Google Play](https://play.google.com/store/apps/details?id=easy.sudoku.puzzle.solver.free). Auto complete with adb.

# Requirements
- python version and related packages can be found in `pyproject.toml`.
- adb v1.0.41
- tesseract v5.3.3.20231005
- turn on USB debugging and allow simulating input.

# Usage
```python
python ./main.py --mode {normal, event}
```
The default parameter is for Redmi Note 12 Turbo (Poco F5) with **$1080 \times 2400$** resolution.