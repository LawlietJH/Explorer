

# v1.2.1

from tkinter import filedialog, Tk
import os


Tk().withdraw()


class Explorer():
	
	def getFileName(title='', file_types=[ 
				['Archivos de Texto','.txt'], ['Todos los Archivos','.*']
			], init_dir=os.getcwd()):
		
		f_name = filedialog.askopenfile(title = title,
										initialdir = init_dir,
										filetypes = file_types)
		if not f_name == None:
			return f_name.name
	
	
	def getFolderName(title='', init_dir=os.getcwd()):
		
		d_path = filedialog.askdirectory(title = title, initialdir = init_dir)
		return d_path
	
	
	def getFileNameSave(file_types=[
					['Archivos de Texto','.txt'], ['Todos los Archivos','.*']
				], title='', init_dir=os.getcwd()):
		
		f_name = filedialog.asksaveasfilename(title = title,
											  initialdir = init_dir,
											  filetypes = file_types)
		if not f_name == None:
			return f_name


