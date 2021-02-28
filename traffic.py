class Traffic:
    def __init__(self, fileName, solName):
        self.fileName = fileName
        self.solName  = solName

        # Open both the files
        self.sol = open(solName,"w")       # solution
        self.fil = open(fileName,"r")           # input data

        # reading the inupt file and storing variables
        self.lines      = fil.readlines()
        self.first_line = lines[0]
        self.D = int(first_line.split()[0])      # D: duration
        self.I = int(first_line.split()[1])      # I: intersections
        self.S = int(first_line.split()[2])      # S: streets
        self.V = int(first_line.split()[3])      # V: cars
        self.F = int(first_line.split()[4])      # F: bonus