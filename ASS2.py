import heapq
class node:
    def __init__(self,char,freq,left=None,right=None):
        self.char=char
        self.freq=freq
        self.left=left
        self.right=right
        self.huff=''
    def __lt__(self,other):
        return self.freq < other.freq
def printnode(node_,val=''):
    newval=val+str(node_.huff)
    if node_.left:
        printnode(node_.left,newval)
    if node_.right:
        printnode(node_.right,newval)
    if not node_.left or not node_.right:
        print(node_.char," -> ",newval)
def huffman(char,freq):
    nodes=[]                                        # q=heapq()
    for i in range(len(char)):
        heapq.heappush(nodes,node(char[i],freq[i]))
    while len(nodes)>1:
        left=heapq.heappop(nodes)
        right=heapq.heappop(nodes)
        left.huff='0'
        right.huff='1'
        parent=node(left.char+right.char,left.freq+right.freq,left,right)
        heapq.heappush(nodes,parent)
    printnode(nodes[0])
if __name__ == "__main__":
    n = int(input("Enter the number of characters: "))
    char = []
    freq = []
    for i in range(n):
        character = input(f"Enter character {i + 1}: ")
        frequency = int(input(f"Enter frequency for character '{character}': "))
        char.append(character)
        freq.append(frequency)
    huffman(char, freq)