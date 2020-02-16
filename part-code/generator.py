import os
import pickle
import sys
import os
from subprocess import call
import PIL.Image
import PIL.ImageTk

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
details_list=[]


def file_save():
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]
    ROOM_NO_PRO = details_list[3]
    PRICE_PRO = details_list[4]
    f = open("hotel.dat", "ab")
    a=save(NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO)
    pickle.dump(a,f,protocol=2)
    f.close()
    listq=[str(NAME_PRO),str(ADDRESS_PRO),str(MOBILE_NO_PRO),str(ROOM_NO_PRO),str(PRICE_PRO)]
    myVars = {'A':NAME_PRO,"B":ADDRESS_PRO,"C":MOBILE_NO_PRO,"D":ROOM_NO_PRO,"E":PRICE_PRO }

    fo=open("recipt.txt","w+")
    for h in range(0,5):
        fo.write(listq[h]+"\r\n")
    fo.close()
    call(["python", "recipt.py"])
    restart_program()


u = list()
partGroup = ["Mild Steel",
"Stainless Steel",
"Galvanized Iron",
"Aluminium",
"Plywood",
"Timber",
"Cloth Items",
"Paints",
"Cushions",
"Glass",
"Auto Electricals",
"Rubber Goods",
"LaminatedSheets",
"Pipes",
"DoorMaterials",
"PVC Items",
"FRPMouldedItems",
"ChemicalsAcids",
"Insulation",
"LubricantsAdhesives"
]


#Dictionary
partGroup_dict = {"Mild Steel" : "MS", "Stainless Steel" : "SS" , "Galvanized Iron" : "GI", "Aluminium" : "AL", "Plywood" : "PW", "Timber" : "TI", "Cloth Items" : "CL", "Paints" : "PA", "Cushions" : "CU", "Glass" : "GL", "Auto Electricals" : "AE", "Rubber Goods" : "RG", "LaminatedSheets" : "LS", "Pipes" : "PI", "Fasteners" : "FA", "DoorMaterials" : "DM", "PVC Items" : "PV", "FRPMouldedItems" : "FR", "ChemicalsAcids" : "CH", "Insulation" : "IN", "LubricantsAdhesives" : "LS"}

MildSteel1 = {"Angle"   : "1", "Channel" : "2", "Flat" : "3", "Sheet" : "4", "Plate" : "5", "Rod" : "6", "Joist" : "7", "Hat section" : "8", "Channel section" : "9"}
MildSteel2 = {"Hot Rolled" : "1", "Cold Rolled" : "2", "Plain" : "3", "Round" : "4", "Square" : "5", "Chequered" : "6"}
MildSteel3 = {"Polished" : "1", "Non-polish" : "2"}

StainlessSteel1 = {"Sheet" : "1", "Coil" : "2"}

GalvanizedIron1 = {"Sheet" : "1", "Wire" : "2", "Pipe"  : "3" , "Fittings" : "4"}  	   
GalvanizedIron2 = {"Plain" : "1", "Corrugated" : "2", "PVC Coated" : "3", "Reducer" : "4", "Elbow" : "5", "Tee" : "6", "Cross" : "7", "Hex Nipple" : "8", "Dummy Plug" : "9", "Union" : "10", "Coupling" : "11", "Clamp" : "12", "Pipe" : "13"}  	

Aluminium1 = {"Extrusions" : "1", "Sheet" : "2", "Plate": "3", "Coil" : "4"}
Aluminium2 = {"Plain" : "1", "Chequered" : "2"}
Aluminium3 = {"Polished" : "1", "Non-Polish" : "2"}

Plywood1 = {"Plain" : "1", "Chequered" : "2"}
Plywood2 = {"B. W. R." : "1", "W. W. R." : "2", "O. S. T." : "3", "Commercial Marine" : "4"}

Timber1 = {"Ayini" : "1", "Karangi" : "2", "Silver Oak" : "3", "Rubber": "4"}
Timber2 = {"Reaper" : "1", "Curves" : "2", "Planks" : "3"}

ClothItems1 = {"Leather Cloth" : "1", "Vinyl Mats" : "2", "Carpets" : "3", "Other Fabricitems" : "4"}
ClothItems2 =  {"Manufacturer" : "1"}
ClothItems3 = {"Shade" : "1", "Colour" : "2"}

