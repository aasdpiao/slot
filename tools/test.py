# coding: utf-8
from prettytable import *

#from Mysql import *
import csv
import math
templates = [
[
    [0,0,0,0,0],
    [1,1,1,1,1],
    [0,0,0,0,0],
],
[
    [1,1,1,1,1],
    [0,0,0,0,0],
    [0,0,0,0,0],
],
[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,1,1,1],
],
[
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
],
[
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1],
],
[
    [0,1,0,1,0],
    [1,0,1,0,1],
    [0,0,0,0,0],
],
[
    [0,0,0,0,0],
    [1,0,1,0,1],
    [0,1,0,1,0],
],
[
    [1,0,1,0,1],
    [0,1,0,1,0],
    [0,0,0,0,0],
],
[
    [0,0,0,0,0],
    [0,1,0,1,0],
    [1,0,1,0,1],
],
[
    [0,1,1,1,0],
    [1,0,0,0,1],
    [0,0,0,0,0],
],
[
    [0,0,0,0,0],
    [1,0,0,0,1],
    [0,1,1,1,0],
],
[
    [1,0,0,0,1],
    [0,1,1,1,0],
    [0,0,0,0,0],
],
[
    [0,0,0,0,0],
    [0,1,1,1,0],
    [1,0,0,0,1],
],
[
    [1,1,0,1,1],
    [0,0,0,0,0],
    [0,0,1,0,0],
],
[
    [0,0,1,0,0],
    [0,0,0,0,0],
    [1,1,0,1,1],
],
[
    [0,0,1,0,0],
    [1,1,0,1,1],
    [0,0,0,0,0],
],
[
    [0,0,0,0,0],
    [1,1,0,1,1],
    [0,0,1,0,0],
],
[
    [1,0,1,0,1],
    [0,0,0,0,0],
    [0,1,0,1,0],
],
[
    [0,1,0,1,0],
    [0,0,0,0,0],
    [1,0,1,0,1],
],
[
    [0,1,0,0,0],
    [1,0,1,0,1],
    [0,0,0,1,0],
],
]

lineTemplate = []
dataString=[]

multipleIocnList=[
	{3:10,4:40,5:200},
	{3:5,4:20,5:100},
	{3:5,4:20,5:100},
	{3:5,4:20,5:100},
	{3:5,4:20,5:100},
	{3:20,4:100,5:500},
	{3:30,4:150,5:800},
	{3:50,4:200,5:1500},
	{3:75,4:300,5:2000},
	{3:0,4:0,5:3000},
	{3:100,4:400,5:3000},
]
Wild = 10

for x in xrange(0,20):
	template = templates[x]
	reelList = []
	lineTemplate.append(reelList)
	for i in xrange(0,5):
		reel = []
		reelList.append(reel)
		for j in xrange(0,3):
			reel.append(template[j][i])

lines = []

for x in lineTemplate:
	line = []
	lines.append(line)
	for reel in x:
		count = 0
		for element in reel:
			if element == 1: line.append(count)
			count = count + 1

def GetReverseList(sourcelist):
	reelList = []
	lineTemplate.append(reelList)
	for i in xrange(0,len(sourcelist[0])):
		reel = []
		reelList.append(reel)
		for j in xrange(0,len(sourcelist)):
			reel.append(sourcelist[j][i])
	return reelList

def GetSlotRunResult():
	result = []
	for i in xrange(0,5):
		reel = []
		result.append(reel)
		for j in xrange(0,3):
			ranNum=random.randint(1,9)
			if ranNum==9 and random.randint(1,10)<=5: #若为9（万能牌） 有50% 的概率重新获取一次
				ranNum=random.randint(1,9)   #(1,11)=1 到 11 
			if ranNum >= 2 :
				ranNum += 1
			reel.append(ranNum)
	return result

