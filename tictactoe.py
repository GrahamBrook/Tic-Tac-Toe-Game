# Tic Tac Toe Game
# File Name:     tictactoe.py
# Programmer:    Eric Brooks
# Date:          3/21/2023
#Problem Statement: Create a tictactoe game using a graphic modules as an interface.
from graphics import *
import time

#Window Constants
window_width = 400
window_height = 500
update_rate = 30
window_background = "white"

#Graphics Window Setup
win = GraphWin("Graphics Window", window_width, window_height)
win.autoflush = False
win.setBackground(window_background)

def main():  
  global box_state 
  box_state = [0,0,0,0,0,0,0,0,0]
  def tic_tac_toe():
    background_setup()
    display_current_turn(1)
    turn_counter(1)
  
  
  def background_setup():
    #Background_setup function
    #Will make a border that will be made with two rectangles, the outer rectangle filled with black and the inner rectangle filled with white
    #Rectangles will make the cross hatch pattern where the tic tac toe game will be played
  
    #Outer Border
    outer_bottom_left_corner = Point(10, 110)
    outer_top_right_corner = Point(390, 490)
    outer_border = Rectangle(outer_bottom_left_corner, outer_top_right_corner)
    outer_border.draw(win)
    outer_border.setFill("Black")
  
    #Inner Border
    inner_bottom_left_corner = Point(15, 115)
    inner_top_right_corner = Point(385, 485)
    inner_border = Rectangle(inner_bottom_left_corner, inner_top_right_corner)
    inner_border.draw(win)
    inner_border.setFill("White")
  
    ####Columns and Rows
    #Each column/row will rectangles filled black and 5 pixels thick
  
    #Left Column
    left_column_bottom_left_corner = Point(137, 115)
    left_column_top_right_corner = Point(142, 485)
    left_column = Rectangle(left_column_bottom_left_corner,
                            left_column_top_right_corner)
    left_column.draw(win)
    left_column.setFill("Black")
  
    #Right Column
    right_column_bottom_left_corner = Point(263, 115)
    right_column_top_right_corner = Point(268, 485)
    right_column = Rectangle(right_column_bottom_left_corner,
                             right_column_top_right_corner)
    right_column.draw(win)
    right_column.setFill("Black")
  
    #Top Row
    top_row_bottom_left_corner = Point(15, 238)
    top_row_top_right_corner = Point(385, 243)
    top_row = Rectangle(top_row_bottom_left_corner, top_row_top_right_corner)
    top_row.draw(win)
    top_row.setFill("Black")
  
    #Bottom Row
    bottom_row_bottom_left_corner = Point(15, 362)
    bottom_row_top_right_corner = Point(385, 367)
    bottom_row = Rectangle(bottom_row_bottom_left_corner,
                           bottom_row_top_right_corner)
    bottom_row.draw(win)
    bottom_row.setFill("Black")
  
    return
  
  
  def x_marker(p1, p2):
    #Creates the x mark on the board, function takes two points, where the first   point is the upper left corner and the second point is the bottom right corner.   Will fill rectangular region between points with red and draw an x in the middle
    x_background = Rectangle(p1, p2)
    x_background.draw(win)
    x_background.setFill("Red")
  
    x_mark_position = Point((p1.getX() + p2.getX()) / 2,
                            (p1.getY() + p2.getY()) / 2)
    x_mark = Text(x_mark_position, "x")
    x_mark.setFace("arial")
    x_mark.setSize(36)
    x_mark.draw(win)
  
  
  def o_marker(p1, p2):
    #Creates the o mark on the board, function takes two points, where the first point is the upper left corner and the second point is the bottom right corner. Will fill rectangular region between points with red and draw an o in the middle
    o_background = Rectangle(p1, p2)
    o_background.draw(win)
    o_background.setFill("Blue")
  
    o_mark_position = Point((p1.getX() + p2.getX()) / 2,
                            (p1.getY() + p2.getY()) / 2)
    o_mark = Text(o_mark_position, "o")
    o_mark.setFace("arial")
    o_mark.setSize(36)
    o_mark.setTextColor("White")
    o_mark.draw(win)
  
  
  def marker_picker(current_player, p1, p2):
    #Chooses to make an x or an o baised on the current player
    if current_player == 1:
      x_marker(p1, p2)
      check_win_condition(current_player)
    elif current_player == 2:
      o_marker(p1, p2)
      check_win_condition(current_player)
    else:
      print("error in marker_picker")
  
  
  def clicker_checker():
    #Clicker function will return values 0 through 8 based on the region the player clicks. 0 is the top left corner, 1 is the middle top corner, and so on and so forth "increasing left to right, up to down"
    while True:
      mouse = win.checkMouse()
      if mouse != None and 15 < mouse.getX() < 142 and 115 < mouse.getY() < 243:
        return 0
      elif mouse != None and 142 < mouse.getX() < 268 and 115 < mouse.getY(
      ) < 243:
        return 1
      elif mouse != None and 268 < mouse.getX() < 385 and 115 < mouse.getY(
      ) < 243:
        return 2
      elif mouse != None and 15 < mouse.getX() < 142 and 243 < mouse.getY(
      ) < 367:
        return 3
      elif mouse != None and 142 < mouse.getX() < 268 and 243 < mouse.getY(
      ) < 367:
        return 4
      elif mouse != None and 268 < mouse.getX() < 385 and 243 < mouse.getY(
      ) < 367:
        return 5
      elif mouse != None and 15 < mouse.getX() < 142 and 367 < mouse.getY(
      ) < 485:
        return 6
      elif mouse != None and 142 < mouse.getX() < 268 and 367 < mouse.getY(
      ) < 485:
        return 7
      elif mouse != None and 268 < mouse.getX() < 385 and 367 < mouse.getY(
      ) < 485:
        return 8
  
  
  #Box_state_updater will change the box state list to match the current player's number baised on clicker_checker's input
  
  
  #box_state_updater will update the box_state list position baised on player input to the current player's number
  def box_state_updater(current_player):
    #Clicker_Checker will return a value 0-8, where each value corrresponds to a box on the board, first the box state will be checked to see if it is 0 and if it is the corrisponding entry on the list will change to the player's number. If the position checked is already equal to a player number then it will not update the list.
    player_input = clicker_checker()
    if player_input == 0:
      if box_state[0] == 0:
        box_state[0] = current_player
        p1 = Point(15, 115)
        p2 = Point(137, 238)
        marker_picker(current_player, p1, p2)
      else:
        box_state_updater(current_player)
    elif player_input == 1:
      if box_state[1] == 0:
        box_state[1] = current_player
        p1 = Point(142, 114)
        p2 = Point(264, 240)
        marker_picker(current_player, p1, p2)
      else:
        box_state_updater(current_player)
    elif player_input == 2:
      if box_state[2] == 0:
        box_state[2] = current_player
        p1 = Point(269, 115)
        p2 = Point(386, 240)
        marker_picker(current_player, p1, p2)
      else:
        box_state_updater(current_player)
    elif player_input == 3:
      if box_state[3] == 0:
        box_state[3] = current_player
        p1 = Point(15, 243)
        p2 = Point(137, 361)
        marker_picker(current_player, p1, p2)
      else:
        box_state_updater(current_player)
    elif player_input == 4:
      if box_state[4] == 0:
        box_state[4] = current_player
        p1 = Point(142, 244)
        p2 = Point(264, 363)
        marker_picker(current_player, p1, p2)
      else:
        box_state_updater(current_player)
    elif player_input == 5:
      if box_state[5] == 0:
        box_state[5] = current_player
        p1 = Point(268, 242)
        p2 = Point(385, 363)
        marker_picker(current_player, p1, p2)
      else:
        box_state_updater(current_player)
    elif player_input == 6:
      if box_state[6] == 0:
        box_state[6] = current_player
        p1 = Point(15, 365)
        p2 = Point(137, 486)
        marker_picker(current_player, p1, p2)
      else:
        box_state_updater(current_player)
    elif player_input == 7:
      if box_state[7] == 0:
        box_state[7] = current_player
        p1 = Point(143, 368)
        p2 = Point(263, 487)
        marker_picker(current_player, p1, p2)
      else:
        box_state_updater(current_player)
    elif player_input == 8:
      if box_state[8] == 0:
        box_state[8] = current_player
        p1 = Point(266, 366)
        p2 = Point(385, 485)
        marker_picker(current_player, p1, p2)
      else:
        box_state_updater(current_player)
    else:
      print("error in box_state_updater")
  
  
  def turn_counter(current_player):
    box_state_updater(current_player)
    if current_player == 1:
      player = 2
      display_current_turn(player)
      turn_counter(player)
    elif current_player == 2:
      player = 1
      display_current_turn(player)
      turn_counter(player)
    else:
      print("error in turn_counter")
  
  
  def display_winner(current_player):
    inner_corner = Point(10, 110)
    outer_corner = Point(390, 490)
    win_window = Rectangle(inner_corner, outer_corner)
    win_window.draw(win)
    if current_player == 1:
      win_window.setFill("Red")
      text_pos = Point((inner_corner.getX() + outer_corner.getX()) / 2,
                       (inner_corner.getY() + outer_corner.getY()) / 2)
      p1_wins = Text(text_pos, "Player 1 Wins!")
      p1_wins.setFace("arial")
      p1_wins.setSize(35)
      p1_wins.draw(win)
      win.after(3000, main)
      
    elif current_player == 2:
      win_window.setFill("Blue")
      text_pos = Point((inner_corner.getX() + outer_corner.getX()) / 2,
                       (inner_corner.getY() + outer_corner.getY()) / 2)
      p2_wins = Text(text_pos, "Player 2 Wins!")
      p2_wins.setFace("arial")
      p2_wins.setSize(35)
      p2_wins.setTextColor("White")
      p2_wins.draw(win)

      win.after(3000, main)
    elif current_player == 3:
      print("Cats Game")
      win_window.setFill("Purple")
      text_pos = Point((inner_corner.getX() + outer_corner.getX()) / 2,
                       (inner_corner.getY() + outer_corner.getY()) / 2)
      cats_game = Text(text_pos, "Cat's Game!")
      cats_game.setFace("arial")
      cats_game.setSize(35)
      cats_game.setTextColor("White")
      cats_game.draw(win)

      win.after(3000, main)
    else:
      print("Error in display_winner")
  
  
  def check_win_condition(current_player):
    player = current_player
    if box_state[0] == box_state[1] == box_state[2] != 0:
      display_winner(player)
  
    elif box_state[3] == box_state[4] == box_state[5] != 0:
      display_winner(player)
  
    elif box_state[6] == box_state[7] == box_state[8] != 0:
      display_winner(player)
    elif box_state[0] == box_state[3] == box_state[6] != 0:
  
      display_winner(player)
  
    elif box_state[1] == box_state[4] == box_state[7] != 0:
  
      display_winner(player)
  
    elif box_state[2] == box_state[5] == box_state[8] != 0:
  
      display_winner(player)
  
    elif box_state[0] == box_state[4] == box_state[8] != 0:
  
      display_winner(player)
    elif box_state[2] == box_state[4] == box_state[6] != 0:
  
      display_winner(player)
    elif box_state[0] and box_state[1] and box_state[2] and box_state[
        3] and box_state[4] and box_state[5] and box_state[6] and box_state[
          7] and box_state[8] != 0:
      display_winner(3)
    else:
      pass
  
  
  def display_current_turn(current_player):
    p1 = Point(9, 23)
    p2 = Point(218, 99)
    background = Rectangle(p1, p2)
    background.draw(win)
    background.setFill("White")
    background.setOutline("White")
    if current_player == 1:
      text_pos = Point((p1.getX() + p2.getX()) / 2, (p1.getY() + p2.getY()) / 2)
      current_turn = Text(text_pos, "Player 1's Turn")
      current_turn.setFace("arial")
      current_turn.setSize(20)
      current_turn.setTextColor("Red")
      current_turn.draw(win)
    elif current_player == 2:
      text_pos = Point((p1.getX() + p2.getX()) / 2, (p1.getY() + p2.getY()) / 2)
      current_turn = Text(text_pos, "Player 2's Turn")
      current_turn.setFace("arial")
      current_turn.setSize(20)
      current_turn.setTextColor("Blue")
      current_turn.draw(win)
    else:
      print("Error in display_current_turn")
  
  def reset():
    while True:
      mouse = win.getMouse()
      if mouse != None:
        tic_tac_toe()
  tic_tac_toe()
main()