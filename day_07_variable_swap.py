# 1. Swap the ball without even losing or crushing the red ball
A = "Red"
B = "Blue"

# 2.Take the 3rd container and move box A Ball into the 3rd countainer
template = A
# Move the ball into A
A = B
# Move template's ball into B
B = template

# Both variables at the bottom to verify the swap work
print(A)
print(B)