Paints1 = {"Manufacturer" : "1"}
Paints2 = {"Primers" : "1", "Base Paints" : "2", "Thinner" : "3", "Enamel" : "4", "Lacquer" : "5", "Poly Urethane" : "6", "Chlorinated Rubber" : "7", "Filler materials" : "8", "Other Addictive" : "9"}
Paints3 = {"Colour" : "1"}

Cushions1 = {"Rubber" : "1", "Foam" : "2", "Coir" : "3"}
Cushions2 = {"Flat" : "1", "Taper" : "2", "Strip" : "3"}

Glass1 = {"Toughened" : "1", "Laminated" : "2"}
Glass2 = {"Flat" : "1", "Curved" : "2"}
Glass3 ={"Clear" : "1", "Smoke" : "2"}

AutoElectricals1 = {"Wires" : "1", "Cables" : "2", "Chokes" : "3", "Stater" : "4", "Fuse Units" : "5", "Bulbs/Lamps" : "6"}
AutoElectricals2 = {"Manufacturer" : "1"}

RubberGoods1 = {"Extrusions" : "1", "Sheets" : "2", "Tubes": "3"}
RubberGoods2 = {"Sire" : "1", "EPDM" : "2"}

LaminatedSheets1 = {"Shade" : "1"}
LaminatedSheets2 = {"Types of finish" : "1"}

Pipes1 = {"M. S." : "1", "ERW" : "2", "Stainless steel" : "3"}
Pipes2 = {"Square Round" : "1"}

DoorMaterials1 = {"Locks" : "1", "Handles" : "2", "Hinges" : "3", "Tower Bolts" : "4", "padlock Items" : "5", "Door Assys" : "6", "Door closer" : "7", "Door padding Item" : "8", "Window material" : "9"}

PVCItems1 = {"Sleeves" : "1", "Inserts" : "2", "Bushes" : "3", "Clips" : "4", "Grommets" : "5", "Packing Items" : "6", "Pipe Fittings" : "7"}
PVCItems2 = { "Colour" : "1", "Flat base" : "2", "Taper base" : "3",  "Reducer" : "4", "Elbow" : "5", "Tee" : "6", "Cross" : "7", "Hex Nipple" : "8", "Dummy Plug" : "9", "Union" : "10",  "Coupling" : "11", "Clamp" : "12", "Pipe" : "13"}

FRPMouldedItems1 = {"Resin" : "1", "Mat" : "2", "Accelerator" : "3", "Catalyst" : "4"}

ChemicalsAcids1 = {"Chemicals" : "1", "Acids" : "2"}

Insulation1 = {"Puf" : "1", "Glass Wool" : "2", "Thermocole" : "3"}

LubricantsAdhesives1 = {"Pastes" : "1","Sealants" : "2", "Oils" : "3", "Grease" : "4"}

#Lists
mildSteel_1 = ["Angle", "Channel", "Flat", "Sheet", "Plate", "Rod", "Joist", "Hat section", "Channel section"]
mildSteel_2 = ["Hot Rolled", "Cold Rolled", "Plain", "Round", "Square", "Chequered"]
mildSteel_3 = ["Polished", "Non- polish"]
StainlessSteel_1 = ["Sheet", "Coil"]
galvanizedIron_1 = ["Sheet", "Wire", "Pipe", "Fittings"]
galvanizedIron_2 = ["Plain", "Corrugated", "PVC Coated", "Reducer", "Elbow", "Tee", "Cross", "Hex Nipple", "Dummy Plug", "Union", "Coupling", "Clamp", "Pipe"]
Aluminium_1 = ["Extrusions", "Sheet", "Plate", "Coil"]
Aluminium_2 = ["Plain", "Chequered"]
Aluminium_3 =["Polished", "Non-Polish"]
Plywood_1 = ["Plain", "Chequered"]
Plywood_2 = ["B. W. R.", "W. W. R.", "O. S. T", "Commercial Marine"]
Timber_1 = ["Ayini", "Karangi", "Silver Oak", "Rubber"]
Timber_2 = ["Reaper", "Curves", "Planks"]
ClothItems_1 = ["Leather Cloth", "Vinyl Mats", "Carpets", "Other Fabric items"]
ClothItems_2 = ["Manufacturer"]
ClothItems_3 = ["Shade", "Colour"] 
Paints_1 = ["Manufacturer"]
Paints_2 = ["Primers", "Base Paints", "Thinner", "Enamel", "Lacquer", "Poly Urethane", "Chlorinated Rubber", "Filler materials", "Other Addictive"]
Paints_3 = ["Colour"]
Cushions_1 = ["Rubber", "Foam", "Coir"]
Cushions_2 = ["Flat", "Taper", "Strip"]
Glass_1 = ["Toughened", "Laminated"]
Glass_2 = ["Flat", "Curved"]
Glass_3 = ["Clear", "Smoke"]
AutoElectricals_1 = ["Wires", "Cables", "Chokes", "Stater", "Fuse Units", "Bulbs/Lamps"]
AutoElectricals_2 = ["Manufacturer"]
AutoElectricals_3 = ["Clear"]
RubberGoods_1 = ["Extrusions", "Sheets", "Tubes"]
RubberGoods_2 = ["Sire", "EPDM"]

