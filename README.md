# SF Sandbox Manager

## Requirements
- Python with the tktinker lib included, can be found on [Homebrew](https://formulae.brew.sh/formula/python-tk@3.11)
- [Salesforce cli tool](https://developer.salesforce.com/tools/salesforcecli) with:
    - [SFDMU](https://help.sfdmu.com/get-started#step-1-install-the-sfdmu) plugin installed
    - Also authorize the orgs that you want to move data between


## Building for distribution
    - Run `python setup.py py2app --emulate-shell-environment`