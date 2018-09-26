# Display energy bars
print("Please enter the number of lives remaining:")
lives = int(input())
print("Please enter the energy level:")
energy = int(input())
print("Please enter the shield level:")
shield = int(input())

print("Lives: ", "♥ " * lives)
print("Energy:", "♦ " * energy)
print("Shield:", "♦ " * shield)
