# -*- coding: utf-8 -*-
import tabula

class Convert():
	def __init__(self, path : str):
		self.pdpath = path
	def tableExtraction(self):
		self.dfs = tabula.read_pdf(self.pdpath, lattice=False, pages = '1')
	def convertExcel(self):
		i = 0
		for df in self.dfs:
			df.to_excel("../xlsx/PDFtable"+str(i) +".xlsx",index=None) # Excel
			self.expath = "../xlsx/PDFtable"+str(i) +".xlsx"
			i+=1
	def getExpath(self):
		return self.expath