from collections import Counter
class Nodes: 
    def __init__(self, probability, symbol, left = None, right = None): 
        self.probability = probability 
        self.symbol = symbol 
        self.left = left 
        self.right = right 
        self.code = '' 
the_codes = dict() 
def CalculateCodes(node, value = ''): 
    newValue = value + str(node.code) 
    if(node.left): 
        CalculateCodes(node.left, newValue) 
    if(node.right): 
        CalculateCodes(node.right, newValue) 
    if(not node.left and not node.right): 
        the_codes[node.symbol] = newValue 
    return the_codes 
def OutputEncoded(the_data, coding): 
    encodingOutput = [] 
    for element in the_data: 
        encodingOutput.append(coding[element]) 
    the_string = ''.join([str(item) for item in encodingOutput])  	
    return the_string	
def HuffmanEncoding(the_data): 
    symbolWithProbs = Counter(the_data)
    the_symbols = symbolWithProbs.keys() 
    the_probabilities = symbolWithProbs.values() 
    print("symbols: ", the_symbols) 
    print("probabilities: ", the_probabilities) 
    the_nodes = [] 
    for symbol in the_symbols: 
        the_nodes.append(Nodes(symbolWithProbs[symbol], symbol)) 
    while len(the_nodes) > 1: 
        the_nodes = sorted(the_nodes, key = lambda x: x.probability) 
        right = the_nodes[1] 
        left = the_nodes[0] 
        left.code = 0 
        right.code = 1 
        newNode = Nodes(left.probability + right.probability, left.symbol + right.symbol, left, right) 
        the_nodes.remove(left) 
        the_nodes.remove(right) 
        the_nodes.append(newNode) 
    huffmanEncoding = CalculateCodes(the_nodes[0]) 
    print("symbols with codes", huffmanEncoding) 
    encodedOutput = OutputEncoded(the_data,huffmanEncoding) 
    return encodedOutput, the_nodes[0] 
def HuffmanDecoding(encodedData, huffmanTree): 
    treeHead = huffmanTree 
    decodedOutput = [] 
    for x in encodedData: 
        if x == '1': 
            huffmanTree = huffmanTree.right   
        elif x == '0': 
            huffmanTree = huffmanTree.left 
        try: 
            if huffmanTree.left.symbol == None and huffmanTree.right.symbol == None: 
                pass 
        except AttributeError: 
            decodedOutput.append(huffmanTree.symbol) 
            huffmanTree = treeHead 
    string = ''.join([str(item) for item in decodedOutput]) 
    return string 
the_data = input("Enter String:") 
print(the_data) 
encoding, the_tree = HuffmanEncoding(the_data) 
print("Encoded output", encoding) 
print("Decoded Output", HuffmanDecoding(encoding, the_tree)) 
