# Create file
file = open('hellow_world.txt', 'w')
file.write('Hello world!')
file.write('Another Hello world!')
file.close()

# Write in exists file
file = open('hellow_world.txt', 'w')
file.write('Another Hello world!')
file.close()

# Add string in exists file
file = open('hellow_world.txt', 'a')
file.write('Finale Hello world!')
file.close()

# Combine read/write modes
file = open('hellow_world.txt', 'r+')
file.write('Real Finale Hello world!')
file.close()

# Find the end of file
file = open('hellow_world.txt', 'r+')
file.seek(0, 2)
file.write('\nMy Finale Hello world!')
file.close()
