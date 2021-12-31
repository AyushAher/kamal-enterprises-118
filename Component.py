import os


class Component:
    def __init__(self, projectname, path, columns, model):

        self.projectname = str(projectname)
        self.model = str(model)
        self.columns = columns
        self.path = path
        self.ModelPath = f"{self.path}/{self.projectname}/{self.model.title()}"

        self.DataType()

    def DataType(self):
        for x in self.columns:
            if str(x[1]).startswith("b'decimal"):
                x[1] = "number"
            elif str(x[1]).startswith("b'tinyint"):
                x[1] = "boolean"
            else:
                x[1] = "string"

        if not self.model.startswith("Vw_"):
            if not os.path.exists(self.ModelPath):
                os.makedirs(self.ModelPath)
            self.CreateComponentTS()

    def CreateComponentTS(self):
        FormFields = []
        fileData0 = 'import { Component, OnInit } from "@angular/core";\n' \
                    '@Component({\n' \
                    f'selector: "app-{self.model.title()}",\n' \
                    f'templateUrl: "./{self.model.title()}.component.html",\n' \
                    '})\n' \
                    f'export class {self.model.title()}Component implements OnInit ' \
                    '{\n' \
                    'form:FormGroup;\n ' \
                    f'model: {self.model};\n ' \
                    'loading = false;\n' \
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
                    '  constructor(\n' \
                    'private formBuilder: FormBuilder,\n ' \
                    'private route: ActivatedRoute,\n ' \
                    'private router: Router, \n' \
                    'private accountService: AccountService,\n' \
                    'private alertService: AlertService,\n' \
                    'private notificationService: NotificationService,\n' \
                    'private listTypeService: ListTypeService,\n' \
                    f'private Service: {self.model.title()}Service\n' \
                    ') {}\n' \
                    '  ngOnInit() {\n' \
                    '    this.user = this.accountService.userValue;\n' \
                    '    this.form = this.formBuilder.group({\n'

        for column in self.columns:

            if str(column[0]).endswith("id"):
                column[0] = str(column[0]).replace("id", "")
            if not (column[0] == "" or column[0] == "updatedby" or column[0] == "updatedon" or column[
                0] == "createdby" or column[0] == "createdon"):
                FormFields.append(f'{column[0]}: ["", Validators.required],\n')

        fileData1 = '})\n' \
                    '    this.id = this.route.snapshot.paramMap.get("id");\n ' \
                    'if (this.id != null) {\n' \
                    '  this.Service.getById(this.id)\n' \
                    '        .pipe(first())\n' \
                    '        .subscribe({\n' \
                    '          next: (data: any) => {\n' \
                    '            this.form.patchValue(data.object);\n' \
                    '          },\n' \
                    '          error: (error) => {\n' \
                    '            this.notificationService.showError("Error", "Error");\n' \
                    '            this.loading = false;\n' \
                    '          },\n' \
                    '        });\n' \
                    '    }\n' \
                    '}\n' \
                    '  get f() {\n' \
                    '    return this.form.controls;\n' \
                    '  }\n' \
                    'onSubmit() {\n' \
                    '    this.submitted = true;\n' \
                    '    // reset alerts on submit\n' \
                    '    this.alertService.clear();\n' \
                    '    // stop here if form is invalid\n' \
                    '    if (this.form.invalid) return\n' \
                    'if (this.id == null && this.hasAddAccess) {\n' \
                    '      this.Service.save(this.model)\n' \
                    '        .pipe(first())\n' \
                    '        .subscribe({\n' \
                    '          next: (data: ResultMsg) => {\n' \
                    '            debugger;\n' \
                    '            if (data.result) {\n' \
                    '              this.notificationService.showSuccess(\n' \
                    '                data.resultMessage,\n' \
                    '                "Success"\n' \
                    '              );\n' \
                    f' this.router.navigate(["{self.model}list"]);\n' \
                    '} else {\n' \
                    '              this.notificationService.showError(data.resultMessage, "Error");\n' \
                    '            }\n' \
                    '            this.loading = false;\n' \
                    '          },\n' \
                    '          error: (error) => {\n' \
                    '            this.notificationService.showError(error, "Error");\n' \
                    '            this.loading = false;\n' \
                    '          },\n' \
                    '        });\n' \
                    '    } else if (this.hasUpdateAccess) {\n' \
                    '    this.model = this.form.value;\n' \
                    '      this.model.id = this.id;\n' \
                    '      this.Service.update(this.id, this.model)\n' \
                    '        .pipe(first())\n' \
                    '        .subscribe({\n' \
                    '          next: (data: ResultMsg) => {\n' \
                    '            if (data.result) {\n' \
                    '              this.notificationService.showSuccess(\n' \
                    '                data.resultMessage,\n' \
                    '                "Success"\n' \
                    '              );\n' \
                    f' this.router.navigate(["{self.model}list"]);\n' \
                    '            } else {\n' \
                    '              this.notificationService.showError(data.resultMessage, "Error");\n' \
                    '            }\n' \
                    '            this.loading = false;\n' \
                    '          },\n' \
                    '          error: (error) => {\n' \
                    '            this.notificationService.showError(error, "Error");\n' \
                    '            this.loading = false;\n' \
                    '          },\n' \
                    '        });\n' \
                    '    }\n' \
                    '  }\n' \
                    '}\n'

        file = open(f"{self.ModelPath}/{self.model.title()}.component.ts", "a")
        file.writelines(fileData0)
        file.writelines(FormFields)
        file.writelines(fileData1)
        file.close()
        FormFields.clear()
