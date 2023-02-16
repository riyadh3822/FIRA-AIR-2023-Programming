import pyqrcode

left = pyqrcode.create("Left")
left.png ("QR1.png",scale = 8)

right = pyqrcode.create("Right")
right.png("QR2.png",scale = 8)

down = pyqrcode.create("Down")
down.png("QR3.png",scale = 8)

up = pyqrcode.create("up")
up.png("QR4.png",scale = 8)