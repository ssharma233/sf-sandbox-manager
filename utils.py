from models import ExportItem, ExportObject

def build_export_objects(account_id):
    export_items = []
    query = f"SELECT Id, Name, RecordTypeId, NumberOfEmployees, Inception_Date__c, Phone, Industry, BillingStreet, BillingCity, BillingState, BillingCountry FROM Account WHERE Id = '{account_id}'"
    export_items.append(ExportItem(query))

    query = f"SELECT Id, FirstName, Lastname, RecordTypeId, AccountId FROM Contact WHERE AccountId = '{account_id}'"
    export_items.append(ExportItem(query))

    query = f"SELECT Id, Name, StageName, CloseDate, Contact__c, Loan_Assist_ID__c, Application_Number__c, Estimated_Annual_Revenue__c, Amount, RecordTypeId, AccountId FROM Opportunity WHERE AccountId = '{account_id}'"
    export_items.append(ExportItem(query))

    query = f"SELECT Id, Name, State__c, Opportunity__c FROM Submission__c WHERE Opportunity__r.AccountId = '{account_id}'"
    export_items.append(ExportItem(query))

    return ExportObject(export_items)

def write_export_file(export_object):
    f = open("export.json", "w")
    f.write(export_object.toJSON())
    f.close()