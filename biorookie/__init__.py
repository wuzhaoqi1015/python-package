from Bio import Entrez
from Bio import SeqIO
import sys
import os
import re
from biorookie.download_ncbi import download_ncbi
from biorookie.read_fasta import read_fasta
from biorookie.read_genbank import read_genbank
from biorookie.analyse import base
from biorookie.analyse import complement
from biorookie.analyse import reverse_comple
from biorookie.alignment import alignment
from biorookie.help import helpme
wel=" 'biorookie' imported successfully!"
help=" You can use 'biorookie.helpme()' to view help documents!"
version=" version:v1.1.0"
print("*"*55+"\n"+wel+"\n"+"*"*55+"\n"+version+"\n"+"*"*55+"\n"+help+"\n"+"*"*55)