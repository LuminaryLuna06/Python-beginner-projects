import pyscreenshot

# Fullscreen shot

# image = pyscreenshot.grab()
# image.show()
# image.save("MaiTheTranh.png")

# Part of screen shot

image = pyscreenshot.grab(bbox=(100,100,1000,1000))
image.show()
image.save("TranhTheMai.png")