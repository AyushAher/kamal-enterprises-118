import os


class Services:
    def __init__(self, projectname, path, columns, model):
        self.projectname = str(projectname)
        self.model = str(model)
        self.columns = columns
        self.path = path
        self.ServicePath = f"{self.path}/{self.projectname}/_services"
        if not os.path.exists(self.ServicePath):
            os.makedirs(self.ServicePath)

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
                self.Service()

    def Service(self):
        fileData = 'import { HttpClient, HttpHeaders } from "@angular/common/http";\n' \
                   'import { Injectable } from "@angular/core";\n' \
                   'import { Router } from "@angular/router";\n' \
                   'import { Observable } from "rxjs";\n' \
                   'import { map } from "rxjs/operators";\n' \
                   'import { environment } from "src/environments/environment";\n' \
                   '\n' \
                   '@Injectable({\n' \
                   '  providedIn: "root",\n' \
                   '})\n' \
                   f'export class {self.model.title()}Service\n' + \
                   '{\n' \
                   f'  public {self.model}: Observable<{self.model}>;\n' \
                   '  private corsheaders: HttpHeaders;\n' \
                   '  private root: string;\n' \
                   '  constructor(private router: Router, private http: HttpClient) {}\n' + \
                   f"  save({self.model.lower()}:{self.model.title()} )" + " {\n" \
                                                                           "    return this.http.post(`${environment.apiUrl}/" + f"/{self.model.lower()}`, {self.model.lower()});\n" \
                                                                                                                                 "  } \n\n " \
                                                                                                                                 "getAll() {\n" \
                                                                                                                                 f"    return this.http.get<{self.model.lower()}[]>" + "(`${environment.apiUrl}" + f"/{self.model.lower()}`);\n" \
                                                                                                                                                                                                                   "  }\n\n" \
                                                                                                                                                                                                                   "  getById(id: string) {\n" \
                                                                                                                                                                                                                   f"    return this.http.get<{self.model.lower()}>(\n" \
                                                                                                                                                                                                                   "      `${environment.apiUrl}" + f"/{self.model.lower()}/" + "${id}`\n" \
                                                                                                                                                                                                                                                                                "    );\n" \
                                                                                                                                                                                                                                                                                "  }\n\n" \
                                                                                                                                                                                                                                                                                "  update(id, params) {\n" \
                                                                                                                                                                                                                                                                                "    return this.http\n" \
                                                                                                                                                                                                                                                                                "      .put(`${environment.apiUrl}" + f"/{self.model.lower()}/" + "/${id}`, params)\n" \
                                                                                                                                                                                                                                                                                                                                                  "      .pipe(\n" \
                                                                                                                                                                                                                                                                                                                                                  "        map((x) => {\n" \
                                                                                                                                                                                                                                                                                                                                                  "          return x;\n" \
                                                                                                                                                                                                                                                                                                                                                  "        })\n" \
                                                                                                                                                                                                                                                                                                                                                  "      );\n" \
                                                                                                                                                                                                                                                                                                                                                  "  }\n\n" \
                                                                                                                                                                                                                                                                                                                                                  "  delete(id: string) {\n" \
                                                                                                                                                                                                                                                                                                                                                  "    return this.http.delete(`${environment.apiUrl}" + f"/{self.model.lower()}/" + "${id}`).pipe(\n" \
                                                                                                                                                                                                                                                                                                                                                                                                                                     "      map((x) => {\n" \
                                                                                                                                                                                                                                                                                                                                                                                                                                     "        return x;\n" \
                                                                                                                                                                                                                                                                                                                                                                                                                                     "      })\n" \
                                                                                                                                                                                                                                                                                                                                                                                                                                     "    );\n" \
                                                                                                                                                                                                                                                                                                                                                                                                                                     "  }\n\n" \
                                                                                                                                                                                                                                                                                                                                                                                                                                     "}\n"

        file = open(f"{self.ServicePath}/{self.model.title()}.service.ts", "w")
        file.writelines(fileData)
        file.close()
