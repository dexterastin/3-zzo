from calcFunctions import * 

functionMap = [
('factorial (!)', factorial),
('dec -> binary', decToBin),
('binary -> dec', binToDec),
('dec -> roman', decToRoman),
('roman	-> dec', romanToDec),
]
functionList =	[x[0]	for	x	in	functionMap]
