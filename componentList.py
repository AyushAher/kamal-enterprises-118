import os


class ComponentList:
    def __init__(self, projectname, path, columns, model):
        self.projectname = str(projectname)
        self.model = str(model)
        self.columns = columns
        self.path = path
        self.ModelPath = f"{self.path}/{self.projectname}/{self.model.title()}"

        if not self.model.startswith("Vw_"):
            if not os.path.exists(self.ModelPath):
                os.makedirs(self.ModelPath)
            self.CreateComponentTS()

    def CreateComponentTS(self):
        fileData0 = 'import { Component, OnInit } from "@angular/core";\n' \
                    '@Component({\n' \
                    f'selector: "app-{self.model.title()}list",\n' \
                    f'templateUrl: "./{self.model.title()}list.component.html",\n' \
                    '})\n' \
                    f'export class {self.model.title()}listComponent implements OnInit ' \
                    '{\n' \
                    'form:FormGroup;\n ' \
                    f'model: {self.model};\n ' \
                    ' loading = false;\n' \
                    'submitted = false;\n' \
                    'isSave = false;\n ' \
                    'type: string;\n' \
                    'id: string;\n  ' \
                    'user: User;\n' \
                    'hasReadAccess: boolean = false;\n' \
                    '  hasUpdateAccess: boolean = false;\n' \
                    '  hasDeleteAccess: boolean = false;\n' \
                    '  hasAddAccess: boolean = false;\n' \
                    '  hasInternalAccess: boolean = false;\n' \
                    ' public columnDefs: ColDef[];\n' \
                    '  private columnApi: ColumnApi;\n' \
                    '  private api: GridApi;\n' \
                    '  constructor(\n' \
                    'private router: Router, \n' \
                    'private accountService: AccountService,\n' \
                    'private notificationService: NotificationService,\n' \
                    f'private Service: {self.model}Service\n' \
                    ') {}\n' \
                    '  ngOnInit() {\n' \
                    '    this.user = this.accountService.userValue;\n' \
                    '    this.columnDefs = this.createColumnDefs();\n\n' \
                    '    this.Service.getAll()\n' \
                    '      .pipe(first())\n' \
                    '      .subscribe({\n' \
                    '        next: (data: any) => {\n' \
                    '          this.model = data.object;\n' \
                    '        },\n' \
                    '        error: (error) => {\n' \
                    '          this.notificationService.showError(error, "Error");\n' \
                    '          this.loading = false;\n' \
                    '        },\n' \
                    '      });\n' \
                    '  }\n' \
                    'Add() {\n' \
                    f'    this.router.navigate(["{self.model}"]);\n' \
                    '  }\n' \
                    '' \
                    '  private createColumnDefs() {\n' \
                    '    return [\n' \
                    '      {\n' \
                    '        headerName: "Action",\n' \
                    '        field: "id",\n' \
                    '        filter: false,' \
                    '        enableSorting: false,\n' \
                    '        editable: false,\n' \
                    '        width: 100,\n' \
                    '        sortable: false,\n' \
                    '        cellRendererFramework: RenderComponent,\n' \
                    '        cellRendererParams: {\n' \
                    f'          inRouterLink: "/{self.model}",\n' \
                    f'          deleteLink: "{self.model[0:5].upper()}",\n' \
                    '          deleteaccess: this.hasDeleteAccess,\n' \
                    '        },\n' \
                    '      },\n'

        filedata2 = '        ]\n' \
                    '}\n' \
                    '  onGridReady(params:any): void {\n' \
                    '    this.api = params.api;\n' \
                    '    this.columnApi = params.columnApi;\n' \
                    '  }\n' \
                    '}\n'

        fileDataList = []
        for column in self.columns:
            if str(column[0]).endswith("id"):
                column[0] = str(column[0]).replace("id", "")

            if not (column[0] == "" or column[0] == "updatedby" or column[0] == "updatedon" or column[
                0] == "createdby" or column[0] == "createdon"):
                fileData1 = '{' \
                            f'        headerName: "{column[0].title()}",\n' \
                            f'        field: "{column[0].title()}",\n' \
                            '        filter: true,\n' \
                            f'        tooltipField: "{column[0].lower()}",\n' \
                            '        enableSorting: true,\n' \
                            '        editable: false,\n' \
                            '        sortable: true,\n' \
                            '      },\n'

                fileDataList.append(fileData1)

        file = open(f"{self.ModelPath}/{self.model}list.component.ts", "w")
        file.writelines(fileData0)
        file.writelines(fileDataList)
        file.writelines(filedata2)
        file.close()
        fileDataList.clear()
