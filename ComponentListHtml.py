import os


class ComponentListHtml:
    def __init__(self, projectname, path, columns, model):
        self.projectname = str(projectname)
        self.model = str(model)
        self.columns = columns
        self.path = path
        self.ModelPath = f"{self.path}/{self.projectname}/{self.model.title()}"

        if not self.model.startswith("Vw_"):
            if not os.path.exists(self.ModelPath):
                os.makedirs(self.ModelPath)
            self.CreateComponentHtml()

    def CreateComponentHtml(self):
        fileData = '<layout>' \
                   r'    <div class="right_col" role="main">' \
                   r'        <div class="container">' \
                   r'            <div class="page-title">' \
                   r'                <div class="title_left">' \
                   r'                    <h3>' \
                   f'{self.model.title()}' \
                   r'</h3>' \
                   r'                </div>' \
                   r'            </div>' \
                   r'            <hr />' \
                   r'            <div class="clearfix"></div>' \
                   r'            <button class="btn btn-sm btn-success button" style="margin: 10px;" ' \
                   r'                (click)="Add()"><i class="fas fa-plus-circle" title="Add"></i></button>' \
                   r'            <div class="col-md-12 col-sm-12">' \
                   r'                <ag-grid-angular style="width: 100%; height: 500px;" class="ag-theme-alpine"' \
                   r'                    (gridReady)="onGridReady($event)" [columnDefs]="columnDefs" [' \
                   r'rowData]="model" rowSelection="single"' \
                   r'                    pagination="true" paginationPageSize=10></ag-grid-angular>' \
                   r'            </div>' \
                   r'        </div>' \
                   r'    </div>' \
                   r'</layout>'

        file = open(f"{self.ModelPath}/{self.model}list.component.html", "w")
        file.writelines(fileData)
        file.close()
