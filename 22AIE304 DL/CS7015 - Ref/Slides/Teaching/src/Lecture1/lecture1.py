import sys
import os

desc_file = open(sys.argv[1])
start_period = int(sys.argv[2])
end_period = int(sys.argv[3])
desc_lines = desc_file.readlines()

desc_lines = [t.split("\t") for t in desc_lines]
desc_lines = desc_lines[1:]
print (desc_lines)
new_file_descriptions  = ["\justify"]
#write descriptions
for i, line in enumerate(desc_lines):
	temp = "\only<" + str(i+1) + ">{" + line[0] + "}"
	new_file_descriptions.append(temp)

new_file_descriptions.append("\end{overlayarea}")

new_file_images = ["\column{0.5\\textwidth}","\\begin{overlayarea}{\\textwidth}{\\textheight}","\\begin{figure}",
"\centering"]
#generate image links
for i, line in enumerate(desc_lines):
	temp = "\only<" + str(i+1) + ">{\\includegraphics[scale=0.5]{" + line[1] + "}}"
	new_file_images.append(temp)

new_file_images += ["\end{figure}","\end{overlayarea}","\end{columns}","\end{minipage}"]


new_file_timelines = ["\\begin{minipage}[t][0.4\\textheight][t]{\\textwidth}","\\begin{overlayarea}{\\textwidth}{\\textheight}",
"\\begin{tikzpicture}[datemarker/.style={circle, draw=black,fill=white},textlabel/.style={anchor=center,text height=1.7ex,text depth=.25ex}]", 
"\\tikzset{every node/.style={font=\\tiny, color=blue}}\draw[fill=gray](-0.2,0) rectangle (13.2,0.5) node[white, below]{};"
]


for i, line in enumerate(desc_lines):
	print (line[3])
	if line[3] == 'point':
		start_point = ((int(line[2])-start_period)*13.0)/(end_period - start_period)
		temp = "\onslide<" + str(i+1) + "->{\\node at (" + str(start_point) + ", 0.25) [datemarker] {};}"
		new_file_timelines.append(temp)
	else:
		x = line[2].split("-")
		print (x)
		start_point, end_point = int(x[0])-start_period, int(x[1]) -start_period
		start_point = int(start_point)*13.0/(end_period - start_period)
		end_point = int(end_point)*13.0/(end_period - start_period)
		temp = "\onslide<" +str(i+1) + "->{\draw[fill=yellow](" + str(start_point) + ",0) rectangle (" + str(end_point) + ", 0.5){};}"
		new_file_timelines.append(temp)
		print start_point, end_point
		start_point = (start_point + end_point )/2.0
		print start_point

	temp = "\onslide<" + str(i + 1) + "->{\draw [line width=1pt] (" + str(start_point) + ", 0.5) to (" + str(start_point) + ", 1.0);}"
	new_file_timelines.append(temp)
	temp = "\onslide<" + str(i + 1) + "->{\draw (" + str(start_point) + ", 1.2) node [textlabel]{" + line[2] + "};}"
	new_file_timelines.append(temp)
	temp = "\onslide<" + str(i+1) + "->{\draw [fill=orange](" + str(start_point) + ", -0.5) circle (2pt){};}"
	new_file_timelines.append(temp)
	temp = "\onslide<" + str(i+1) + "->{\draw(" + str(start_point) + ", -0.5) circle (4pt){};}"
	new_file_timelines.append(temp)
	temp = "\onslide<" + str(i + 1) + "->{\draw [line width=1pt] (" + str(start_point) + ", 0) to (" +str(start_point) + ", -0.3);}"
	new_file_timelines.append(temp)
	temp = "\onslide<" + str(i+1) + "->{\draw (" + str(start_point) + ",-0.9) node [textlabel] {" + line[4] + "};}"
	new_file_timelines.append(temp)


new_file_timelines += ["\end{tikzpicture}","\end{overlayarea}","\end{minipage}","\end{frame}","\end{document}"]


new_file = sys.argv[4]
new_file = open(new_file, "w")

for i in new_file_descriptions:
	new_file.write(i + "\n")

for i in new_file_images:
	new_file.write(i + "\n")

for i in new_file_timelines:
	new_file.write(i + "\n")
