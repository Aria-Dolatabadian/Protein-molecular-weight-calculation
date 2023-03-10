AminoAcids = {"A":89,"V":117,"L":131,"I":131,"P":115,"F":165,"W":204,"M":149,"G":75,"S":105,"C":121,"T":119,
      "Y":181,"N":132,"Q":146,"D":133,"E":147,"K":146,"R":174,"H":155}

ProteinSec = "MTWGHPGYMTWGHPGYMTWGHPGYMTWGHPGYMTWGHPGY"
MolecularWeight= 0
for x in ProteinSec:
    MolecularWeight = MolecularWeight + AminoAcids.get(x)
MolecularWeight = MolecularWeight - (18 * (len(ProteinSec)-1))
print("Protein molecular weight is:", MolecularWeight)
