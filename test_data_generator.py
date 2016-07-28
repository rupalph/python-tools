import decimal
import random
import csv
import os
import properties

def printme( strin, i):
	keyworks = ['id','num']
	num = 1000 + i
	result=strin
	if any(k in strin.lower() for k in keywords):
		result = str(num)
	else:
		result=strin
	return result

def getDecimal (ctype):

	typestr  = Ctype
	width, dec_width = typestr.split(",")
	width = int (width) - int(dec_width)
	dec_width =int (dec_width)
	t1 = '9'
	t1 = t1.rjust (width, '9')
	i = int (t1)
	t2 = t2.rjust (dec_width, '9')
	d =int (t2)
	if (dec_width >0)
		return str (decimal.Decimal ('%d.%d' % (random.randint (0, i), random.randint(0,d))))
	else
		return str (decimal.Decimal ('%d' % random.randint (0, i))))


array = []
#path to schema file
path = properties.PATH
primarykey = properties.PRIMARYKEY_SEED
primarykeycol  =properties.PRIMARKYKEYS
skipcolstr = properties.COLUMNS_TO_SKIP
skipcol = False
iterations = properties.TOTAL_PER_RECORD_TYPE
outputlines = []
escape = properties.ESCAPE
delim = escape+properties.FIELD_DELIMITER+escape
newLineChar = properties.NEWLINE

for file in os listdir (path):
	primarykey = properties.PRIMARYKEY_SEED
	current_file = os.path.join(path, file)
	print (current_file)
	filename = current_file
	if any(k in filename for k in skipcolstr):
		skipcol = True
	else
		skipcol = False
		array = []

	for count in range(0,iterations):
		primarykey =primarykey + 1
		with open(current_file, new11ne='\n’) as csvfile:
			csvreader = csv.reader(csvfile, delimiter=',')
			for row in csvreader:
			#print (row)
			colnum,col,co1type,width,comments=row
			if 'RECORDLTYPE' in C01:
				val=filename[10:len(f1lenam)-10]
			elif any(k in col for k in prinarykeycol):
				#W" int (;zaim@.;."xk.:.@.y)
				val=str(primarykey)
			elif 'decimal' in coltype.lower():
				val=getDecimal(coltype[8:len(coltype)-1])
			elif 'integer' in coltype.lower():
				val=getDecimal(width+",0")
			else:
				val=printme(col,i)
			
			#print(val)
			#print("primarykey:"+str(primarykey))
			array.append(val)
			i=i+1
		
		output = escape+delim.join(array)+escape
		
		if skipcol:
			if "HEADER" in filename:
				header = output
			else:
				trailer = array.copy()
		else:
			outputlines.append(output)
		
		array.clear()
		
		
	if properties.FILE_PER_SCHEMA is True:
		outputStr = newLineChar.join(outputlines)
		save_path = properties.OUTPUT_DIR
		completeName = os.path.basename(filename)
		completeName = os.path.join(save_path,completeName[:completeName.index('.')]+".txt")
		myfile = open(completeName,'w')
		myfile.writelines(outputStr)
		myfile.close()
		outputlines.clear()
	
	if properties.FILE_PER_SCHEMA is False:
		outputStr = newLineChar.join(outputlines)
		trailer[recCountPos] = str(len(outputlines))
		outputStr = header + newLineChar + outputStr + newLineChar + escape+delim.join(trailer)+escape
		completeName = os.path.join(properties.OUTPUT_DIR,"ouput.txt")
		myfile = open(completeName,'w')
		myfile.writelines(outputStr)
		myfile.close()



