height = int(input("Height?\n"))
width = int(input("Width?\n"))
depth = int(input("Depth?\n"))

def volume(h, w, d):
    volume = (h * w * d)
    return volume

def main():
    print(volume(height, width, depth))
main()
