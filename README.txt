Example of ensemble simulation for 

STEP 1: create a CSV file with uncertain input parameters

> python create_ensemble_Cartesian.py

The number of samples, the uncertain parameters and their ranges are defined in the create_ensemble_Cartesian.py file
Each parameters has a keyword, for example "var1"

STEP 2: create folders

> python create_inputfiles.py

This script create the folders by making a copy of the folder "templatedir". The values of the uncertain parameters
in the input file must be replaced by the string "ENSAMBLE_xyz", where "xyz" is the keyword assigned in create_ensamble.py. For example, if "var1" is defined as unknown in create_ensemble_Cartesian.py, we must have in an input file "ENSEMBLE_var1".   

STEP 3: launch the simulations

> python launch_jobs.py

This script launch all the simulations. The maximum number of concurrent runs can be prescribed in the file. This script launch a batch script "run.sh" present in each folder "ensemble.xxxxx".
 

