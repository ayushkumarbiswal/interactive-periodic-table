# Importing required modules
import tkinter as tk
from tkinter import messagebox
import random
import mysql.connector as msql

# Function to display Interactive Periodic Table
def explore():
    
    # Creating toplevel window under root
    wind1 = tk.Toplevel(root)
    wind1.title("Interactive Periodic Table")
    wind1.iconbitmap("periodic-table.ico")
    wind1['bg'] = "white"

    # Creating frame to contain the periodic table
    ptable = tk.Frame(wind1, bg = "white")
    ptable.pack(side = "left")

    # Initialising element data

    # element name
    nm = ["", "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
          "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium",
          "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
          "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
          "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin",
          "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
          "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium",
          "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury",
          "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium",
          "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium",
          "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium",
          "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"]

    # symbol
    sym = ["", "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
           "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
           "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
           "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
           "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
           "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
           "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
           "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
           "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
           "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
           "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
           "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

    # atomic number
    Z = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
         "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
         "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
         "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
         "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100",
         "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118"]

    # atomic weight
    AW = ["", 1.0079, 4.0026, 6.941, 9.0122, 10.811, 12.0107, 14.0067, 15.9994, 18.9984, 20.1797,
          22.9897, 24.305, 26.9815, 28.0855, 30.9738, 32.065, 35.453, 39.948, 39.0983, 40.078,
          44.9559, 47.867, 50.9415, 51.9961, 54.938, 55.845, 58.6934, 58.9332, 63.546, 65.38,
          69.723, 72.63, 74.9216, 78.96, 79.904, 83.8, 85.4678, 87.62, 88.9059, 91.224,
          92.9064, 95.94, 98, 101.07, 102.9055, 106.42, 107.8682, 112.411, 114.818, 118.71,
          121.76, 127.6, 126.9045, 131.293, 132.9055, 137.327, 138.9055, 140.116, 140.9077, 144.242,
          145, 150.36, 151.964, 157.25, 158.9253, 162.5, 164.9303, 167.259, 168.9342, 173.04,
          174.967, 178.49, 180.9479, 183.84, 186.207, 190.23, 192.217, 195.078, 196.9665, 200.59,
          204.3833, 207.2, 208.9804, 209, 210, 222, 223, 226, 227, 232.0381,
          231.0359, 238.0289, 237, 244, 243, 247, 247, 251, 252, 257,
          258, 259, 266, 267, 268, 269, 270, 269, 278, 281,
          282, 285, 286, 289, 290, 293, 294, 294]

    # atomic radius
    R = ["", "0.32", "0.37", "1.30", "0.99", "0.84", "0.75", "0.71", "0.64", "0.60", "0.62",
         "1.60", "1.40", "1.24", "1.14", "1.09", "1.04", "1.00", "1.01", "2.00", "1.74",
         "1.59", "1.48", "1.44", "1.30", "1.29", "1.24", "1.18", "1.17", "1.22", "1.20",
         "1.23", "1.20", "1.20", "1.18", "1.17", "1.16", "2.15", "1.90", "1.76", "1.64",
         "1.56", "1.46", "1.38", "1.36", "1.34", "1.30", "1.36", "1.40", "1.42", "1.40",
         "1.40", "1.37", "1.36", "1.36", "2.38", "2.06", "1.94", "1.84", "1.90", "1.88",
         "1.86", "1.85", "1.83", "1.82", "1.81", "1.80", "1.79", "1.77", "1.77", "1.78",
         "1.74", "1.64", "1.58", "1.50", "1.41", "1.36", "1.32", "1.30", "1.30", "1.32",
         "1.44", "1.45", "1.50", "1.42", "1.48", "1.46", "2.42", "2.11", "2.01", "1.90",
         "1.84", "1.83", "1.80", "1.80", "1.73", "1.68", "1.68", "1.68", "1.65", "1.67",
         "1.73", "1.76", "1.61", "1.57", "1.49", "1.43", "1.41", "1.34", "1.29", "1.28",
         "1.21", "1.22", "1.36", "1.43", "1.62", "1.75", "1.65", "1.57"]

    # electronic configuration
    EC = ["", "1s¹", "1s²", "[He] 2s¹", "[He] 2s²", "[He] 2s² 2p¹",
          "[He] 2s² 2p²", "[He] 2s² 2p³", "[He] 2s² 2p⁴", "[He] 2s² 2p⁵", "1s² 2s² 2p⁶",
          "[Ne] 3s¹", "[Ne] 3s²", "[Ne] 3s² 3p¹", "[Ne] 3s² 3p²", "[Ne] 3s² 3p³",
          "[Ne] 3s² 3p⁴", "[Ne] 3s² 3p⁵", "1s² 2s² 2p⁶ 3s² 3p⁶", "[Ar] 4s¹", "[Ar] 4s²",
          "[Ar] 3d¹ 4s²", "[Ar] 3d² 4s²", "[Ar] 3d³ 4s²", "[Ar] 3d⁵ 4s¹", "[Ar] 3d⁵ 4s²",
          "[Ar] 3d⁶ 4s²", "[Ar] 3d⁷ 4s²", "3d⁸ 4s²", "[Ar] 3d¹⁰ 4s¹", "[Ar] 3d¹⁰ 4s²",
          "[Ar] 3d¹⁰ 4s² 4p¹", "[Ar] 3d¹⁰ 4s² 4p²", "[Ar] 3d¹⁰ 4s² 4p³", "[Ar] 3d¹⁰ 4s² 4p⁴", "[Ar] 3d¹⁰ 4s² 4p⁵",
          "1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶", "[Kr] 5s¹", "[Kr] 5s²", "[Kr] 4d¹ 5s²", "[Kr] 4d² 5s²",
          "[Kr] 4d⁴ 5s¹", "[Kr] 4d⁵ 5s¹", "[Kr] 4d⁵ 5s²", "[Kr] 4d⁷ 5s¹", "[Kr] 4d⁸ 5s¹",
          "[Kr] 4d¹⁰", "[Kr] 4d¹⁰ 5s¹", "[Kr] 4d¹⁰ 5s²", "[Kr] 4d¹⁰ 5s² 5p¹", "[Kr] 4d¹⁰ 5s² 5p²",
          "[Kr] 4d¹⁰ 5s² 5p³", "[Kr] 4d¹⁰ 5s² 5p⁴", "[Kr] 4d¹⁰ 5s² 5p⁵", "1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁶", "[Xe] 6s¹",
          "[Xe] 6s²", "[Xe] 5d¹ 6s²", "[Xe] 4f¹ 5d¹ 6s²", "[Xe] 4f³ 6s²", "[Xe] 4f⁴ 6s²",
          "[Xe] 4f⁵ 6s²", "[Xe] 4f⁶ 6s²", "[Xe] 4f⁷ 6s²", "[Xe] 4f⁷ 5d¹ 6s²", "[Xe] 4f⁹ 6s²",
          "[Xe] 4f¹⁰ 6s²", "[Xe] 4f¹¹ 6s²", "[Xe] 4f¹² 6s²", "[Xe] 4f¹³ 6s²", "[Xe] 4f¹⁴ 6s²",
          "[Xe] 4f¹⁴ 5d¹ 6s²", "[Xe] 4f¹⁴ 5d² 6s²", "[Xe] 4f¹⁴ 5d³ 6s²", "[Xe] 4f¹⁴ 5d⁴ 6s²", "[Xe] 4f¹⁴ 5d⁵ 6s² ",
          "[Xe] 4f¹⁴ 5d⁶ 6s²", "[Xe] 4f¹⁴ 5d⁷ 6s²", "[Xe] 4f¹⁴ 5d⁹ 6s¹", "[Xe] 4f¹⁴ 5d¹⁰ 6s¹", "[Xe] 4f¹⁴ 5d¹⁰ 6s²",
          "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p¹", "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p²", "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p³", "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁴", "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁵",
          "1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁶ 4f¹⁴ 5d¹⁰ 6s² 6p⁶", "[Rn] 7s¹", "[Rn] 7s²", "[Rn] 6d¹ 7s²", "[Rn] 6d² 7s²",
          "[Rn] 5f² 6d¹ 7s²", "[Rn] 5f³ 6d¹ 7s²", "[Rn] 5f⁴ 6d¹ 7s²", "[Rn] 5f⁶ 7s²", "[Rn] 5f⁷ 7s²",
          "[Rn] 5f⁷ 6d¹ 7s²", "[Rn] 5f⁹ 7s²", "[Rn] 5f¹⁰ 7s²", "[Rn] 5f¹¹ 7s²", "[Rn] 5f¹² 7s²",
          "[Rn] 5f¹³ 7s²", "[Rn] 5f¹⁴ 7s²", "[Rn] 5f¹⁴ 7s² 7p¹", "[Rn] 5f¹⁴ 6d² 7s²", "[Rn] 5f¹⁴ 6d³ 7s²",
          "[Rn] 5f¹⁴ 6d⁴ 7s²", "[Rn] 5f¹⁴ 6d⁵ 7s²", "[Rn] 5f¹⁴ 6d⁶ 7s²", "[Rn] 5f¹⁴ 6d⁷ 7s²", "[Rn] 5f¹⁴ 6d⁸ 7s²",
          "[Rn] 5f¹⁴ 6d⁹ 7s²", "[Rn] 5f¹⁴ 6d¹⁰ 7s²", "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p¹", "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p²", "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p³",
          "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁴", "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁵",
          "1s² 2s² 2p⁶ 3s² 3p⁶ 3d¹⁰ 4s² 4p⁶ 4d¹⁰ 5s² 5p⁶ 4f¹⁴ 5d¹⁰ 6s² 6p⁶ 5f¹⁴ 6d¹⁰ 7s² 7p⁶"]

    # oxidation state(s)
    OS = ["", "−1 +1", "0", "+1", "+2", "+3", "-4 -3 -2 -1 0 +1 +2 +3 +4", "-3 +3 +5", "-2", "-1", "0",
          "+1", "+2", "+3", "-4 +4", "-3 +3 +5", "-2 +2 +4 +6", "-1 +1 +3 +5 +7", "0", "+1", "+2",
          "+3", "+2 +3 +4", "+2 +3 +4 +5", "+2 +3 +6", "+2 +3 +4 +6 +7", "+2 +3", "+2 +3", "+2", "+1 +2", "+2",
          "+3", "-4 +2 +4", "-3 +3 +5", "-2 +2 +4 +6", "-1 +1 +3 +5", "0", "+1", "+2", "+3", "+4",
          "+5", "+4 +6", "+4 +7", "+3 +4", "+3", "0 +2 +4", "+1", "+2", "+3", "-4 +2 +4",
          "-3 +3 +5", "-2 +2 +4 +6", "-1 +1 +3 +5 +7", "0", "+1", "+2", "+3", "+3 +4", "+3", "+3",
          "+3", "+3", "+2 +3", "+3", "+3", "+3", "+3", "+3", "+3", "+3",
          "+3", "+4", "+5", "+4 +6", "+4 +7", "+4", "+3 +4", "+2 +4", "+1 +3", "+1 +2",
          "+1 +3", "+2 +4", "+3", "-2 +2 +4", "-1 +1", "+2", "+1", "+2", "+3", "+4",
          "+5", "+4 +6", "+5", "+4", "+3", "+3", "+3", "+3", "+3", "+3",
          "+3", "+2", "+3", "+4", "+5", "+6", "+7", "+8", "+1 +3 +6", "0 +2 +8",
          "+3", "+2", "+1 +3", "+2", "+1 +3", "+2", "+1 +3", "+2 +4"]

    # ionization energy
    IE = ["", 1312.0, 2372.3, 520.2, 899.5, 800.6, 1086.5, 1402.3, 1313.9, 1681.0, 2080.7,
          495.8, 737.7, 577.5, 786.5, 1011.8, 999.6, 1251.2, 1520.6, 418.8, 589.8,
          633.1, 658.8, 650.9, 652.9, 717.3, 762.5, 760.4, 737.1, 745.5, 906.4,
          578.8, 762.0, 947.0, 941.0, 1139.9, 1350.8, 403.0, 549.5, 600.0, 640.1,
          652.1, 684.3, 702.0, 710.2, 719.7, 804.4, 731.0, 867.8, 558.3, 708.6,
          834, 869.3, 1008.4, 1170.4, 375.7, 502.9, 538.1, 534.4, 527.0, 533.1,
          540.0, 544.5, 547.1, 593.4, 565.8, 573.0, 581.0, 589.3, 596.7, 603.4,
          523.5, 658.5, 761.0, 770.0, 760.0, 840.0, 880.0, 870.0, 890.1, 1007.1,
          589.4, 715.6, 703.0, 812.1, 899.0, 1037.0, 393.0, 509.3, 499.0, 587.0,
          568.0, 597.6, 604.5, 584.7, 578.0, 581.0, 601.0, 608.0, 619.0, 629.0,
          636.0, 639.0, 479.0, 580.0, 665.0, 757.0, 740.0, 730.0, 800.0, 960.0,
          1020.0, 1155.0, 707.2, 832.2, 538.3, 663.9, 736.9, 860.1]

    # Function to display element data
    def display(n):
        messagebox.showinfo(nm[n],
                            "Symbol: {} \
                            \nAtomic Number: {} \
                            \nAtomic Weight: {} \
                            \nAtomic Radius (in Å): {} \
                            \nElectron Configuration: {} \
                            \nCommon Oxidation State(s): {} \
                            \nIonisation Energy (in kJ/mol): {}".format(sym[n], Z[n], AW[n], R[n], EC[n], OS[n], IE[n]))

    # Function to search for an element
    def search():

        # Get query from search box
        global query
        query = sbox.get()
        if query.islower():
            query = query.capitalize()

        # Search by element name
        if query in nm:
            result = nm.index(query)
            display(result)

        # Search by symbol
        elif query in sym:
            result = sym.index(query)
            display(result)

        # Search by atomic number
        elif query in Z:
            result = Z.index(query)
            display(result)

        # Error message for invalid search query
        else :
            messagebox.askretrycancel("Not Found", "No matching results found. Please check your input and try again")

    # Creating labels for group number and period number
    
    g1 = tk.Label(ptable, text = "1")
    g2 = tk.Label(ptable, text = "2")
    g3 = tk.Label(ptable, text = "3")
    g4 = tk.Label(ptable, text = "4")
    g5 = tk.Label(ptable, text = "5")
    g6 = tk.Label(ptable, text = "6")
    g7 = tk.Label(ptable, text = "7")
    g8 = tk.Label(ptable, text = "8")
    g9 = tk.Label(ptable, text = "9")
    g10 = tk.Label(ptable, text = "10")
    g11 = tk.Label(ptable, text = "11")
    g12 = tk.Label(ptable, text = "12")
    g13 = tk.Label(ptable, text = "13")
    g14 = tk.Label(ptable, text = "14")
    g15 = tk.Label(ptable, text = "15")
    g16 = tk.Label(ptable, text = "16")
    g17 = tk.Label(ptable, text = "17")
    g18 = tk.Label(ptable, text = "18")

    g1.grid(row = 0, column = 1)
    g2.grid(row = 0, column = 2)
    g3.grid(row = 0, column = 3)
    g4.grid(row = 0, column = 4)
    g5.grid(row = 0, column = 5)
    g6.grid(row = 0, column = 6)
    g7.grid(row = 0, column = 7)
    g8.grid(row = 0, column = 8)
    g9.grid(row = 0, column = 9)
    g10.grid(row = 0, column = 10)
    g11.grid(row = 0, column = 11)
    g12.grid(row = 0, column = 12)
    g13.grid(row = 0, column = 13)
    g14.grid(row = 0, column = 14)
    g15.grid(row = 0, column = 15)
    g16.grid(row = 0, column = 16)
    g17.grid(row = 0, column = 17)
    g18.grid(row = 0, column = 18)

    p1 = tk.Label(ptable, text = "1")
    p2 = tk.Label(ptable, text = "2")
    p3 = tk.Label(ptable, text = "3")
    p4 = tk.Label(ptable, text = "4")
    p5 = tk.Label(ptable, text = "5")
    p6 = tk.Label(ptable, text = "6")
    p7 = tk.Label(ptable, text = "7")

    p1.grid(row = 2, column = 0)
    p2.grid(row = 3, column = 0)
    p3.grid(row = 4, column = 0)
    p4.grid(row = 5, column = 0)
    p5.grid(row = 6, column = 0)
    p6.grid(row = 7, column = 0)
    p7.grid(row = 8, column = 0)

    # Creating element buttons
    e1 = tk.Button(ptable, text = sym[1], height = 2, width = 5, bg = 'gold2', fg = 'white', command = lambda: display(1))
    e2 = tk.Button(ptable, text = sym[2], height = 2, width = 5, bg = 'cyan3', fg = 'white', command = lambda: display(2))
    e3 = tk.Button(ptable, text = sym[3], height = 2, width = 5, bg = 'violet', fg = 'white', command = lambda: display(3))
    e4 = tk.Button(ptable, text = sym[4], height = 2, width = 5, bg = 'dark green', fg = 'white', command = lambda: display(4))
    e5 = tk.Button(ptable, text = sym[5], height = 2, width = 5, bg = 'dark khaki', fg = 'white', command = lambda: display(5))
    e6 = tk.Button(ptable, text = sym[6], height = 2, width = 5, bg = 'gold2', fg = 'white', command = lambda: display(6))
    e7 = tk.Button(ptable, text = sym[7], height = 2, width = 5, bg = 'gold2', fg = 'white', command = lambda: display(7))
    e8 = tk.Button(ptable, text = sym[8], height = 2, width = 5, bg = 'gold2', fg = 'white', command = lambda: display(8))
    e9 = tk.Button(ptable, text = sym[9], height = 2, width = 5, bg = 'green3', fg = 'white', command = lambda: display(9))
    e10 = tk.Button(ptable, text = sym[10], height = 2, width = 5, bg = 'cyan3', fg = 'white', command = lambda: display(10))
    e11 = tk.Button(ptable, text = sym[11], height = 2, width = 5, bg = 'violet', fg = 'white', command = lambda: display(11))
    e12 = tk.Button(ptable, text = sym[12], height = 2, width = 5, bg = 'dark green', fg = 'white', command = lambda: display(12))
    e13 = tk.Button(ptable, text = sym[13], height = 2, width = 5, bg = 'silver', fg = 'white', command = lambda: display(13))
    e14 = tk.Button(ptable, text = sym[14], height = 2, width = 5, bg = 'dark khaki', fg = 'white', command = lambda: display(14))
    e15 = tk.Button(ptable, text = sym[15], height = 2, width = 5, bg = 'gold2', fg = 'white', command = lambda: display(15))
    e16 = tk.Button(ptable, text = sym[16], height = 2, width = 5, bg = 'gold2', fg = 'white', command = lambda: display(16))
    e17 = tk.Button(ptable, text = sym[17], height = 2, width = 5, bg = 'green3', fg = 'white', command = lambda: display(17))
    e18 = tk.Button(ptable, text = sym[18], height = 2, width = 5, bg = 'cyan3', fg = 'white', command = lambda: display(18))
    e19 = tk.Button(ptable, text = sym[19], height = 2, width = 5, bg = 'violet', fg = 'white', command = lambda: display(19))
    e20 = tk.Button(ptable, text = sym[20], height = 2, width = 5, bg = 'dark green', fg = 'white', command = lambda: display(20))
    e21 = tk.Button(ptable, text = sym[21], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(21))
    e22 = tk.Button(ptable, text = sym[22], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(22))
    e23 = tk.Button(ptable, text = sym[23], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(23))
    e24 = tk.Button(ptable, text = sym[24], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(24))
    e25 = tk.Button(ptable, text = sym[25], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(25))
    e26 = tk.Button(ptable, text = sym[26], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(26))
    e27 = tk.Button(ptable, text = sym[27], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(27))
    e28 = tk.Button(ptable, text = sym[28], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(28))
    e29 = tk.Button(ptable, text = sym[29], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(29))
    e30 = tk.Button(ptable, text = sym[30], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(30))
    e31 = tk.Button(ptable, text = sym[31], height = 2, width = 5, bg = 'silver', fg = 'white', command = lambda: display(31))
    e32 = tk.Button(ptable, text = sym[32], height = 2, width = 5, bg = 'dark khaki', fg = 'white', command = lambda: display(32))
    e33 = tk.Button(ptable, text = sym[33], height = 2, width = 5, bg = 'dark khaki', fg = 'white', command = lambda: display(33))
    e34 = tk.Button(ptable, text = sym[34], height = 2, width = 5, bg = 'gold2', fg = 'white', command = lambda: display(34))
    e35 = tk.Button(ptable, text = sym[35], height = 2, width = 5, bg = 'green3', fg = 'white', command = lambda: display(35))
    e36 = tk.Button(ptable, text = sym[36], height = 2, width = 5, bg = 'cyan3', fg = 'white', command = lambda: display(36))
    e37 = tk.Button(ptable, text = sym[37], height = 2, width = 5, bg = 'violet', fg = 'white', command = lambda: display(37))
    e38 = tk.Button(ptable, text = sym[38], height = 2, width = 5, bg = 'dark green', fg = 'white', command = lambda: display(38))
    e39 = tk.Button(ptable, text = sym[39], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(39))
    e40 = tk.Button(ptable, text = sym[40], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(40))
    e41 = tk.Button(ptable, text = sym[41], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(41))
    e42 = tk.Button(ptable, text = sym[42], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(42))
    e43 = tk.Button(ptable, text = sym[43], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(43))
    e44 = tk.Button(ptable, text = sym[44], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(44))
    e45 = tk.Button(ptable, text = sym[45], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(45))
    e46 = tk.Button(ptable, text = sym[46], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(46))
    e47 = tk.Button(ptable, text = sym[47], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(47))
    e48 = tk.Button(ptable, text = sym[48], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(48))
    e49 = tk.Button(ptable, text = sym[49], height = 2, width = 5, bg = 'silver', fg = 'white', command = lambda: display(49))
    e50 = tk.Button(ptable, text = sym[50], height = 2, width = 5, bg = 'silver', fg = 'white', command = lambda: display(50))
    e51 = tk.Button(ptable, text = sym[51], height = 2, width = 5, bg = 'dark khaki', fg = 'white', command = lambda: display(51))
    e52 = tk.Button(ptable, text = sym[52], height = 2, width = 5, bg = 'dark khaki', fg = 'white', command = lambda: display(52))
    e53 = tk.Button(ptable, text = sym[53], height = 2, width = 5, bg = 'green3', fg = 'white', command = lambda: display(53))
    e54 = tk.Button(ptable, text = sym[54], height = 2, width = 5, bg = 'cyan3', fg = 'white', command = lambda: display(54))
    e55 = tk.Button(ptable, text = sym[55], height = 2, width = 5, bg = 'violet', fg = 'white', command = lambda: display(55))
    e56 = tk.Button(ptable, text = sym[56], height = 2, width = 5, bg = 'dark green', fg = 'white', command = lambda: display(56))
    f1 = tk.Label(ptable, text = "*")
    la = tk.Label(ptable, text = "*")
    e57 = tk.Button(ptable, text = sym[57], height = 2, width = 5, bg = 'pink3', fg = 'white', command = lambda: display(57))
    e58 = tk.Button(ptable, text = sym[58], height = 2, width = 5, bg = 'pink3', fg = 'white', command = lambda: display(58))
    e59 = tk.Button(ptable, text = sym[59], height = 2, width = 5, bg = 'pink3', fg = 'white', command = lambda: display(59))
    e60 = tk.Button(ptable, text = sym[60], height = 2, width = 5, bg = 'pink3', fg = 'white', command = lambda: display(60))
    e61 = tk.Button(ptable, text = sym[61], height = 2, width = 5, bg = 'pink3', fg = 'white', command = lambda: display(61))
    e62 = tk.Button(ptable, text = sym[62], height = 2, width = 5, bg = 'pink3', fg = 'white', command = lambda: display(62))
    e63 = tk.Button(ptable, text = sym[63], height = 2, width = 5, bg = 'pink3', fg = 'white', command = lambda: display(63))
    e64 = tk.Button(ptable, text = sym[64], height = 2, width = 5, bg = 'pink3', fg = 'white', command = lambda: display(64))
    e65 = tk.Button(ptable, text = sym[65], height = 2, width = 5, bg = 'pink3', fg = 'white', command = lambda: display(65))
    e66 = tk.Button(ptable, text = sym[66], height = 2, width = 5, bg = 'pink3', fg = 'white', command = lambda: display(66))
    e67 = tk.Button(ptable, text = sym[67], height = 2, width = 5, bg = 'pink3', fg = 'white', command = lambda: display(67))
    e68 = tk.Button(ptable, text = sym[68], height = 2, width = 5, bg = 'pink3', fg = 'white', command = lambda: display(68))
    e69 = tk.Button(ptable, text = sym[69], height = 2, width = 5, bg = 'pink3', fg = 'white', command = lambda: display(69))
    e70 = tk.Button(ptable, text = sym[70], height = 2, width = 5, bg = 'pink3', fg = 'white', command = lambda: display(70))
    e71 = tk.Button(ptable, text = sym[71], height = 2, width = 5, bg = 'pink3', fg = 'white', command = lambda: display(71))
    e72 = tk.Button(ptable, text = sym[72], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(72))
    e73 = tk.Button(ptable, text = sym[73], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(73))
    e74 = tk.Button(ptable, text = sym[74], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(74))
    e75 = tk.Button(ptable, text = sym[75], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(75))
    e76 = tk.Button(ptable, text = sym[76], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(76))
    e77 = tk.Button(ptable, text = sym[77], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(77))
    e78 = tk.Button(ptable, text = sym[78], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(78))
    e79 = tk.Button(ptable, text = sym[79], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(79))
    e80 = tk.Button(ptable, text = sym[80], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(80))
    e81 = tk.Button(ptable, text = sym[81], height = 2, width = 5, bg = 'silver', fg = 'white', command = lambda: display(81))
    e82 = tk.Button(ptable, text = sym[82], height = 2, width = 5, bg = 'silver', fg = 'white', command = lambda: display(82))
    e83 = tk.Button(ptable, text = sym[83], height = 2, width = 5, bg = 'silver', fg = 'white', command = lambda: display(83))
    e84 = tk.Button(ptable, text = sym[84], height = 2, width = 5, bg = 'dark khaki', fg = 'white', command = lambda: display(84))
    e85 = tk.Button(ptable, text = sym[85], height = 2, width = 5, bg = 'dark khaki', fg = 'white', command = lambda: display(85))
    e86 = tk.Button(ptable, text = sym[86], height = 2, width = 5, bg = 'cyan3', fg = 'white', command = lambda: display(86))
    e87 = tk.Button(ptable, text = sym[87], height = 2, width = 5, bg = 'violet', fg = 'white', command = lambda: display(87))
    e88 = tk.Button(ptable, text = sym[88], height = 2, width = 5, bg = 'dark green', fg = 'white', command = lambda: display(88))
    f2 = tk.Label(ptable, text = "**")
    ac = tk.Label(ptable, text = "**")
    e89 = tk.Button(ptable, text = sym[89], height = 2, width = 5, bg = 'deep pink3', fg = 'white', command = lambda: display(89))
    e90 = tk.Button(ptable, text = sym[90], height = 2, width = 5, bg = 'deep pink3', fg = 'white', command = lambda: display(90))
    e91 = tk.Button(ptable, text = sym[91], height = 2, width = 5, bg = 'deep pink3', fg = 'white', command = lambda: display(91))
    e92 = tk.Button(ptable, text = sym[92], height = 2, width = 5, bg = 'deep pink3', fg = 'white', command = lambda: display(92))
    e93 = tk.Button(ptable, text = sym[93], height = 2, width = 5, bg = 'deep pink3', fg = 'white', command = lambda: display(93))
    e94 = tk.Button(ptable, text = sym[94], height = 2, width = 5, bg = 'deep pink3', fg = 'white', command = lambda: display(94))
    e95 = tk.Button(ptable, text = sym[95], height = 2, width = 5, bg = 'deep pink3', fg = 'white', command = lambda: display(95))
    e96 = tk.Button(ptable, text = sym[96], height = 2, width = 5, bg = 'deep pink3', fg = 'white', command = lambda: display(96))
    e97 = tk.Button(ptable, text = sym[97], height = 2, width = 5, bg = 'deep pink3', fg = 'white', command = lambda: display(97))
    e98 = tk.Button(ptable, text = sym[98], height = 2, width = 5, bg = 'deep pink3', fg = 'white', command = lambda: display(98))
    e99 = tk.Button(ptable, text = sym[99], height = 2, width = 5, bg = 'deep pink3', fg = 'white', command = lambda: display(99))
    e100 = tk.Button(ptable, text = sym[100], height = 2, width = 5, bg = 'deep pink3', fg = 'white', command = lambda: display(100))
    e101 = tk.Button(ptable, text = sym[101], height = 2, width = 5, bg = 'deep pink3', fg = 'white', command = lambda: display(101))
    e102 = tk.Button(ptable, text = sym[102], height = 2, width = 5, bg = 'deep pink3', fg = 'white', command = lambda: display(102))
    e103 = tk.Button(ptable, text = sym[103], height = 2, width = 5, bg = 'deep pink3', fg = 'white', command = lambda: display(103))
    e104 = tk.Button(ptable, text = sym[104], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(104))
    e105 = tk.Button(ptable, text = sym[105], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(105))
    e106 = tk.Button(ptable, text = sym[106], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(106))
    e107 = tk.Button(ptable, text = sym[107], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(107))
    e108 = tk.Button(ptable, text = sym[108], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(108))
    e109 = tk.Button(ptable, text = sym[109], height = 2, width = 5, command = lambda: display(109))
    e110 = tk.Button(ptable, text = sym[110], height = 2, width = 5, command = lambda: display(110))
    e111 = tk.Button(ptable, text = sym[111], height = 2, width = 5, command = lambda: display(111))
    e112 = tk.Button(ptable, text = sym[112], height = 2, width = 5, bg = 'salmon', fg = 'white', command = lambda: display(112))
    e113 = tk.Button(ptable, text = sym[113], height = 2, width = 5, command = lambda: display(113))
    e114 = tk.Button(ptable, text = sym[114], height = 2, width = 5, command = lambda: display(114))
    e115 = tk.Button(ptable, text = sym[115], height = 2, width = 5, command = lambda: display(115))
    e116 = tk.Button(ptable, text = sym[116], height = 2, width = 5, command = lambda: display(116))
    e117 = tk.Button(ptable, text = sym[117], height = 2, width = 5, command = lambda: display(117))
    e118 = tk.Button(ptable, text = sym[118], height = 2, width = 5, command = lambda: display(118))
    blank1 = tk.Label(ptable, text = "")
    blank2 = tk.Label(ptable, text = "")

    e1.grid(row = 2, column = 1)
    e2.grid(row = 2, column = 18)
    e3.grid(row = 3, column = 1)
    e4.grid(row = 3, column = 2)
    e5.grid(row = 3, column = 13)
    e6.grid(row = 3, column = 14)
    e7.grid(row = 3, column = 15)
    e8.grid(row = 3, column = 16)
    e9.grid(row = 3, column = 17)
    e10.grid(row = 3, column = 18)
    e11.grid(row = 4, column = 1)
    e12.grid(row = 4, column = 2)
    e13.grid(row = 4, column = 13)
    e14.grid(row = 4, column = 14)
    e15.grid(row = 4, column = 15)
    e16.grid(row = 4, column = 16)
    e17.grid(row = 4, column = 17)
    e18.grid(row = 4, column = 18)
    e19.grid(row = 5, column = 1)
    e20.grid(row = 5, column = 2)
    e21.grid(row = 5, column = 3)
    e22.grid(row = 5, column = 4)
    e23.grid(row = 5, column = 5)
    e24.grid(row = 5, column = 6)
    e25.grid(row = 5, column = 7)
    e26.grid(row = 5, column = 8)
    e27.grid(row = 5, column = 9)
    e28.grid(row = 5, column = 10)
    e29.grid(row = 5, column = 11)
    e30.grid(row = 5, column = 12)
    e31.grid(row = 5, column = 13)
    e32.grid(row = 5, column = 14)
    e33.grid(row = 5, column = 15)
    e34.grid(row = 5, column = 16)
    e35.grid(row = 5, column = 17)
    e36.grid(row = 5, column = 18)
    e37.grid(row = 6, column = 1)
    e38.grid(row = 6, column = 2)
    e39.grid(row = 6, column = 3)
    e40.grid(row = 6, column = 4)
    e41.grid(row = 6, column = 5)
    e42.grid(row = 6, column = 6)
    e43.grid(row = 6, column = 7)
    e44.grid(row = 6, column = 8)
    e45.grid(row = 6, column = 9)
    e46.grid(row = 6, column = 10)
    e47.grid(row = 6, column = 11)
    e48.grid(row = 6, column = 12)
    e49.grid(row = 6, column = 13)
    e50.grid(row = 6, column = 14)
    e51.grid(row = 6, column = 15)
    e52.grid(row = 6, column = 16)
    e53.grid(row = 6, column = 17)
    e54.grid(row = 6, column = 18)
    e55.grid(row = 7, column = 1)
    e56.grid(row = 7, column = 2)
    f1.grid(row = 7, column = 3)
    e72.grid(row = 7, column = 4)
    e73.grid(row = 7, column = 5)
    e74.grid(row = 7, column = 6)
    e75.grid(row = 7, column = 7)
    e76.grid(row = 7, column = 8)
    e77.grid(row = 7, column = 9)
    e78.grid(row = 7, column = 10)
    e79.grid(row = 7, column = 11)
    e80.grid(row = 7, column = 12)
    e81.grid(row = 7, column = 13)
    e82.grid(row = 7, column = 14)
    e83.grid(row = 7, column = 15)
    e84.grid(row = 7, column = 16)
    e85.grid(row = 7, column = 17)
    e86.grid(row = 7, column = 18)
    e87.grid(row = 8, column = 1)
    e88.grid(row = 8, column = 2)
    f2.grid(row = 8, column = 3)
    e104.grid(row = 8, column = 4)
    e105.grid(row = 8, column = 5)
    e106.grid(row = 8, column = 6)
    e107.grid(row = 8, column = 7)
    e108.grid(row = 8, column = 8)
    e109.grid(row = 8, column = 9)
    e110.grid(row = 8, column = 10)
    e111.grid(row = 8, column = 11)
    e112.grid(row = 8, column = 12)
    e113.grid(row = 8, column = 13)
    e114.grid(row = 8, column = 14)
    e115.grid(row = 8, column = 15)
    e116.grid(row = 8, column = 16)
    e117.grid(row = 8, column = 17)
    e118.grid(row = 8, column = 18)
    blank1.grid(row = 9, column = 1)
    la.grid(row = 10, column = 3)
    e57.grid(row = 10, column = 4)
    e58.grid(row = 10, column = 5)
    e59.grid(row = 10, column = 6)
    e60.grid(row = 10, column = 7)
    e61.grid(row = 10, column = 8)
    e62.grid(row = 10, column = 9)
    e63.grid(row = 10, column = 10)
    e64.grid(row = 10, column = 11)
    e65.grid(row = 10, column = 12)
    e66.grid(row = 10, column = 13)
    e67.grid(row = 10, column = 14)
    e68.grid(row = 10, column = 15)
    e69.grid(row = 10, column = 16)
    e70.grid(row = 10, column = 17)
    e71.grid(row = 10, column = 18)
    ac.grid(row = 11, column = 3)
    e89.grid(row = 11, column = 4)
    e90.grid(row = 11, column = 5)
    e91.grid(row = 11, column = 6)
    e92.grid(row = 11, column = 7)
    e93.grid(row = 11, column = 8)
    e94.grid(row = 11, column = 9)
    e95.grid(row = 11, column = 10)
    e96.grid(row = 11, column = 11)
    e97.grid(row = 11, column = 12)
    e98.grid(row = 11, column = 13)
    e99.grid(row = 11, column = 14)
    e100.grid(row = 11, column = 15)
    e101.grid(row = 11, column = 16)
    e102.grid(row = 11, column = 17)
    e103.grid(row = 11, column = 18)
    blank2.grid(row = 12, column = 1)

    # Creating frame to contain colour legend for element series
    legend = tk.Frame(wind1, bg = "white")
    legend.pack(side = "left")

    # Creating labels for the colour legend
    
    indent2 = tk.Label(legend, height = 1, width = 1)
    AM = tk.Label(legend, text = "Alkali Metals", height = 1, width = 17, bg = 'violet', fg = 'white')
    AEM = tk.Label(legend, text = "Alkaline Earth Metals", height = 1, width = 17, bg = 'dark green', fg = 'white')
    TM = tk.Label(legend, text = "Transition Metals", height = 1, width = 17, bg = 'salmon', fg = 'white')
    PTM = tk.Label(legend, text = "Post-Transition Metals", height = 1, width = 17, bg = 'silver', fg = 'white')
    SM = tk.Label(legend, text = "Metalloids", height = 1, width = 17, bg = 'dark khaki', fg = 'white')
    HL = tk.Label(legend, text = "Halogens", height = 1, width = 17, bg = 'green3', fg = 'white')
    NM = tk.Label(legend, text = "Other Non-Metals", height = 1, width = 17, bg = 'gold2', fg = 'white')
    NG = tk.Label(legend, text = "Noble Gases", height = 1, width = 17, bg = 'cyan3', fg = 'white')
    LA = tk.Label(legend, text = "Lanthanoids", height = 1, width = 17, bg = 'pink3', fg = 'white')
    AC = tk.Label(legend, text = "Actinoids", height = 1, width = 17, bg = 'deep pink3', fg = 'white')
    UN = tk.Label(legend, text = "Unknown", height = 1, width = 17)

    indent2.grid(row = 0, column = 0, padx = 2, pady = 2)
    AM.grid(row = 1, column = 1, padx = 2, pady = 2)
    AEM.grid(row = 2, column = 1, padx = 2, pady = 2)
    TM.grid(row = 3, column = 1, padx = 2, pady = 2)
    PTM.grid(row = 4, column = 1, padx = 2, pady = 2)
    SM.grid(row = 5, column = 1, padx = 2, pady = 2)
    HL.grid(row = 6, column = 1, padx = 2, pady = 2)
    NM.grid(row = 7, column = 1, padx = 2, pady = 2)
    NG.grid(row = 8, column = 1, padx = 2, pady = 2)
    LA.grid(row = 9, column = 1, padx = 2, pady = 2)
    AC.grid(row = 10, column = 1, padx = 2, pady = 2)
    UN.grid(row = 11, column = 1, padx = 2, pady = 2)

    # Frame to contain search option
    srch = tk.Frame(wind1, height = 4, width = 4, bg = "white")
    srch.pack(side = "bottom")

    # Creating search box, search button and label 
    sr = tk.Label(srch, text = "Type Below to Search:")
    sbox = tk.Entry(srch, bd = 4)
    sbut = tk.Button(srch, text = "Go", height = 1, width = 3, command = search)

    sr.grid(row = 1, column = 1)
    sbox.grid(row = 2, column = 1)
    sbut.grid(row = 2, column = 2)

    # To put the toplevel window in front of its parent window
    wind1.wm_transient(root)

