import observer as obs
import argparse
import hgvser
import trainer as train

parser = argparse.ArgumentParser(description=
    'Train Classifiers Based on Sequence and Associated GFF Annotation')
# Sequence and Annotation's path
parser.add_argument('--fasta', required=True, type=str,
    metavar='<path>', help='path to fasta file')
parser.add_argument('--gff', required=True, type=str,
    metavar='<path>', help='path to GFF3 file')
# Clf files and Dict file's path
parser.add_argument('--path', required=False, type=str,default='default/',
    metavar='<path>', help='path to classifier (.pkl) files and dictionary')
parser.add_argument('--dict', required=False, type=str,default='Jeanne.js',
    metavar='<path>', help='path to dict(.js) file')
parser.add_argument('--init', required=False, type=str,default='Katyusha.pkl',
    metavar='<path>', help='path to init classifier (.pkl) file')
parser.add_argument('--term', required=False, type=str,default='Erika.pkl',
    metavar='<path>', help='path to term classifier (.pkl) file')
parser.add_argument('--entCDS', required=False, type=str,default='Nadeshiko.pkl',
    metavar='<path>', help='path to entCDS classifier (.pkl) file')
parser.add_argument('--outCDS', required=False, type=str,default='Juliet.pkl',
    metavar='<path>', help='path to outCDS classifier (.pkl) file')
# mode for cov19 training
parser.add_argument('--mode', required=False, type=str,default='hasRNA',
    metavar='<path>', help='hasRNA or noRNA')

arg = parser.parse_args()
seq_file = arg.fasta
gff_file = arg.gff
path = arg.path
dict_file = arg.dict
init_file = arg.init
term_file = arg.term
entCDS_file = arg.entCDS
outCDS_file = arg.outCDS
mode = arg.mode

filenames = [
    path + init_file,
    path + term_file,
    path + entCDS_file,
    path + outCDS_file,
    path + dict_file
]

train.Trainer(seq_file, gff_file, filenames = filenames, mode = mode)
