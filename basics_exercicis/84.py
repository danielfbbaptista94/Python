from screeninfo import get_monitor

width = get_monitor()[0].width
height = get_monitor()[0].height

print("Width: %s,  Height: %s" % (width, height))
