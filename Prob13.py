with open('Prob13.in.txt','r') as f:
	lines = f.read().splitlines()
marker = 0
def next_line():
	global marker
	line = lines[marker]
	marker += 1
	return line

TargetFrameTime = 1000.0 / 90.0
LowThreshold = .7 * TargetFrameTime
ExtrapolateThreshold = .85 * TargetFrameTime
HighThreshold = .9 * TargetFrameTime


def extrapolated_value(x1,y1,x2,y2,x):
	return y1 + ((x-x1)/(x2-x1)) * (y2-y1)


T = int(next_line())

for t in range(T):
	line = next_line()

	frame_0, frame_1, frame_2, current_quality = list(map(float, line.split(' ')))
	quality = current_quality

	if frame_2 > HighThreshold:
		quality -= 2

	elif frame_2 > ExtrapolateThreshold:
		ex_val_0_2 = extrapolated_value(0,frame_0,2,frame_2,3)
		ex_val_1_2 = extrapolated_value(1,frame_1,2,frame_2,3)

		if max(ex_val_0_2, ex_val_1_2) > HighThreshold:
			quality -= 2

	elif frame_0 < LowThreshold and frame_1 < LowThreshold and frame_2 < LowThreshold:
		quality += 1

	print(int(quality))
		
