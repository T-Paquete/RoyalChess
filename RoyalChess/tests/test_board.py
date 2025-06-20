import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from src.game.board import Board
from src.game.constants import ROWS, COLS
from src.game.piece import (
    Pawn, RoyalGuard, Knight, Counselor, Rook, Wizard, Prince, Dragon, Lion, King, Queen,
    Symbol, WhiteHat, BlackHat
)

def test_board_grid_size():
    board = Board()
    assert len(board.grid) == ROWS
    assert all(len(row) == COLS for row in board.grid)

def test_empty_middle_squares():
    board = Board()
    # Rows 3–6 should be completely empty
    for row in range(3, 7):
        for col in range(COLS):
            assert board.grid[row][col] is None

def test_initial_pawn_placement():
    board = Board()
    # White pawns
    for col in list(range(0, 4)) + list(range(8, 12)):
        piece = board.grid[7][col]
        assert isinstance(piece, Pawn)
        assert piece.color == "white"
    # Black pawns
    for col in list(range(0, 4)) + list(range(8, 12)):
        piece = board.grid[2][col]
        assert isinstance(piece, Pawn)
        assert piece.color == "black"

def test_initial_royal_guard_placement():
    board = Board()
    for col in range(4, 8):
        assert isinstance(board.grid[7][col], RoyalGuard)
        assert board.grid[7][col].color == "white"
        assert isinstance(board.grid[2][col], RoyalGuard)
        assert board.grid[2][col].color == "black"

def test_initial_rook_placement():
    board = Board()
    assert isinstance(board.grid[8][0], Rook)
    assert board.grid[8][0].color == "white"
    assert isinstance(board.grid[8][11], Rook)
    assert board.grid[8][11].color == "white"
    assert isinstance(board.grid[1][0], Rook)
    assert board.grid[1][0].color == "black"
    assert isinstance(board.grid[1][11], Rook)
    assert board.grid[1][11].color == "black"

def test_initial_knight_placement():
    board = Board()
    assert isinstance(board.grid[8][1], Knight)
    assert board.grid[8][1].color == "white"
    assert isinstance(board.grid[8][10], Knight)
    assert board.grid[8][10].color == "white"
    assert isinstance(board.grid[1][1], Knight)
    assert board.grid[1][1].color == "black"
    assert isinstance(board.grid[1][10], Knight)
    assert board.grid[1][10].color == "black"

def test_initial_dragon_placement():
    board = Board()
    assert isinstance(board.grid[8][2], Dragon)
    assert board.grid[8][2].color == "white"
    assert isinstance(board.grid[1][2], Dragon)
    assert board.grid[1][2].color == "black"

def test_initial_wizard_placement():
    board = Board()
    assert isinstance(board.grid[8][3], Wizard)
    assert board.grid[8][3].color == "white"
    assert isinstance(board.grid[1][3], Wizard)
    assert board.grid[1][3].color == "black"

def test_initial_lion_placement():
    board = Board()
    assert isinstance(board.grid[8][9], Lion)
    assert board.grid[8][9].color == "white"
    assert isinstance(board.grid[1][9], Lion)
    assert board.grid[1][9].color == "black"

def test_initial_prince_placement():
    board = Board()
    assert isinstance(board.grid[8][8], Prince)
    assert board.grid[8][8].color == "white"
    assert isinstance(board.grid[1][8], Prince)
    assert board.grid[1][8].color == "black"

def test_initial_counselor_placement():
    board = Board()
    assert isinstance(board.grid[8][4], Counselor)
    assert board.grid[8][4].color == "white"
    assert isinstance(board.grid[8][7], Counselor)
    assert board.grid[8][7].color == "white"
    assert isinstance(board.grid[1][4], Counselor)
    assert board.grid[1][4].color == "black"
    assert isinstance(board.grid[1][7], Counselor)
    assert board.grid[1][7].color == "black"

def test_initial_king_queen_placement():
    board = Board()
    assert isinstance(board.grid[8][6], King)
    assert board.grid[8][6].color == "white"
    assert isinstance(board.grid[1][6], King)
    assert board.grid[1][6].color == "black"
    assert isinstance(board.grid[8][5], Queen)
    assert board.grid[8][5].color == "white"
    assert isinstance(board.grid[1][5], Queen)
    assert board.grid[1][5].color == "black"

def test_initial_symbol_placement():
    board = Board()
    assert isinstance(board.grid[9][5], Symbol)
    assert board.grid[9][5].color == "white"
    assert isinstance(board.grid[9][6], Symbol)
    assert board.grid[9][6].color == "white"
    assert isinstance(board.grid[0][5], Symbol)
    assert board.grid[0][5].color == "black"
    assert isinstance(board.grid[0][6], Symbol)
    assert board.grid[0][6].color == "black"

def test_initial_whitehat_blackhat_placement():
    board = Board()
    assert isinstance(board.grid[9][4], WhiteHat)
    assert board.grid[9][4].color == "white"
    assert isinstance(board.grid[0][4], WhiteHat)
    assert board.grid[0][4].color == "black"
    assert isinstance(board.grid[9][7], BlackHat)
    assert board.grid[9][7].color == "white"
    assert isinstance(board.grid[0][7], BlackHat)
    assert board.grid[0][7].color == "black"