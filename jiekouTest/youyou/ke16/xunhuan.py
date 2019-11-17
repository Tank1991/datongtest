from ke16.readexcel import ExcelUtil

sheets =["Sheet1","Sheet2","Sheet3"]

for i in sheets:
    d = ExcelUtil("data.xlsx", sheetName=i)
    data1 = d.dict_data()
    print("循环读取的sheet名称：%s"%i)
    print(data1)
