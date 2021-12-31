import os


class ComponentHtml:
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
                   '    <div class="right_col" role="main">' \
                   '        <div class="container">' \
                   '            <div class="page-title">' \
                   '                <div class="title_left">' \
                   '                    <h3>Serial No</h3>' \
                   '                </div>' \
                   '            </div>' \
                   '            <div class="clearfix"></div>' \
                   '            <hr />' \
                   '            <div class="col-md-12 col-sm-12 ">' \
                   '                <form [formGroup]="form" (ngSubmit)="onSubmit()">' \
                   '                    <div class="row">'

        fileData0 = '</div>' \
                    '                    <br />' \
                    '                    <div class="row">' \
                    '                        <div class="col-md-6 col-sm-6" style="padding:10px;">' \
                    '<button *ngIf="hasAddAccess || hasUpdateAccess" class="btn btn-primary" type="submit"' \
                    '                                class="btn btn-primary">' \
                    '<span *ngIf="loading" class="spinner-border spinner-border-sm mr-1"></span>' \
                    '                                Submit' \
                    '                            </button>' \
                    f'<a routerLink="/{self.model}list" class="btn btn-secondary" style="margin-left: 10px;">Back</a>' \
                    '                        </div>' \
                    '                    </div>' \
                    '                </form>' \
                    '            </div>' \
                    '        </div>' \
                    '    </div>' \
                    '</layout>'

        FormFields = []

        for column in self.columns:
            if str(column[0]).endswith("id"):
                column[0] = str(column[0]).replace("id", "")
            if not (column[0] == "" or column[0] == "updatedby" or column[0] == "updatedon" or column[
                0] == "createdby" or column[0] == "createdon"):
                data = f'<div class="col-md-4 col-sm-4">\n' \
                       f'<label for="{column[0]}">{column[0].title()}</label>\n' \
                       f'<input id="{column[0]}" type="text" formControlName="{column[0]}"\n' \
                       ' class="form-control" [ngClass]="{ \' is -invalid\': ' \
                       f'submitted && f.{column[0]}\n' \
                       '.errors}" /> \n<div *ngIf="submitted &&' \
                       f' f.{column[0]}.errors" class="invalid-feedback">\n <div *ngIf="f.{column[0]}.errors.required">\n' \
                       f'{column[0]} is required\n</div>\n</div>\n</div>'

                FormFields.append(data)

        file = open(f"{self.ModelPath}/{self.model}.component.html", "w")
        file.writelines(fileData)
        file.writelines(FormFields)
        file.writelines(fileData0)
        file.close()
        FormFields.clear()
