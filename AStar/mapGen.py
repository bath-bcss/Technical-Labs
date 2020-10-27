width = 200
height = 200

out = ""
for y in range(width):
    for x in range(height):
        if(x == 0 or y == 0 or x == width - 1 or y == height - 1):
            out += "#"
        else:
            out += " "

    out += "\n"

print(out)

