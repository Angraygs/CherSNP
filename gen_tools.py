import json


"""
General tools
"""

def complementary(seq):
    ans = []
    for i in seq[::-1].upper():
        if i == 'A':
            ans.append('T')
        elif i == 'T':
            ans.append('A')
        elif i == 'G':
            ans.append('C')
        elif i == 'C':
            ans.append('G')
    return ''.join(ans)


def _kmers(alphabet, table, key, k):
    if (k == 0) :
        if key not in table:
            table.append(key)
            return

    for i in range(4):
        t = key + alphabet[i]
        _kmers(alphabet, table, t, k - 1)

def generate(k=1, type='list', pseudo=0):
    alphabet = ['A', 'C', 'G', 'T']
    table = []
    _kmers(alphabet, table, '', k)
    if type == 'list':return table
    elif type =='dict':
        dict = {}
        for key in table:
            dict[key] = pseudo
        return dict


def encode_json(data, out='temp_json.js' ):
	with open(out,'w+')as report:
		json.dump(data,report,indent=4)
	report.close()

def decode_json(file):
	with open(file)as json_file:
		data = json.load(json_file)
	json_file.close()
	return data
