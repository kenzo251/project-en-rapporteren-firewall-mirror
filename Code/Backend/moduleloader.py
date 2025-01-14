#!/usr/bin/python
#example code
import os
import importlib

# Define the path to the modules folder
module_folder = "Backend/modules"

def getModules(moduleset,ignored=[]):
	# Get a list of all Python files in the modules folder
	module_filenames = [f for f in os.listdir(f"{module_folder}/{moduleset}") if os.path.isdir(f"{module_folder}/{moduleset}/{f}") and f!="__pycache__"]
	
	# Import all modules in the modules folder and store them in a dictionary
	modules = {}
	for module_name in module_filenames:
		try:
			module = importlib.import_module(f"{module_folder.replace('/','.')}.{moduleset}.{module_name}",package=None)
			modules[module_name] = (module, (module_name in ignored))
		except Exception as ex:
			print(f"error loading module {module_name}.{moduleset}")
			print(ex)
	return modules
