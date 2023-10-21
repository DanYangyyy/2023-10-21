import qrcode

img = qrcode.make("丹丹加油，好好学习")
img.save('qrcode.png')