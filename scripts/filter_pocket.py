import sys 
sys.path.append('..')
import os
from helpers.binding_pocket import BindingPocket
from os import listdir
from os.path import isfile, join
import logging

# Initialize the logger
#Initialize logger
logging.basicConfig(filename='filter_pocket_log.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s:%(message)s')

# Check if the user provided an argument
if len(sys.argv) > 1:
    # The first command-line argument (index 0) is the script name
    # So the actual argument provided by the user is at index 1
    user_input = sys.argv[1]
    #print("You provided input:", user_input)
    mypath = user_input
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    output_path=sys.argv[2]

    pocket=sys.argv[3]

    num_atoms_before=int(sys.argv[4])
    #print(onlyfiles)
    file_number=0
    for file in onlyfiles:
        if not file.endswith(".pdb"):
            continue
        #create a binding pocket object
        binding_pocket=BindingPocket(file_path=mypath+'/'+file,output_path=f"{output_path}/"+file,pocket=pocket,b_factor_threshold=0,num_atoms_before=num_atoms_before)
        #find the binding pocket
        flag=binding_pocket.find_binding_pocket()
        file_number+=1
        if flag==-1:
            logging.error(f"Could not find the pocket {pocket} in file {file} - {file_number}/{len(onlyfiles)}")
        elif flag==1:
            logging.info(f"Processed file {file_number}/{len(onlyfiles)}")

    #create a binding pocket object
    # binding_pocket=BindingPocket(file_path="data\AF-A0A087XJA9-F1-model_v4.pdb",output_path="data\\test_class.pdb",pocket="KAIEP",b_factor_threshold=50,num_atoms_before=7)
    # #find the binding pocket
    # binding_pocket.find_binding_pocket()
else:
    logging.error("Please provide the data path")
    sys.exit(1)

