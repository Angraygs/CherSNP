import observer as obs
import argparse
import hgvser
import trainer as train

parser = argparse.ArgumentParser(description='Just for test now')
parser.add_argument('--dict', required=False, type=str,default='None',
    metavar='<path>', help='path to dict(.js) file')
parser.add_argument('--init', required=False, type=str,default='None',
    metavar='<path>', help='path to init classifier (.pkl) file')
parser.add_argument('--term', required=False, type=str,default='None',
    metavar='<path>', help='path to term classifier (.pkl) file')
parser.add_argument('--entCDS', required=False, type=str,default='None',
    metavar='<path>', help='path to entCDS classifier (.pkl) file')
parser.add_argument('--outCDS', required=False, type=str,default='None',
    metavar='<path>', help='path to outCDS classifier (.pkl) file')
# Need more parser for filenames

arg = parser.parse_args()
# seq_file = arg.fasta
# gff_file = arg.gff

clfs = train.Classifiers(filenames = "Default")
print(clfs.init.predict([[-1,-1,-1]]))


# test = hgvser.HGVS('c.123A>T')
# print(test.type, test.prefix, test.info.alt, test.info.ref, test.info.pos)
