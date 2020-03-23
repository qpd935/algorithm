from PIL import Image
import argparse


# parser = argparse.ArgumentParser()
# # parser.add_argument('D:\Download\Google\\attractive-beautiful-beauty-735552.jpg')
# parser.add_argument('433H.jpg')
# args = parser.parse_args()
# imgpath = args.file

imgpath = 'D:\Download\Google\\attractive-beautiful-beauty-735552.jpg'
imgpath = 'D:\QPDSpace\\20181212115635.jpg'
# imgpath = 'd:\QPDSpace\qrPspId.jpg'
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

print('path:' + imgpath)

def get_char(R, G, B):	
	length = len(ascii_char)
	gray = (R*299 + G*587 + B*114 + 500) / 1000
	# gray = int(0.2126 * R + 0.7152 * G + 0.0722 * B)
	unit = (256.0 + 1)/length
	return ascii_char[int(gray/unit)]

def output(imgpath, width=100, height=100):
	im = Image.open(imgpath)
	im = im.resize((width, height), Image.NEAREST)
	txt = ''
	for h in range(height):
		for w in range(width):
			txt += get_char(*im.getpixel((w, h))[:3])
		txt += '\n'
	return txt

def save_as_txtfile(txt):
	with open('d:\desktop\img2char.txt', 'w') as f:
		f.write(txt)


# if __name__ == '__main__':
# 	print(output(imgpath, 120, 90))
# 	save_as_txtfile(output(imgpath, 120, 90))


save_as_txtfile(output(imgpath, 60, 45))