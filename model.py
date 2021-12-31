import os


class Model:
    def __init__(self, projectname, path, columns, model):
        self.projectname = str(projectname)
        self.model = str(model)
        self.columns = columns
        self.path = path
        self.ModelPath = f"{self.path}/{self.projectname}/_models"

        if not os.path.exists(self.ModelPath):
            os.makedirs(self.ModelPath)

        self.DataType()

    def DataType(self):
        for column in self.columns:
            if str(column[1]).startswith("b'decimal"):
                column[1] = "number"
            elif str(column[1]).startswith("b'tinyint"):
                column[1] = "boolean"
            else:
                column[1] = "string"
        if not self.model.startswith("Vw_"):
            self.CreateModel()

    def CreateModel(self):
        filedata = f"export class {self.model}" + "{\n"
        fileDataList = []

        for column in self.columns:
            feild = f"{str(column[0]).title()} !: {column[1]}; \n"
            fileDataList.append(feild)

            if str(column[0]).endswith("id"):
                column[0] = str(column[0]).replace("id", "")
                if not column[0] == "":
                    fileDataList.append(f"{str(column[0]).title()} !: {column[1]}; \n")

        fileDataList.append("}\n")
        file = open(f"{self.ModelPath}/{self.model}.model.ts", "w")
        file.writelines(filedata)
        file.writelines(fileDataList)
        file.close()
        fileDataList.clear()