LaminatedSheets_1 =["Shade"]
LaminatedSheets_2 = ["Types of finish"]
Pipes_1 = ["M. S.", "ERW", "Stainless steel"]
Pipes_2 = ["Square Round"]
DoorMaterials = ["Locks", "Handles", "Hinges", "Tower Bolts", "Padlock Items", "Door Assys", "Door closer", "Door padding Item", "Window material"]
PVCItems_1 = ["Sleeves", "Inserts", "Bushes", "Clips", "Grommets", "Packing Items", "Pipe Fittings"]
PVCItems_2 = ["Colour", "Flat base", "Taper base", "Reducer", "Elbow", "Tee", "Cross", "Hex Nipple", "Dummy Plug", "Union", "Coupling", "Clamp", "Pipe"]
FRPMouldedItems_1 = ["Resin", "Mat", "Accelerator", "Catalyst"]
ChemicalsAcids_1 = ["Chemicals", "Acids"]
Insulation_1 = ["Puf", "Glass Wool", "Thermocol"]
LubricantsAdhesives_1 = ["Pastes", "Sealants", "Oils", "Grease"]

def restart_program():
    """Restarts the current program.

    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function.
    """
    python = sys.executable
    os.execl(python, python, * sys.argv)

class save:
    def __init__(self,NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,ROOM_NO_PRO,PRICE_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.room_no=ROOM_NO_PRO
        self.price=PRICE_PRO

class HOTEL_MANGMENT_checkin:
       
    def __init__(self):

        def image_show():
            part_2 = self.Entry1.get()
            print(part_2)
            if part_2 == StainlessSteel_1[0]:
                fp = open("images.png","rb")
                img = PIL.Image.open(fp)
                img.show()
                           
        def dynamic_change():
            
            part = groupOne.get()
            if part == "":
                messagebox.showerror("Error", "Please Enter A Value!")

            elif part == partGroup[0]:
                
                groupTwo = StringVar()
                self.Entry2 = Combobox(self.Frame2,values=mildSteel_2)
                self.mobile=StringVar()
                self.Entry2.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
                self.Entry2.configure(background="white")
                self.Entry2.configure(textvariable=groupTwo)

                groupThree = StringVar()
                self.Entry3 = Combobox(self.Frame2,values=mildSteel_3)
                self.name=StringVar()
                self.Entry3.place(relx=0.47, rely=0.44,height=34, relwidth=0.43)
                self.Entry3.configure(background="white")
                self.Entry3.configure(textvariable=groupThree)

                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=mildSteel_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")
                self.Entry1.configure(textvariable=groupFour)
           
            elif part == partGroup[1]:

                groupTwo = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=StainlessSteel_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")                
                self.Entry1.configure(textvariable=groupTwo)
           
            elif part == partGroup[2]:
                
                groupTwo = StringVar()
                self.Entry2 = Combobox(self.Frame2,values=galvanizedIron_2)
                self.mobile=StringVar()
                self.Entry2.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
                self.Entry2.configure(background="white")                
                self.Entry2.configure(textvariable=groupTwo)

                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=galvanizedIron_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")               
                self.Entry1.configure(textvariable=groupFour)

            elif part == partGroup[3]:
                
                groupTwo = StringVar()
                self.Entry2 = Combobox(self.Frame2,values=Aluminium_2)
                self.mobile=StringVar()
                self.Entry2.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
                self.Entry2.configure(background="white")                
                self.Entry2.configure(textvariable=groupTwo)

                groupThree = StringVar()
                self.Entry3 = Combobox(self.Frame2,values=Aluminium_3)
                self.name=StringVar()
                self.Entry3.place(relx=0.47, rely=0.44,height=34, relwidth=0.43)
                self.Entry3.configure(background="white")               
                self.Entry3.configure(textvariable=groupThree)

                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=Aluminium_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")                
                self.Entry1.configure(textvariable=groupFour)
            
            elif part == partGroup[4]:
                
                groupTwo = StringVar()
                self.Entry2 = Combobox(self.Frame2,values=Plywood_2)
                self.mobile=StringVar()
                self.Entry2.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
                self.Entry2.configure(background="white")                
                self.Entry2.configure(textvariable=groupTwo)

                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=Plywood_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")                
                self.Entry1.configure(textvariable=groupFour)
            
            elif part == partGroup[5]:
                
                groupTwo = StringVar()
                self.Entry2 = Combobox(self.Frame2,values=Timber_2)
                self.mobile=StringVar()
                self.Entry2.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
                self.Entry2.configure(background="white")                
                self.Entry2.configure(textvariable=groupTwo)

                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=Timber_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")               
                self.Entry1.configure(textvariable=groupFour)
            
            elif part == partGroup[6]:
                
                groupTwo = StringVar()
                self.Entry2 = Combobox(self.Frame2,values=ClothItems_2)
                self.mobile=StringVar()
                self.Entry2.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
                self.Entry2.configure(background="white")               
                self.Entry2.configure(textvariable=groupTwo)

                groupThree = StringVar()
                self.Entry3 = Combobox(self.Frame2,values=ClothItems_3)
                self.name=StringVar()
                self.Entry3.place(relx=0.47, rely=0.44,height=34, relwidth=0.43)
                self.Entry3.configure(background="white")                
                self.Entry3.configure(textvariable=groupThree)

                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=ClothItems_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")                
                self.Entry1.configure(textvariable=groupFour)
            
            elif part == partGroup[7]:
                
                groupTwo = StringVar()
                self.Entry2 = Combobox(self.Frame2,values=Paints_2)
                self.mobile=StringVar()
                self.Entry2.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
                self.Entry2.configure(background="white")                
                self.Entry2.configure(textvariable=groupTwo)

                groupThree = StringVar()
                self.Entry3 = Combobox(self.Frame2,values=Paints_3)
                self.name=StringVar()
                self.Entry3.place(relx=0.47, rely=0.44,height=34, relwidth=0.43)
                self.Entry3.configure(background="white")               
                self.Entry3.configure(textvariable=groupThree)

                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=Paints_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")                
                self.Entry1.configure(textvariable=groupFour)
            
            elif part == partGroup[8]:
                
                groupTwo = StringVar()
                self.Entry2 = Combobox(self.Frame2,values=Cushions_2)
                self.mobile=StringVar()
                self.Entry2.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
                self.Entry2.configure(background="white")               
                self.Entry2.configure(textvariable=groupTwo)

                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=Cushions_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")                
                self.Entry1.configure(textvariable=groupFour)
            
            elif part == partGroup[9]:
                groupTwo = StringVar()
                self.Entry2 = Combobox(self.Frame2,values=Glass_2)
                self.mobile=StringVar()
                self.Entry2.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
                self.Entry2.configure(background="white")               
                self.Entry2.configure(textvariable=groupTwo)

                groupThree = StringVar()
                self.Entry3 = Combobox(self.Frame2,values=Glass_3)
                self.name=StringVar()
                self.Entry3.place(relx=0.47, rely=0.44,height=34, relwidth=0.43)
                self.Entry3.configure(background="white")              
                self.Entry3.configure(textvariable=groupThree)

                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=Glass_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")                
                self.Entry1.configure(textvariable=groupFour)

            elif part == partGroup[10]:
                
                groupTwo = StringVar()
                self.Entry2 = Combobox(self.Frame2,values=AutoElectricals_2)
                self.mobile=StringVar()
                self.Entry2.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
                self.Entry2.configure(background="white")                
                self.Entry2.configure(textvariable=groupTwo)

                groupThree = StringVar()
                self.Entry3 = Combobox(self.Frame2,values=AutoElectricals_3)
                self.name=StringVar()
                self.Entry3.place(relx=0.47, rely=0.44,height=34, relwidth=0.43)
                self.Entry3.configure(background="white")               
                self.Entry3.configure(textvariable=groupThree)

                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=AutoElectricals_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")              
                self.Entry1.configure(textvariable=groupFour)

            elif part == partGroup[11]:
                
                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=RubberGoods_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")               
                self.Entry1.configure(textvariable=groupFour)
                
                groupTwo = StringVar()
                self.Entry2 = Combobox(self.Frame2,values=RubberGoods_2)
                self.mobile=StringVar()
                self.Entry2.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
                self.Entry2.configure(background="white")              
                self.Entry2.configure(textvariable=groupTwo)

            elif part == partGroup[12]:
                
                groupTwo = StringVar()
                self.Entry2 = Combobox(self.Frame2,values=LaminatedSheets_2)
                self.mobile=StringVar()
                self.Entry2.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
                self.Entry2.configure(background="white")                
                self.Entry2.configure(textvariable=groupTwo)

                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=LaminatedSheets_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")              
                self.Entry1.configure(textvariable=groupFour)
            
            elif part == partGroup[13]:
                
                groupTwo = StringVar()
                self.Entry2 = Combobox(self.Frame2,values=Pipes_2)
                self.mobile=StringVar()
                self.Entry2.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
                self.Entry2.configure(background="white")               
                self.Entry2.configure(textvariable=groupTwo)

                self.Entry1 = Combobox(self.Frame2,values=Pipes_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")            
                self.Entry1.configure(textvariable=groupFour)
            
            elif part == partGroup[14]:
  
                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=DoorMaterials)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")               
                self.Entry1.configure(textvariable=groupFour)
            
            elif part == partGroup[15]:
                
                groupTwo = StringVar()
                self.Entry2 = Combobox(self.Frame2,values=PVCItems_2)
                self.mobile=StringVar()
                self.Entry2.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
                self.Entry2.configure(background="white")               
                self.Entry2.configure(textvariable=groupTwo)

                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=PVCItems_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")                
                self.Entry1.configure(textvariable=groupFour)
            
            elif part == partGroup[16]:
                
                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=FRPMouldedItems_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")               
                self.Entry1.configure(textvariable=groupFour)

            elif part == partGroup[17]:
 
                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=ChemicalsAcids_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")
                self.Entry1.configure(textvariable=groupFour)
            
            elif part == partGroup[18]:
 
                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=Insulation_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")                
                self.Entry1.configure(textvariable=groupFour)
            
            elif part == partGroup[19]:
 
                groupFour = StringVar()
                self.Entry1 = Combobox(self.Frame2,values=LubricantsAdhesives_1)
                self.mobile=StringVar()
                self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
                self.Entry1.configure(background="white")              
                self.Entry1.configure(textvariable=groupFour)
      
        def submit_clicked():
            
            part_1 = groupOne.get()
            global part_2
            part_2 = self.Entry1.get()
            part_3 = self.Entry2.get()
            part_4 = self.Entry3.get()
            part_5 = self.Entry5.get()
            part_6 = self.Entry6.get()
            part_7 = self.Entry7.get()
            
            if part_1 == partGroup[0]:
                
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}{}{}".format(partGroup_dict[part_1],MildSteel1[part_2],MildSteel2[part_3],MildSteel3[part_4],part_5,part_6,part_7))
                self.Message3.configure(width=1000)
            elif part_1 == partGroup[1]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}".format(partGroup_dict[part_1],StainlessSteel1[part_2],part_5,part_6,part_7))
                self.Message3.configure(width=1000)

            elif part_1 == partGroup[2]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}{}".format(partGroup_dict[part_1],GalvanizedIron1[part_2],GalvanizedIron2[part_3],part_5,part_6,part_7))
                self.Message3.configure(width=1000)
            elif part_1 == partGroup[3]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}{}{}".format(partGroup_dict[part_1],Aluminium1[part_2],Aluminium2[part_3],Aluminium3[part_4],part_5,part_6,part_7))
                self.Message3.configure(width=1000)  
                 
            elif part_1 == partGroup[4]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}{}".format(partGroup_dict[part_1],Plywood1[part_2],Plywood2[part_3],part_5,part_6,part_7))
                self.Message3.configure(width=1000)

            elif part_1 == partGroup[5]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}{}".format(partGroup_dict[part_1],Timber1[part_2],Timber2[part_3],part_5,part_6,part_7))
                self.Message3.configure(width=1000) 
            
            elif part_1 == partGroup[6]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}{}{}".format(partGroup_dict[part_1],ClothItems1[part_2],ClothItems2[part_3],ClothItems3[part_4],part_5,part_6,part_7))
                self.Message3.configure(width=1000)
            
            elif part_1 == partGroup[7]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}{}{}".format(partGroup_dict[part_1],Paints1[part_2],Paints2[part_3],Paints3[part_4],part_5,part_6,part_7))
                self.Message3.configure(width=1000)

            elif part_1 == partGroup[8]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}{}".format(partGroup_dict[part_1],Cushions1[part_2],Cushions2[part_3],part_5,part_6,part_7))
                self.Message3.configure(width=1000)

            elif part_1 == partGroup[9]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}{}{}".format(partGroup_dict[part_1],Glass1[part_2],Glass2[part_3],Glass3[part_4],part_5,part_6,part_7))
                self.Message3.configure(width=1000)  

            elif part_1 == partGroup[10]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}{}".format(partGroup_dict[part_1],AutoElectricals1[part_2],AutoElectricals2[part_3],part_5,part_6,part_7))
                self.Message3.configure(width=1000)          
            
            elif part_1 == partGroup[11]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}{}".format(partGroup_dict[part_1],RubberGoods1[part_2],RubberGoods2[part_3],part_5,part_6,part_7))
                self.Message3.configure(width=1000)

            elif part_1 == partGroup[12]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}{}".format(partGroup_dict[part_1],LaminatedSheets1[part_2],LaminatedSheets2[part_3],part_5,part_6,part_7))
                self.Message3.configure(width=1000)

            elif part_1 == partGroup[13]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}{}".format(partGroup_dict[part_1],Pipes1[part_2],Pipes2[part_3],part_5,part_6,part_7))
                self.Message3.configure(width=1000) 

            elif part_1 == partGroup[14]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}".format(partGroup_dict[part_1],DoorMaterials1[part_2],part_5,part_6,part_7))
                self.Message3.configure(width=1000) 

            elif part_1 == partGroup[15]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}{}".format(partGroup_dict[part_1],PVCItems1[part_2],PVCItems2[part_3],part_5,part_6,part_7))
                self.Message3.configure(width=1000) 

            elif part_1 == partGroup[16]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}".format(partGroup_dict[part_1],FRPMouldedItems1[part_2],part_5,part_6,part_7))
                self.Message3.configure(width=1000) 

            elif part_1 == partGroup[17]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}".format(partGroup_dict[part_1],ChemicalsAcids1[part_2],part_5,part_6,part_7))
                self.Message3.configure(width=1000)                
                
            elif part_1 == partGroup[18]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}".format(partGroup_dict[part_1],Insulation1[part_2],part_5,part_6,part_7))
                self.Message3.configure(width=1000)

            elif part_1 == partGroup[19]:
                self.Message3 = Message(self.Frame2)
                self.Message3.place(relx=0.15, rely=0.75, relheight=0.20, relwidth=0.40)
                self.Message3.configure(background="dark slate gray")
                self.Message3.configure(font=font11)
                self.Message3.configure(foreground="gray10")
                self.Message3.configure(highlightbackground="#ffffff")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text="{}{}{}{}{}".format(partGroup_dict[part_1],LubricantsAdhesives1[part_2],part_5,part_6,part_7))
                self.Message3.configure(width=1000)    
           
        def bill(self):

            
            G = []
            f2 = open("hotel.dat", "rb")
            try:
                while True:
                    s = pickle.load(f2)

                    k = s.room_no
                    G.append(k)
                    continue

            except EOFError:
                pass

            for r in a:
                if r not in G:
                    self.room = r
                    break
                else:
                    continue
            self.room = r
            f2.close()

            file_save()

        root = Tk()


        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Times New Roman} -size 28 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 18 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI} -size 16 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family {Segoe UI} -size 19 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1069x742")
        root.title("PART CODE GENERATION")
        root.configure(background="dark slate gray")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")

        def enter(event):
            self.Button4.configure(foreground="red")

        def leave(event):
            self.Button4.configure(foreground="#000000")    
       
        self.Text1 = Text(root)
        self.Text1.place(relx=0.03, rely=0.65, relheight=0.29, relwidth=0.93)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#ffffff")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#e6e6e6")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=994)
        self.Text1.configure(wrap=WORD)

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.93)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="dark slate gray")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=995)

        
        self.Message3 = Message(self.Frame1)
        self.Message3.place(relx=0.34, rely=0.11, relheight=0.79, relwidth=0.35)
        self.Message3.configure(background="dark slate gray")
        self.Message3.configure(font=font11)
        self.Message3.configure(foreground="gray10")
        self.Message3.configure(highlightbackground="#ffffff")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text=''' THE GENERATOR''')
        self.Message3.configure(width=347)

        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)



        self.Frame2 = Frame(root)
        self.Frame2.place(relx=0.03, rely=0.18, relheight=0.46, relwidth=0.93)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="dark slate gray")
        self.Frame2.configure(highlightbackground="#ffffff")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=995)
   
        empty=[]
        groupOne = StringVar()
        self.Entry0 = Combobox(self.Frame2,values=partGroup)
        self.name=StringVar()
        self.Entry0.place(relx=0.47, rely=0.05,height=34, relwidth=0.43)
        self.Entry0.configure(background="white smoke")
        
        self.Entry0.configure(textvariable=groupOne)

        groupTwo = StringVar()
        self.Entry2 = Combobox(self.Frame2,values=empty)
        self.mobile=StringVar()
        self.Entry2.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)
        self.Entry2.configure(background="white")
                
        self.Entry2.configure(textvariable=groupTwo)

        groupThree = StringVar()
        self.Entry3 = Combobox(self.Frame2,values=empty)
        self.name=StringVar()
        self.Entry3.place(relx=0.47, rely=0.44,height=34, relwidth=0.43)
        self.Entry3.configure(background="white")
                
        self.Entry3.configure(textvariable=groupThree)

        groupFour = StringVar()
        self.Entry1 = Combobox(self.Frame2,values=empty)
        self.mobile=StringVar()
        self.Entry1.place(relx=0.47, rely=0.19,height=34, relwidth=0.43)
        self.Entry1.configure(background="white")                
        self.Entry1.configure(textvariable=groupFour)


        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.91, rely=0.05, height=33, width=43)
        self.Button2.configure(activebackground="#ffffff")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="white smoke")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#ffffff")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''OK''')
        self.Button2.configure(command=dynamic_change)

        groupTwo = StringVar()
        self.Entry5 = Entry(self.Frame2)
        self.mobile=StringVar()
        self.Entry5.place(relx=0.47, rely=0.60,height=34, relwidth=0.10)
        self.Entry5.configure(background="white smoke")
        self.Entry5.configure(textvariable=groupTwo)
 
        groupTwo = StringVar()
        self.Entry6 = Entry(self.Frame2)
        self.mobile=StringVar()
        self.Entry6.place(relx=0.57, rely=0.60,height=34, relwidth=0.10)
        self.Entry6.configure(background="white smoke") 
        self.Entry6.configure(textvariable=groupTwo)    

        groupTwo = StringVar()
        self.Entry7 = Entry(self.Frame2)
        self.mobile=StringVar()
        self.Entry7.place(relx=0.67, rely=0.60,height=34, relwidth=0.10)
        self.Entry7.configure(background="white smoke")
        self.Entry7.configure(textvariable=groupTwo)

        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0.05, rely=0.03, height=47, width=289)
        self.Label3.configure(activebackground="#ffffff")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="dark slate gray")
        self.Label3.configure(disabledforeground="#bfbfbf")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#ffffff")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''PART GROUP''')

        self.Label5 = Label(self.Frame2)
        self.Label5.place(relx=0.05, rely=0.16, height=47, width=334)
        self.Label5.configure(activebackground="#ffffff")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="dark slate gray")
        self.Label5.configure(disabledforeground="#bfbfbf")
        self.Label5.configure(font=font12)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#ffffff")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''SUB GROUP 1''')

        self.Label4 = Label(self.Frame2)
        self.Label4.place(relx=0.05, rely=0.29, height=47, width=329)
        self.Label4.configure(activebackground="#ffffff")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="dark slate gray")
        self.Label4.configure(disabledforeground="#bfbfbf")
        self.Label4.configure(font=font12)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#ffffff")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''SUB GROUP 2''')

        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.05, rely=0.43, height=47, width=334)
        self.Label1.configure(background="dark slate gray")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''SUB GROUP 3''')

        self.Label5 = Label(self.Frame2)
        self.Label5.place(relx=0.05, rely=0.58, height=47, width=334)
        self.Label5.configure(activebackground="#ffffff")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="dark slate gray")
        self.Label5.configure(disabledforeground="#bfbfbf")
        self.Label5.configure(font=font12)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#ffffff")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''DIMENSIONS (LxBxH)''')

        self.Message5 = Message(self.Frame2)
        self.Message5.place(relx=0.42, rely=0.58, relheight=0.12, relwidth=0.03)
        self.Message5.configure(background="dark slate gray")
        self.Message5.configure(font=font13)
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#ffffff")
        self.Message5.configure(highlightcolor="black")
        self.Message5.configure(text=''':''')
        self.Message5.configure(width=26)

        self.Message4 = Message(self.Frame2)
        self.Message4.place(relx=0.41, rely=0.04, relheight=0.1, relwidth=0.05)
        self.Message4.configure(background="dark slate gray")
        self.Message4.configure(font=font13)
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#ffffff")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(text=''':''')
        self.Message4.configure(width=46)

        self.Message5 = Message(self.Frame2)
        self.Message5.place(relx=0.42, rely=0.17, relheight=0.12, relwidth=0.03)
        self.Message5.configure(background="dark slate gray")
        self.Message5.configure(font=font13)
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#ffffff")
        self.Message5.configure(highlightcolor="black")
        self.Message5.configure(text=''':''')
        self.Message5.configure(width=26)

        self.Message6 = Message(self.Frame2)
        self.Message6.place(relx=0.415, rely=0.3, relheight=0.09, relwidth=0.04)
        self.Message6.configure(background="dark slate gray")
        self.Message6.configure(font=font13)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#ffffff")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text=''':''')
        self.Message6.configure(width=36)

        self.Button4 = Button(self.Frame2)
        self.Button4.place(relx=0.76, rely=0.72, height=83, width=156)
        self.Button4.configure(activebackground="#ffffff")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="white smoke")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font16)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#ffffff")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.bind("<Enter>", enter)
        self.Button4.bind("<Leave>", leave)
        self.Button4.configure(text='''SUBMIT''')
        self.Button4.configure(command=submit_clicked)

        self.Button4 = Button(self.Frame2)
        self.Button4.place(relx=0.60, rely=0.72, height=83, width=156)
        self.Button4.configure(activebackground="#ffffff")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="white smoke")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font16)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#ffffff")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.bind("<Enter>", enter)
        self.Button4.bind("<Leave>", leave)
        self.Button4.configure(text='''GET INFO''')
        self.Button4.configure(command=image_show)

        self.Message8 = Message(self.Frame2)
        self.Message8.place(relx=0.42, rely=0.41, relheight=0.11, relwidth=0.03)
        self.Message8.configure(background="dark slate gray")
        self.Message8.configure(font=font13)
        self.Message8.configure(foreground="#000000")
        self.Message8.configure(highlightbackground="#ffffff")
        self.Message8.configure(highlightcolor="black")
        self.Message8.configure(text=''':''')
        self.Message8.configure(width=26)



        root.mainloop()


if __name__ == '__main__':
    hotel=HOTEL_MANGMENT_checkin()
