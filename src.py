import os
import shutil


class SrcFolder:
    def __init__(self, projectname, path):
        self.projectname = projectname
        self.path = path

        (os.mkdir(f"{self.path}/{self.projectname}/src"), self.MainTs()) if os.path.exists(
            f"{self.path}/{self.projectname}/src") else print("'Src' Directory Exists")

    def MainTs(self):
        fileData = "import { enableProdMode } from '@angular/core';\n"\
            "import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';\n"\
            "import { AppModule } from './app/app.module';\n"\
            "import { environment } from './environments/environment';\n"\
            "if (environment.production) \n"\
            "{\n"\
            "enableProdMode();\n"\
            "}\n"\
            "platformBrowserDynamic()\n"\
            ".bootstrapModule(AppModule)\n"\
            ".catch(err => console.error(err));"

        File = open(f"{self.path}/{self.projectname}/src/main.ts", "w")
        File.writelines(fileData)
        File.close()
        self.AllFiles()

    # style.css, favicon included:-
    def AllFiles(self):
        # polyfills.ts file
        Polyfills = [
            "/**",
            "* This file includes polyfills needed by Angular and is loaded before the app.\n",
            "* You can add your own extra polyfills to this file.\n",
            "*\n",
            "* This file is divided into 2 sections:\n",
            "*   1. Browser polyfills. These are applied before loading ZoneJS and are sorted by browsers.\n",
            "*   2. Application imports. Files imported after ZoneJS that should be loaded before your main\n",
            "*      file.\n",
            "*\n",
            '* The current setup is for so-called "evergreen" browsers; the last versions of browsers that\n',
            "* automatically update themselves. This includes Safari >= 10, Chrome >= 55 (including Opera),\n",
            "* Edge >= 13 on the desktop, and iOS 10 and Chrome on mobile.\n",
            "*\n",
            "* Learn more in https://angular.io/guide/browser-support\n",
            "*/\n",
            "\n",
            "/***************************************************************************************************\n",
            "* BROWSER POLYFILLS\n",
            "*/\n",
            "\n",
            "/**\n",
            "* IE11 requires the following for NgClass support on SVG elements\n",
            "*/\n",
            "// import 'classlist.js';  // Run `npm install --save classlist.js`.\n",
            "\n",
            "/**\n",
            "* Web Animations `@angular/platform-browser/animations`\n",
            "* Only required if AnimationBuilder is used within the application and using IE/Edge or Safari.\n",
            "* Standard animation support in Angular DOES NOT require any polyfills (as of Angular 6.0).\n",
            "*/\n",
            "// import 'web-animations-js';  // Run `npm install --save web-animations-js`.\n",
            "\n",
            "/**\n",
            "* By default, zone.js will patch all possible macroTask and DomEvents\n",
            "* user can disable parts of macroTask/DomEvents patch by setting following flags\n",
            "* because those flags need to be set before `zone.js` being loaded, and webpack\n",
            "* will put import in the top of bundle, so user need to create a separate file\n",
            "* in this directory (for example: zone-flags.ts), and put the following flags\n",
            "* into that file, and then add the following code before importing zone.js.\n",
            "* import './zone-flags';\n",
            "*\n",
            "* The flags allowed in zone-flags.ts are listed here.\n",
            "*\n",
            "* The following flags will work for all browsers.\n",
            "*\n",
            "* (window as any).__Zone_disable_requestAnimationFrame = true; // disable patch requestAnimationFrame\n",
            "* (window as any).__Zone_disable_on_property = true; // disable patch onProperty such as onclick\n",
            "* (window as any).__zone_symbol__UNPATCHED_EVENTS = ['scroll', 'mousemove']; // disable patch specified eventNames\n",
            "*\n",
            "*  in IE/Edge developer tools, the addEventListener will also be wrapped by zone.js\n",
            "*  with the following flag, it will bypass `zone.js` patch for IE/Edge\n",
            "*\n",
            "*  (window as any).__Zone_enable_cross_context_check = true;\n",
            "*\n",
            "*/\n",
            "\n",
            "/***************************************************************************************************\n",
            "* Zone JS is required by default for Angular itself.\n",
            "*/\n",
            "import 'zone.js';  // Included with Angular CLI.\n",
            "\n",
            "\n",
            "/***************************************************************************************************\n",
            "* APPLICATION IMPORTS\n",
            "*/"
        ]

        PolyfillsFile = open(
            f"{self.path}/{self.projectname}/src/polyfills.ts", "w")
        PolyfillsFile.writelines(Polyfills)
        PolyfillsFile.close()

        # style.css file
        StyleFile = open(f"{self.path}/{self.projectname}/src/style.css", "w")
        StyleFile.close()

        # copy favicon
        shutil.copyfile(f"{os.getcwd()}\\favicon.ico",
                        f"{self.path}/{self.projectname}/src")

        # index.html file
        IndexHtmlData = [
            '<!doctype html>\n'
            '<html lang="en">\n',
            '<head>\n',
            '  <meta charset="utf-8">\n',
            f'  <title>{self.projectname}</title>\n',
            '  <base href="/">\n',
            '  <meta name="viewport" content="width=device-width, initial-scale=1">\n',
            '  <link rel="icon" type="image/x-icon" href="favicon.ico">\n',
            '</head>\n',
            '<body>\n',
            '  <app-root></app-root>\n',
            '</body>\n',
            '</html>\n',
        ]
        IndexHtmlFile = open(
            f"{self.path}/{self.projectname}/src/index.html", "w")
        IndexHtmlFile.writelines(IndexHtmlData)
        IndexHtmlFile.close()

        TestTsData = [
            "// This file is required by karma.conf.js and loads recursively all the .spec and framework files",
            "import 'zone.js/testing';\n",
            "import { getTestBed } from '@angular/core/testing';\n",
            "import {\n",
            "  BrowserDynamicTestingModule,\n",
            "  platformBrowserDynamicTesting\n",
            "} from '@angular/platform-browser-dynamic/testing';\n",
            "\n",
            "declare const require: {\n",
            "  context(path: string, deep?: boolean, filter?: RegExp): {\n",
            "    keys(): string[];\n",
            "    <T>(id: string): T;\n",
            "  };\n",
            "};\n",
            "\n",
            "// First, initialize the Angular testing environment.\n",
            "getTestBed().initTestEnvironment(\n",
            "  BrowserDynamicTestingModule,\n",
            "  platformBrowserDynamicTesting()\n",
            ");\n",
            "// Then we find all the tests.\n",
            "const context = require.context('./', true, /\.spec\.ts$/);\n",
            "// And load the modules.\n",
            "context.keys().map(context);\n"
        ]

        TestTsFile = open(
            f"{self.path}/{self.projectname}/src/test.ts", "w")
        TestTsFile.writelines(TestTsData)
        TestTsFile.close()
