from subprocess import run, Popen, PIPE, STDOUT
import json
from tkinter import *
from tkinter import ttk
import utils

class Window:
    def __init__(self, root, from_orgs, to_orgs):
        frm = ttk.Frame(root, padding=10)
        frm.grid()

        ttk.Label(frm, text="To Org:").grid(column=3, row=0)
        self.selected_to_org = StringVar(root)
        self.selected_to_org.set(to_orgs[0])
        self.to_org_combobox = ttk.Combobox(frm, values=to_orgs, textvariable=self.selected_to_org)
        self.to_org_combobox.grid(column=3, row=1)

        ttk.Label(frm, text="From Org:").grid(column=0, row=0)
        self.selected_from_org = StringVar(root)
        self.selected_from_org.set(from_orgs[0])
        self.from_org_combobox = ttk.Combobox(frm, values=from_orgs, textvariable=self.selected_from_org)
        self.from_org_combobox.grid(column=0, row=1)

        ttk.Label(frm, text="Enter Account Id:").grid(column=1, row=2)
        self.id_input = Text(frm, state=NORMAL, width=50, height=1)
        self.id_input.grid(column=1, row=3)

        ttk.Label(frm, text="Transfer Results").grid(column=1, row=5)
        self.cmd_output = Text(frm, state=NORMAL, width=50, height=20)
        self.cmd_output.grid(column=1, row=6)


        self.transfer_button = ttk.Button(frm, text='Create Data', command=self.create_data)
        self.transfer_button.grid(column=1, row=4, pady=20)

        self.progress_bar = ttk.Progressbar(frm, mode='determinate')
        self.progress_bar.grid(column=3, row=4)

    def create_data(self):
        account_id = self.id_input.get("1.0", "end-1c")
        if not account_id:
            return

        export_objects = utils.build_export_objects(account_id)
        utils.write_export_file(export_objects)
        self.progress_bar.step(49)

        self.cmd_output.insert("1.0", "")
        command = "sfdx sfdmu:run --sourceusername " + self.selected_from_org.get() + " --targetusername " + self.selected_to_org.get()
        print(command)
        output = Popen(command, stdout = PIPE, stderr = STDOUT, shell = True)
        while True:
            line = output.stdout.readline()
            self.cmd_output.insert(END, line)
            if not line: break
        self.progress_bar.step(49)

def main():
    data = run("sfdx org:list --json", capture_output=True, shell=True, text=True)
    orgs = json.loads(data.stdout)
    from_orgs = []
    to_orgs = []
    for org in orgs["result"]["nonScratchOrgs"]:
        from_orgs.append(org["alias"])
        if(org["loginUrl"] != "https://login.salesforce.com" and org["isDevHub"] != True):
            to_orgs.append(org["alias"])
    root = Tk()
    Window(root, from_orgs, to_orgs)
    root.mainloop()

main()