# Function for Periodic Properties Quiz
def play():

    # Creating toplevel window under root
    wind2 = tk.Toplevel(root)
    wind2.title("Periodic Properties Quiz")
    wind2.geometry('400x350')
    wind2.iconbitmap("periodic-table.ico")
    v = tk.IntVar()

    # Connecting to mySQL database and creating cursor object
    cnx = msql.connect(host = "localhost", user = "root", password = "manager", database = "GAME")
    cursor = cnx.cursor()

    # Initialising questions, options and correct answers
    ques = ["Identify the least stable ion amongst the following.",
            "The set representing the correct order of first ionisation potential is",
            "The correct order of radii is",
            "Which of the following has the maximum number of unpaired electrons?",
            "The element with Z = 120 (not yet discovered) will be an/a"]
    o1 = ["", "Li⁺", "Be⁻", "B⁻", "C⁻"]
    o2 = ["", "K > Na > Li", "Be > Mg >Ca", "B >C > N", "Ge > Si >C"]
    o3 = ["", "N < Be < B", "F⁻ < O²⁻ < N³⁻", "Na < Li < K", "Fe³⁺ < Fe⁴⁺ < Fe²⁺"]
    o4 = ["", "Mg²⁺", "Ti³⁺", "V³⁺", "Fe²⁺"]
    o5 = ["", "transition metal", "inner-transition metal", "alkaline earth metal", "alkali metal"]
    choice = [o1, o2, o3, o4, o5]
    ans = [2, 2, 2, 4, 3]

    # Generate a list of unique random numbers 
    qn = random.sample(range(0, len(ques)), 5)

    # List to store correct answers by the user
    user_ans = []

    # Function to get user selection and check for correct answer
    def selection():
        selected = v.get()
        for i in range(len(ques)):
            if qsn["text"] == ques[i]:  
                break
        if ans[i] == selected:
            user_ans.append((i, selected))

    # Function to proceed the game forward
    def nxt():
        
        # Count the number of times the function is executed
        nxt.count += 1

        # Compute score
        global score
        score = len(set(user_ans))*10
        
        global us_name
        us_name=nmbox.get()
        
        name.destroy()
        nmbut.destroy()

        # Generate questions
        n = qn[nxt.count - 2]
        qsn['text'] = ques[n]
        qsn.pack()
        r1['text'] = choice[n][1]
        r2['text'] = choice[n][2]
        r3['text'] = choice[n][3]
        r4['text'] = choice[n][4]
        r1.pack()
        r2.pack()
        r3.pack()
        r4.pack()
        nbut.pack()
            
        if nxt.count > 5:

            # Destroy question label and radio buttons
            nmbox.destroy()
            qsn.destroy()
            r1.destroy()
            r2.destroy()
            r3.destroy()
            r4.destroy()
            nbut.destroy()
            
            # Display score
            messagebox.showinfo("Score", str(score))

            # Insert records into mySQL database
            query1 = "INSERT INTO HIGH_SCORE VALUES('{}', {})".format(us_name, score)
            cursor.execute(query1)
            cnx.commit()
            
            # Reset score after completion of game
            score = 0
            
    nxt.count = 0

    # Function to display high score
    def high_score():

        # Creating toplevel window under wind2
        hscore = tk.Toplevel(wind2)
        hscore.iconbitmap("periodic-table.ico")
        hscore['bg'] = "white"
        hscore.title("High Score")

        # Fetching records from high score table
        cursor.execute("SELECT * FROM HIGH_SCORE")
        data = cursor.fetchall()

        # Function to clear high score records
        def clr():
            cursor.execute("DELETE FROM HIGH_SCORE")
            cnx.commit()
            messagebox.showinfo("Clear", "Records cleared successfully. Please reopen the High Score window to see the changes")

        # Creating button to clear records
        cbut = tk.Button(hscore, text = "Clear Records", command = clr)
        cbut.pack()

        # Creating heading label
        h1 = tk.Label(hscore, text = "NAME\t\tSCORE")
        h1.pack()

        # Creating labels to display high score records
        for row in data:
            sc = tk.Label(hscore, text = row[0]+"\t\t"+str(row[1]))
            sc.pack()

        # To put the toplevel window in front of its parent window
        hscore.wm_transient(wind2)

    # Creating entry to accept name of the user
    name = tk.Label(wind2, text = "Enter your name below:")
    nmbox = tk.Entry(wind2, bd = 4)
    nmbut = tk.Button(wind2, text = "Go", command = nxt)
    name.pack()
    nmbox.pack()
    nmbut.pack()

    # Creating high score button
    HS = tk.Button(wind2, text = "View High Score", command = high_score)
    HS.pack(side = "bottom")

    # Creating labels and radiobuttons to display question and options
    qsn = tk.Label(wind2)
    r1 = tk.Radiobutton(wind2, variable = v, value = 1, command=selection)
    r2 = tk.Radiobutton(wind2, variable = v, value = 2, command=selection)
    r3 = tk.Radiobutton(wind2, variable = v, value = 3, command=selection)
    r4 = tk.Radiobutton(wind2, variable = v, value = 4, command=selection)
    nbut = tk.Button(wind2, text = "next", command = nxt)

    # To put the toplevel window in front of its parent window
    wind2.wm_transient(root)