def GetSlotList(index):
	result=[[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
	ind=0
	for i in xrange(0,5):
		
		myS=numToStr(index)
		for j in xrange(0,3):
			if index==11:
				index=11
			myI=strToNum(myS,ind)
			result[i][j]=myI
			ind+=1
	return result

# 十一进制转num
# _str：十一进制str
# n:位数 (0开始)
def strToNum(_str,n):
	inT=0
	_strList=[]
	for v in _str:
		_strList.append(v)
	_strList.reverse()
	if n+1>len(_str):
		m_S="0"
	else:
		m_S=_strList[n]

	if m_S=="a":
		inT=10
	elif m_S=="b":
		inT=11
	else:
		inT=int(m_S)
	return inT+1

# 十进制转11进制
def numToStr( _int): 
	CHS_STR="0123456789a"
	if (_int < 0) :
		return null;  
	lenI = len(CHS_STR)
	chs=[]
	for c in CHS_STR:
		chs.append(c)
	n = -1
	intVal = _int
	val=[]

	while (intVal >=0 ): 

		if (intVal < lenI): 
			n =  int(intVal)
		else:  
			n = int(intVal % lenI)
		intVal = int(math.floor(intVal/lenI))
		val.append(chs[n]); 
		if intVal<=0:
			break
	vStrin=""
	val.reverse()
	for j in val:
		vStrin+=j
	return vStrin;  
 
def printTable(count,tab):
	#target = GetReverseList(tab)

	pt = PrettyTable()
	pt.add_column("index:%d"%(count),["row1", "row2", "row3"])
	pt.add_column("column1",tab[0])
	pt.add_column("column2",tab[1])
	pt.add_column("column3",tab[2])
	pt.add_column("column4",tab[3])
	pt.add_column("column5",tab[4])
	print(pt.get_string())

	

def GetSlotRunLinesResult(result):
	boardLines = []
	for index,simpleLine in enumerate(lines):
		testList = []
		for i,j in enumerate(simpleLine):
			testList.append(result[i][j])
		firstSymbol = Wild
		mathCount = 0
		iconGifList=[]
		
		for x in xrange(0,5):
			element = testList[x]

			if firstSymbol == Wild: #第一个位置，先记录
				firstSymbol = element
				iconGifList.append(simpleLine[x])
				mathCount = mathCount + 1
			elif firstSymbol == element or element == Wild:
				iconGifList.append(simpleLine[x])
				mathCount = mathCount + 1
			else:
				break
		if mathCount >= 3:
			
			#multipleIocnList[firstSymbol-1][mathCount]
			#boardLines.append([index+1,firstSymbol,mathCount])
			# boardLines.append([index+1,firstSymbol,multipleIocnList[firstSymbol-1][mathCount]])
			#print(str(firstSymbol)+"号图案出现了"+str(mathCount)+"个为"+str(multipleIocnList[firstSymbol-1][mathCount])+"倍")

			boardLines.append([index+1,iconGifList,multipleIocnList[firstSymbol-1][mathCount]])

			
	return boardLines

if __name__ == "__main__":
	#ConnectDB()
	
	# f = open('test.txt','a')
	# f.write('\n hello boy!')
	# f.close()
	# fa = open('test.txt') 
	# print(fa.read())


	#f.close()
	beishuDict={}
	shulianList=[]
	# for x in xrange(1,1000):
	x=-1
	# solist=GetSlotList()

	# while len(shulianList)<300:
	while x<=1000000:
		x=x+1

		result = GetSlotRunResult()
		# result = GetSlotList(x)
		boardLines = GetSlotRunLinesResult(result)
		linestr = str(boardLines)
		printTable(x,result)
		
	

		print(len(shulianList))
		print(boardLines)

		beishu=0
		zhonglist=[]
		zhongIconPoslist=[]
		for i in xrange(0,len(boardLines)):
			beishu=beishu+boardLines[i][2]
			zhonglist.append(boardLines[i][0])

			# zhongIconPoslist.append(boardLines[i][1])
			
			for j,simplePos in enumerate(boardLines[i][1]):
				if j>=len(zhongIconPoslist):
					iconReel=[]
					zhongIconPoslist.append(iconReel)
					iconReel.append(simplePos)
				else:
					# 遍历 zhongIconPoslist[j]里是否有 simplePos，有：进入下一次，没有：加入
					isOne=True
					for v in xrange(0,len(zhongIconPoslist[j])):
						if zhongIconPoslist[j][v]==simplePos:
							isOne=False
					if isOne==True :
						zhongIconPoslist[j].append(simplePos)
					
	
		# if beishuDict.has_key(beishu):
		# 	if beishuDict[beishu]<5:
		# 		beishuDict[beishu]=beishuDict[beishu]+1
		# 	else:
		# 		if not(beishu in shulianList):
		# 			shulianList.append(beishu)
		# 		continue
				
		# else:
		# 	beishuDict[beishu]=1
		
								#总倍数 #中奖线     #图标号
		dataString.append([x,beishu,zhonglist,zhongIconPoslist,[result[0],result[1],result[2],result[3],result[4]] ])
		
		
	print("shulian:"+str(len(shulianList)))
	csvfile = file('csv_test100W.csv', 'wb')
	writer = csv.writer(csvfile)
	writer.writerow(['id','math','lin','iconPoslist','JM'])
	writer.writerows(dataString)
	csvfile.close()	
		#SaveRecord(result,boardLines,linestr)
	#DisconnectDB()
	