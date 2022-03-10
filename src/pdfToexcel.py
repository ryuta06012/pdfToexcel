# -*- coding: utf-8 -*-
from pprint import pprint
import pandas as pd
import Convert
import InformationInput

convert = Convert.Convert('../sample2.pdf')
convert.tableExtraction()
convert.convertExcel()

info = InformationInput.InformationInput(convert.getExpath())
info.iterCols()
info.addDataByColumn()
info.createExcel()