# Main Window

# Creating root window
root = tk.Tk()
root.title("Introduction")
root.iconbitmap("periodic-table.ico")
root['bg'] = "white"
root.resizable(False, False)

# Creating labels to display instructions and buttons to launch applications

Instruction1 = tk.Label(root, anchor = "w", justify = "left", height = 8, width = 70,
                       text = "\t\tINSTRUCTIONS FOR INTERACTIVE PERIODIC TABLE \
                              \n\nHello Learner!! \nThe button below launches the interactive periodic table. \
                              \nClick on an element to explore its properties. \
                              \nYou can also search for an element by using the search option at the bottom of the window.")
Instruction2 = tk.Label(root, anchor = "w", justify = "left", height = 8, width = 70,
                       text = "\t\tINSTRUCTIONS FOR PERIODIC TABLE QUIZ \
                              \n\nThe button below launches the periodic properties quiz. \
                              \nPlay this quiz to assess your knowledge of the topic. \
                              \nFirst you need to enter your name and click on the go button. Then the quiz gets started.")
btn1 = tk.Button(root, text = "Explore", command = explore)
btn2=tk.Button(root, text = "Play", command = play)

Instruction1.pack()
btn1.pack()
Instruction2.pack()
btn2.pack()

# To display the window untill it is closed manually
root.mainloop()
