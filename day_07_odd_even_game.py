# The Odd/Even Game Scoreboard
player_score = 27

# Using the Modulo Operator (%) to check if the score is odd or even
print(player_score % 2)

# The player's score is an odd no., they hit penalty and lose 5 points
player_score -= 5

# The new score of the player
print(player_score)
print(player_score % 2)

# The player's score is an even no., they increase by 10
player_score += 10

# Final scoreboard print
print(player_score)
