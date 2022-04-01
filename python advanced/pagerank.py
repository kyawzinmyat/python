class Node:
	counter=-1
	def __init__(self,name):
		self.__outgoingNode_list =[]
		self.index=self.setIndex()
		self.name =name
	
	@property
	def outgoingNode_List(self):
		return self.__outgoingNode_list
	
	
	def getNumOfOutgoingNodes(self):
			return len(self.__outgoingNode_list)
		
	def setAdjNode(self,adjNode):
		self.__outgoingNode_list.append(adjNode)
		
	def setIndex(self):
		Node.counter
		Node.counter+=1
		return Node.counter
	

	def getIndex(self):
		return self.index
		
class Graph:
		
		def __init__(self):
			
			self.nodeRankMatrix=[[]]
			self.nodesList =[]
			self.rankMatrix= []
			self.nodeRankDict={}
			
		def addNewNode(self,listOfNodes):
			for node in listOfNodes:
				self.nodesList.append(node)
			self.setRankMatrix()
			
			
			
			
			
			
		## need to refactor	
		def setNodeRankMatrix(self):
			self.initializeNodesRankMatrix()
			
				
		def calculateRank(self):
			self.setValuesForNodesRankMatrix()
			self.multiplyNodeAndRankMatrix()
			
			
			
			
			
			
		def multiplyNodeAndRankMatrix(self):
			for m in range(5):
				m=[0 for i in range(len(self.rankMatrix))]
				for i in range(len(self.nodeRankMatrix)):
					for j in range(len(self.rankMatrix)):
						m[i]+=self.rankMatrix[j]*self.nodeRankMatrix[i][j]
			
				self.rankMatrix=m
			self.setNodeRankDict()
			
	
			
			
			
			
		def multiplyMultipleTime(self):
			for i in range(1):
				self.multiplyNodeAndRankMatrix()
				
				
			
		def setValuesForNodesRankMatrix(self):
			for node in self.nodesList:
				for adjNode in node.outgoingNode_List:
					self.nodeRankMatrix[adjNode.getIndex()][node.getIndex()]=1/node.getNumOfOutgoingNodes()
				
			
			
			
			
			
		def initializeNodesRankMatrix(self):
			self.nodeRankMatrix=[[0 for j in range(len(self.nodesList))]for i in range(len(self.nodesList))]
			
			
		
		
				
			
			
		def setRankMatrix(self):
			self.setNodeRankMatrix()
			self.setValueForRankMatrix()
			
		def setValueForRankMatrix(self):
			for node in self.nodesList:
				self.rankMatrix.append(1/len(self.nodesList))
			
		def getNodesRankMatrix(self):
			return self.nodeRankMatrix
		
		def getRankMatrix(self):
			return self.rankMatrix
			
		def setNodeRankDict(self):
			for i in range(len(self.nodesList)):
				self.nodeRankDict[self.rankMatrix[i]]=self.nodesList[i]
				
				
		def getNodeRankDict(self):
			return self.nodeRankDict
				
			

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")


nodeA.setAdjNode(nodeB)
nodeB.setAdjNode(nodeC)
nodeB.setAdjNode(nodeD)
nodeB.setAdjNode(nodeA)
nodeC.setAdjNode(nodeA)
nodeC.setAdjNode(nodeD)
nodeD.setAdjNode(nodeA)
nodeD.setAdjNode(nodeB)



listOfNodes=[nodeA,nodeB,nodeC,nodeD]			
			
internet = Graph()
internet.addNewNode(listOfNodes)
#print(internet.getNodesRankMatrix())
#print(internet.getRankMatrix())		
internet.calculateRank()	
#print(internet.nodeRankMatrix)
#print(internet.getRankMatrix())


j=internet.getRankMatrix()
print(j)
l = internet.getRankMatrix()
l=sorted(l,reverse=True)
j= internet.getNodeRankDict()




