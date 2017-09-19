import re

# SVG Pattern 

def draw(patt):
	patt =  ''.join([str(int(n)+1) for n in patt]) # 0 to 1 1 to 2 ...
	svg = '<?xml version="1.0" encoding="utf-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" version="1.2" width="240" height="240" >'
	line = '''
	<line x1="$" y1="$" x2="$" y2="$" stroke="#F6F8FA" stroke-width="5" />
	<line x1="$" y1="$" x2="$" y2="$" stroke="#F6F8FA" stroke-width="5" />
	<line x1="$" y1="$" x2="$" y2="$" stroke="#F6F8FA" stroke-width="5" />
	<line x1="$" y1="$" x2="$" y2="$" stroke="#F6F8FA" stroke-width="5" />
	<line x1="$" y1="$" x2="$" y2="$" stroke="#F6F8FA" stroke-width="5" />
	<line x1="$" y1="$" x2="$" y2="$" stroke="#F6F8FA" stroke-width="5" />
	<line x1="$" y1="$" x2="$" y2="$" stroke="#F6F8FA" stroke-width="5" />
	<line x1="$" y1="$" x2="$" y2="$" stroke="#F6F8FA" stroke-width="5" />
	<line x1="$" y1="$" x2="$" y2="$" stroke="#F6F8FA" stroke-width="5" />
	'''
	circle = '''
	<circle cx="45" cy="45" r="2.5" fill="black"  stroke-width="40" stroke-opacity="0.8"  -1/>
	<circle cx="45" cy="125" r="2.5" fill="black" stroke-width="40" stroke-opacity="0.8" -4/>
	<circle cx="45" cy="205" r="2.5" fill="black"  stroke-width="40" stroke-opacity="0.8" -7/>
	<circle cx="125" cy="45" r="2.5" fill="black"  stroke-width="40" stroke-opacity="0.8" -2/>
	<circle cx="125" cy="125" r="2.5" fill="black"  stroke-width="40" stroke-opacity="0.8"  -5/>
	<circle cx="125" cy="205" r="2.5" fill="black" stroke-width="40" stroke-opacity="0.8" -7/>
	<circle cx="205" cy="45" r="2.5" fill="black"  stroke-width="40" stroke-opacity="0.8" -3/>
	<circle cx="205" cy="125" r="2.5" fill="black"  stroke-width="40" stroke-opacity="0.8" -6/>
	<circle cx="205" cy="205" r="2.5" fill="black"  stroke-width="40" stroke-opacity="0.8"  -9/>
	'''
	text = '''
	<text x="38" y="52" fill="green" font-size="24">-1</text>
	<text x="118" y="52" fill="green" font-size="24">-2</text>
	<text x="197" y="52" fill="green" font-size="24">-3</text>
	<text x="38" y="133" fill="green" font-size="24">-4</text>
	<text x="118" y="132" fill="green" font-size="24">-5</text>
	<text x="198" y="132" fill="green" font-size="24">-6</text>
	<text x="38" y="212" fill="green" font-size="24">-7</text>
	<text x="118" y="212" fill="green" font-size="24">-8</text>
	<text x="198" y="212" fill="green" font-size="24">-9</text>
	'''
	# make circles
	for i in patt:
		circle = circle.replace('-' + i, 'stroke="green"')
	circle = re.sub('-[0-9]', '', circle)
	# make lines
	w = []
	for j in range(len(patt)-1):
		w.append(patt[j:j+2])
	for i in w:
		for n in range(len(i)):
			d = int(i[n]) - 1
			x = d % 3
			y = d / 3
			line = line.replace('$', str(x*(2*15+2*25)+45), 1)
			line = line.replace('$', str(y*(2*15+2*25)+45), 1)
	# put numbers
	for t in range(1,len(patt)+1):
		text = text.replace('-' + patt[t-1], str(t))
	text = re.sub('-[0-9]','',text)
	svg = svg + circle + line + text + '\n</svg>'
	return svg
