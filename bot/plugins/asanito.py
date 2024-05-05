from typing import Dict
from .plugin import Plugin
import requests
import json
from datetime import datetime

ownerUserID = 370
BEARERAUTH = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjYxNTlFOTYwOUE2QUY1OTQwMDhCQkNEMTBBMkI5QTQ1IiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE3MTQ5MzkwMDYsImV4cCI6MTcxNzUzMTAwNiwiaXNzIjoiaHR0cDovL2lkZW50aXR5YXBpLXNlcnZpY2U6ODAwMyIsImF1ZCI6ImFzYW5pdG8iLCJjbGllbnRfaWQiOiJhc2FuaXRvQ2xpZW50Iiwic3ViIjoiMjI5NCIsImF1dGhfdGltZSI6MTcxNDkzOTAwNiwiaWRwIjoibG9jYWwiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ3b29kc3RvcmUtMDkwMTc1Mzk1MDgiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjM3MCIsInVzZXJJZCI6IjM3MCIsInBlcm1pc3Npb25zIjoiUGVybWlzc2lvbnNEYXNoYm9hcmRDb250ZW50LTEsUGVybWlzc2lvbnNGaW5hbmNpYWxDaGFydC0xLFBlcm1pc3Npb25zRmluYW5jZVJlcG9ydC0xLFBlcm1pc3Npb25zVXNlcnMtMSxQZXJtaXNzaW9uc1N0YXRpb24tMSxQZXJtaXNzaW9uc0FjcXVhaW50aW5nVHlwZS0xLFBlcm1pc3Npb25zUHJpY2VVbml0LTEsUGVybWlzc2lvbnNKb2JQb3NpdGlvbi0xLFBlcm1pc3Npb25zTmljTmFtZVRpdGxlLTEsUGVybWlzc2lvbnNTb2NpYWxUeXBlLTEsUGVybWlzc2lvbnNWb2lwTnVtYmVyLTEsUGVybWlzc2lvbnNQaG9uZUNhbGxTdWJqZWN0LTEsUGVybWlzc2lvbnNSb2xlLTEsUGVybWlzc2lvbnNGdW5uZWwtMSxQZXJtaXNzaW9uc0Z1bm5lbExldmVsLTEsUGVybWlzc2lvbnNPcmdhbml6YXRpb24tMSxQZXJtaXNzaW9uc0JhbmstMSxQZXJtaXNzaW9uc0JhbmtBY2NvdW50LTEsUGVybWlzc2lvbnNCYW5rQWNjb3VudFByb2ZpbGUtMSxQZXJtaXNzaW9uc0JhbmtDaGFjay0xLFBlcm1pc3Npb25zUHJvcGVydHlHcm91cC0xLFBlcm1pc3Npb25zUHJvcGVydHktMSxQZXJtaXNzaW9uc09wZXJhdGluZ0luY29tZS0xLFBlcm1pc3Npb25zT3BlcmF0aW5nSW5jb21lUHJvZmlsZS0xLFBlcm1pc3Npb25zTm9uT3BlcmF0aW5nSW5jb21lLTEsUGVybWlzc2lvbnNOb25PcGVyYXRpbmdJbmNvbWVQcm9maWxlLTEsUGVybWlzc2lvbnNDb3N0R3JvdXAtMSxQZXJtaXNzaW9uc0Nvc3RUeXBlLTEsUGVybWlzc2lvbnNJbnRlcm5hbEJhbmtBY2NvdW50VHJuc2FjdGlvbi0xLFBlcm1pc3Npb25zSW50ZXJuYWxCYW5rQWNjb3VudFRybnNhY3Rpb25Qcm9maWxlLTEsUGVybWlzc2lvbnNMb2FuLTEsUGVybWlzc2lvbnNDb3N0LTEsUGVybWlzc2lvbnNDb3N0UHJvZmlsZS0xLFBlcm1pc3Npb25zUHVyY2hhc2luZ0Nvc3QtMSxQZXJtaXNzaW9uc1B1cmNoYXNpbmdDb3N0UHJvZmlsZS0xLFBlcm1pc3Npb25zU2hhcmVIb2xkZXItMSxQZXJtaXNzaW9uc1NoYXJlSG9sZGVyVHJhbnNhY3Rpb24tMSxQZXJtaXNzaW9uc0d1YXJhbnRlZS0xLFBlcm1pc3Npb25zU2FsYXJ5VHJhbnNhY3Rpb24tMSxQZXJtaXNzaW9uc0NvbnRhY3QtMSxQZXJtaXNzaW9uc0ZpbmFuY2UtMSxQZXJtaXNzaW9uc1BheW1lbnRSZWNlaXB0LTEsUGVybWlzc2lvbnNDb250cmFjdC0xLFBlcm1pc3Npb25zQ29udHJhY3RQcm9maWxlLTEsUGVybWlzc2lvbnNDb250cmFjdFRlbXBsYXRlLTEsUGVybWlzc2lvbnNMZXR0ZXJUZW1wbGF0ZS0xLFBlcm1pc3Npb25zUGF5bWVudFRlcm0tMSxQZXJtaXNzaW9uc0xldHRlci0xLFBlcm1pc3Npb25zTGV0dGVyUHJvZmlsZS0xLFBlcm1pc3Npb25zQXBwbHlGb3JtLTEsUGVybWlzc2lvbnNTdXJ2ZXlGb3JtLTEsUGVybWlzc2lvbnNQcm9jZXNzLTEsUGVybWlzc2lvbnNQcm9jZXNzSm91cm5leS0xLFBlcm1pc3Npb25zVXNlclRyZWUtMSxQZXJtaXNzaW9uc1JlcG9ydC0xLFBlcm1pc3Npb25zTWVldGluZ3NDYWxlbmRlci0xLFBlcm1pc3Npb25zUGVyc29uNzY3LFBlcm1pc3Npb25zUGVyc29uUHJvZmlsZS0xLFBlcm1pc3Npb25zQ29tcGFueTc2NyxQZXJtaXNzaW9uc0NvbXBhbnlQcm9maWxlLTEsUGVybWlzc2lvbnNDb250YWN0U3VwcG9ydExldmVsLTEsUGVybWlzc2lvbnNJbnZvaWNlSXNzdWFuY2VBdXRvQnBtc1NldHRpbmctMSxQZXJtaXNzaW9uc05lZ290aWF0aW9uTGV2ZWxDaGFuZ2VDb250cm9sU2V0dGluZy0xLFBlcm1pc3Npb25zRW1haWwtMSxQZXJtaXNzaW9uc0VtYWlsQ29uZmlnLTEsUGVybWlzc2lvbnNJbnRlcm5hbGl6YXRpb24tMSxQZXJtaXNzaW9uc0RlZmF1bHRGdW5uZWwtMSxQZXJtaXNzaW9uc0NoYW5nZVBhc3N3b3JkLTEsUGVybWlzc2lvbnNBdXRvbWF0aWNNZXNzYWdlU2V0dGluZy0xLFBlcm1pc3Npb25zTWFzc1Ntcy0xLFBlcm1pc3Npb25zTG9ncy0xLFBlcm1pc3Npb25zQnVzaW5lc3NQcm9jZXNzLTEsUGVybWlzc2lvbnNCdXNpbmVzc1Byb2Nlc3NQcm9maWxlLTEsUGVybWlzc2lvbnNQcm9jZXNzVHlwZS0xLFBlcm1pc3Npb25zUHJvY2Vzc0xldmVsLTEsUGVybWlzc2lvbnNSZW1pbmRlclRhc2stMSxQZXJtaXNzaW9uc1dhcmVob3VzZS0xLFBlcm1pc3Npb25zUHJvZHVjdC0xLFBlcm1pc3Npb25zQmFyY29kZVNldHRpbmctMSxQZXJtaXNzaW9uc1Byb2R1Y3RQcm9maWxlLTEsUGVybWlzc2lvbnNQcm9kdWN0Q2F0ZWdvcnktMSxQZXJtaXNzaW9uc0ludm9pY2U3Njc5LFBlcm1pc3Npb25zSW52b2ljZVByb2ZpbGUtMSxQZXJtaXNzaW9uc05lZ290aWF0aW9uMTkxLFBlcm1pc3Npb25zTmVnb3RpYXRpb25Qcm9maWxlLTEsUGVybWlzc2lvbnNQcm9kdWN0VW5pdC0xLFBlcm1pc3Npb25zV29ya0ZpZWxkLTEsUGVybWlzc2lvbnNNZWV0aW5nUm9vbS0xLFBlcm1pc3Npb25zRmFpbGVkQW5kU3VjY2VlZGVkTmVnb3RpYXRpb25zUmVwb3J0LTEsUGVybWlzc2lvbnNTYWxlSW52b2ljZXNSZXBvcnQtMSxQZXJtaXNzaW9uc1NlbGxlcnNSZXBvcnQtMSxQZXJtaXNzaW9uc05lZ290aWF0aW9uU2V0dGluZy0xLFBlcm1pc3Npb25zVm9pcFNldHRpbmctMSxQZXJtaXNzaW9uc0ludGVyYWN0aW9uVHlwZS0xLFBlcm1pc3Npb25zQ29tbWlzc2lvblNldHRpbmctMSxQZXJtaXNzaW9uc0NvbW1pc3Npb24tMSxQZXJtaXNzaW9uc0ZpZWxkU2V0dGluZy0xLFBlcm1pc3Npb25zSWRlbnRpdHlDb250YWN0LTEsUGVybWlzc2lvbnNQYXltZW50R2F0ZXdheS0xLFBlcm1pc3Npb25zU2VwaWRhclNlcnZpY2UtMSIsIkN1c3RvbWVySWQiOiIxMDk2IiwiQ3VzdG9tZXIiOiJ3b29kc2hvcGEiLCJSb2xlIjoid29vZHN0b3JlLUFkbWluc3RyYXRvciIsImp0aSI6IjI2QkVFNzBEMzYyNzYxRkYyOEExNzFFMERGNzYzRjgxIiwiaWF0IjoxNzE0OTM5MDA2LCJzY29wZSI6WyJhc2FuaXRvIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbInBhc3N3b3JkIl19.XvkHtVHbWXOuFxZTr2fezOYxCxhwwFuVL74g7bL9UXZJjSakmOPUalO4anuwcZQwx1YQRppqSf1AOZoGz6KsL9gbqL7ZWz6PAW7-ChcRhVGEdPdWDKmf8SOIbhC0qxsdYSDcBruDo0M1rAarlyfbHNM9hZu7hCvb1OegFmXWo3Y6O2yuDWcO529F1rRbp9veNzb8pZsehIOTMCuAp79Yodz7wjfTlg2E8JURIwXa-fdlZlOPxvc77eDRKyLZ9samZqVA4pZXa6kxA9b45MkrRwe_d7SFndZS31VbJ1WRcIqhOZL4mNfoHyzDgyyn95ToB_5LL6ySBKSfLqfFi4R_ww"

headers = {
"accept": "application/json, text/plain, */*",
"accept-language": "en-US,en;q=0.9,fa;q=0.8",
"authorization": BEARERAUTH, 
"content-type": "application/json",
"sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "\"Windows\"",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-site"
}


class AsanitoPlugin(Plugin):
    """
    A plugin to add, modify or view data in asanito CRM.
    """

    def get_source_name(self) -> str:
        return "asanito"    
    
    
    
    def get_spec(self) -> [Dict]:
        return [
        {
            "name": "AddLeanWithApi",
            "description": "Creates a profile for a person in the Asanito CRM.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "First name of the person"
                    },
                    "lastName": {
                        "type": "string",
                        "description": "Last name of the person",
                    },
                    "mobiles": {
                        "type": "string",
                        "description": "Phone number of the person, should be in latin numbers without extra characters. e.g. 09123456789",
                    },
                    "genderID": {
                        "type": "number",
                        "description": "Gender of the person. Write 1 for male, 2 for female, and 3 when the gender is unknown. Try guessing the gender based on the given name by user",
                    }
                },
                "required": ["name", "lastName", "mobiles"],
            },
        },
        {
            "name": "getPhoneByName",
            "description": "finds the phone number of a person in the Asanito CRM.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "name of the person who we want to find his/her phone number"
                        }
                },
                "required": ["name"],
            },
        },
    {
        "name": "addNote",
        "description": "creates a note for a person in the asanito CRM.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "name of the person who we want to add a note in his/her profile"
                },
                "title": {
                    "type": "string",
                    "description": "summarize the content into a short title for the note",
                },
                "content": {
                    "type": "string",
                    "description": "the note that the user wants to add to a person's profile",
                }
            },
            "required": ["name","title","content"],
        },
    },
    {
        "name": "addNegotiation",
        "description": "creates a Negotiation. can be for a person in the asanito CRM but the person is optional.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "title of negotiation"
                },
                "name": {
                    "type": "string",
                    "description": "name of the person who we want to create a negotiation for if asked to",
                }
            },
            "required": ["title"],
        },
    },
    {
        "name": "addCall",
        "description": "creates a call log for a person in the asanito CRM.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "name of the person who we want to add a call log in his/her profile"
                },
                "content": {
                    "type": "string",
                    "description": "the note/title that the user wants to add to the call log",
                }
            },
            "required": ["name","content"]
        }
    },
    {
        "name": "newMeeting",
        "description": "creates a meeting for a person in the asanito CRM.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "name of the person who we want to add a meeting in his/her profile"
                },
                "title": {
                    "type": "string",
                    "description": "summarize the content into a short title for the meeting"
                },
                "content": {
                    "type": "string",
                    "description": "the note/title that the user wants to add to the meeting",
                }
            },
            "required": ["name","content", "title"]
        }
    },
    {
        "name": "getRemainedAmount",
        "description": "Finds the balance of the person's account. If this amount is positive, it is a debit, if it is negative, it is a credit",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "name of the person"
                }
            },
            "required": ["name"]
        }
    },
    {
        "name": "toDo",
        "description": "creates a task / to do in the asanito CRM.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "title of the task."
                },
                "description": {
                    "type": "string",
                    "description": "description of the task. guess the description based on user input"
                },
                "remindDate": {
                    "type": "string",
                    "description": "reminder date. by default set the reminder date for tomorrow morning. make sure you format the date like this: %Y-%m-%dT%H:%M (AD date)",
                },
                "dueDate": {
                    "type": "string",
                    "description": "due date. optional",
                }
            },
            "required": ["title","description", "remindDate"]
        }
    },
    {
        "name": "getSegragatedIncome",
        "description": "This function finds the disaggregated income in a specified time period",
        "parameters": {
            "type": "object",
            "properties": {
                "fromdate": {
                    "type": "string",
                    "description": "Time period start date. make sure time is in this format: %Y-%m-%dT00:00:00. e.g. 2024-03-20T00:00:00"
                },
                "todate": {
                    "type": "string",
                    "description": "Time period end date. make sure time is in this format: %Y-%m-%dT00:00:00. e.g. 2024-03-20T00:00:00"
                }
            },
            "required": ["fromdate","todate"]
        }
    },
    {
        "name": "getTotalIncomeCost",
        "description": "This function finds the income and expenses in a certain period of time",
        "parameters": {
            "type": "object",
            "properties": {
                "fromdate": {
                    "type": "string",
                    "description": "Time period start date. make sure time is in this format: %Y-%m-%dT00:00:00. e.g. 2024-03-20T00:00:00"
                },
                "todate": {
                    "type": "string",
                    "description": "Time period end date. make sure time is in this format: %Y-%m-%dT00:00:00. e.g. 2024-03-20T00:00:00"
                }
            },
            "required": ["fromdate","todate"]
        }
    },
    {
        "name": "getPurchaseSaleInvoices",
        "description": "A function to get the total amount of purchase and sales invoices",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }

        ]  
        
      
        
    async def execute(self,function_name, helper, **kwargs) -> Dict:
        if function_name == 'AddLeanWithApi':
            return self.AddLeanWithApi(**kwargs)
        elif function_name == 'getPhoneByName':
            return self.getPhoneByName(**kwargs)
        elif function_name == 'newMeeting':
            return self.newMeeting(**kwargs)
        elif function_name == 'addNote':
            return self.addNote(**kwargs)
        elif function_name == 'addNegotiation':
            return self.addNegotiation(**kwargs)
        elif function_name == 'addCall':
            return self.addCall(**kwargs)
        elif function_name == 'getRemainedAmount':
            return self.getRemainedAmount(**kwargs)
        elif function_name == 'toDo':
            return self.toDo(**kwargs)
        elif function_name == 'getSegragatedIncome':
            return self.getSegragatedIncome(**kwargs)
        elif function_name == 'getTotalIncomeCost':
            return self.getTotalIncomeCost(**kwargs)
        elif function_name == 'getPurchaseSaleInvoices':
            return self.getPurchaseSaleInvoices(**kwargs)
        
        
        
        
    def AddLeanWithApi(self, **kwargs):
        url = 'https://clouddevbak.asanito.app/api/asanito/Person/AddLeanWithApi'   
        data = [
        {
        "name": "",
        "lastName": "",
        "oldSystemID": 1,
        "mobiles": [""],
        "nationalCode": "",
        "genderID": 3
        }
        ]
        data[0]["name"] = kwargs["name"]
        data[0]["lastName"] = kwargs["lastName"]
        data[0]["mobiles"] = [kwargs["mobiles"]]
        if "genderID" in kwargs:
            data[0]["genderID"] = kwargs["genderID"]   
 
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return {'message': 'Data posted successfully!'}
        else:
            return {'error': 'Error posting data'}
    

    def getPhoneByName(self, **kwargs):

        url = 'https://clouddevbak.asanito.app/api/asanito/Person/advancedSearch'
        
        
        data = {
          "acquaintionTypeIDs": "",
          "interactionIDs": "",
          "genderIDs": "",
          "orderType": True,
          "value": kwargs["name"],
          "skip": 0,
          "take": 20,
          "filterCustomFields": []
        }
        
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            result_json = response.json()
            if "resultList" in result_json and len(result_json["resultList"]) > 0:
                id = result_json["resultList"][0]["phoneNumbers"][0]["mobile"]
                return id
            else:
                return 'Could not find the person'
        else:
            return 'Failed to fetch data'

    def getUserIdByName(self, name):
        
        url = 'https://clouddevbak.asanito.app/api/asanito/Person/advancedSearch'
    
        data = {
          "acquaintionTypeIDs": "",
          "interactionIDs": "",
          "genderIDs": "",
          "orderType": True,
          "value": name,
          "skip": 0,
          "take": 20,
          "filterCustomFields": []
        }
    
    
        response = requests.post(url, json=data, headers=headers)
    
        if response.status_code == 200:
            result_json = response.json()
            if "resultList" in result_json and len(result_json["resultList"]) > 0:
                id = result_json["resultList"][0]["id"]
                return id
            else:
                return 'Could not find the person'
        else:
            return 'Failed to fetch data'
    
        
    def addNote(self, **kwargs):     
        
        url = 'https://clouddevbak.asanito.app/api/asanito/Note/add'
    
        data = {
                 "title": kwargs["title"],
                 "htmlContent": "<p>" + kwargs["content"] + "</p>",
                 "pin": False,
                 "relatedEntities": [
                   {
                     "entityID": self.getUserIdByName(kwargs["name"]),
                     "type": 1
                   }
                 ]
               }
    
        response = requests.post(url,json=data, headers=headers)
        if response.status_code == 200:
          return('Data posted successfully!')
        else:
          return('Error posting data')
        
        
    def addNegotiation(self, **kwargs):     
        
        url = 'https://clouddevbak.asanito.app/api/asanito/Negotiation/addNew'
    
        data = {
                  "description": "",
                  "title": kwargs["title"],
                  "code": 0,
                  "amount": "10000",
                  "funnelLevelID": 130,
                  "productCategoryIDs": [],
                  "productIDs": [],
                  "personContectIDs": [
                    
                  ],
                  "companyContectIDs": [],
                  "successReasons": "",
                  "failureReasons": "",
                  "companyPartnerIDs": [],
                  "personPartnerIDs": [],
                  "mounthlyIncome": 0,
                  "ownerUserID": ownerUserID
                }

        if "name" in kwargs and kwargs["name"] is not None:
            data["personContectIDs"][0] = self.getUserIdByName(kwargs["name"])
    
        response = requests.post(url,json=data, headers=headers)
        if response.status_code == 200:
          return('Data posted successfully!')
        else:
          return('Error posting data')
        
        
    def addCall(self, **kwargs):     
        
        url = 'https://clouddevbak.asanito.app/api/asanito/PhoneCall/addNew'
    
        data = {
                 "date": datetime.now().strftime("%Y-%m-%dT%H:%M"),
                 "phoneCallSubjectID": 59,
                 "callResult": 2,
                 "htmlContent": "<p>" + kwargs["content"] + "</p>",
                 "pin": False,
                 "callerUserID": ownerUserID,
                 "personID": self.getUserIdByName(kwargs["name"]),
                 "companyID": None,
                 "callType": 0,
                 "singleSelectSubmittedProperties": []
               }
            
        response = requests.post(url,json=data, headers=headers)
        if response.status_code == 200:
          return('Data posted successfully!')
        else:
          return('Error posting data')
    
    
    def newMeeting(self, **kwargs):     
        
        url = 'https://clouddevbak.asanito.app/api/asanito/Meeting/add'

        data = {
                  "title": kwargs["title"],
                  "participants": [
                    {
                      "personID": self.getUserIdByName(kwargs["name"]),
                      "companyID": 0,
                      "type": 1
                    }
                  ],
                  "meetingRoomId": None,
                  "createGoogleMeetLink": False,
                  "outcome": 4,
                  "date": datetime.now().strftime("%Y-%m-%dT%H:%M"),
                  "duration": 30,
                  "htmlContent": "<p>" + kwargs["content"] + "</p>",
                  "mainParticipantUserID": ownerUserID,
                  "otherParticipantUserIDs": [],
                  "pin": False,
                  "relatedCompanyIDs": [],
                  "relatedNegotiationIDs": [],
                  "relatedPersonIDs": [],
                  "outsideRoom": {
                    "address": None,
                    "location": None,
                    "name": "دفتر آسانیتو"
                  }
                }

        response = requests.post(url,json=data, headers=headers)
        if response.status_code == 200:
          return('Data posted successfully!')
        else:
          return('Error posting data')



    def getRemainedAmount(self, **kwargs):     
        
        url = 'https://clouddevbak.asanito.app/api/asanito/Person/getDetailedByID?ID=' + str(self.getUserIdByName(kwargs["name"]))

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            data = response.json()
            remained_amount = data["remainedAmount"]
            return remained_amount
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            return None


    def getPurchaseSaleInvoices(self):     
        
        url = 'https://clouddevbak.asanito.app/api/asanito/Finance/getFinanceStatistics?companyID=0&personID=0'

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            data = response.json()
            formatted_text = ""
            formatted_text = f"مبلغ کل فاکتور های فروش: {data['sellAmount']} ریال\n"
            formatted_text += f"مبلغ کل فاکتور های خرید: {data['buyAmount']} ریال"
            return formatted_text
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            return None


      
    def toDo(self, **kwargs):     
        
        url = 'https://clouddevbak.asanito.app/api/asanito/ReminderTask/addNew'
    
        data = {
                  "title": kwargs["title"],
                  "description": kwargs["description"],
                  "priority": 3,
                  "remindDate": kwargs["remindDate"],
                  "dueDate": "",
                  "sms": False,
                  "email": False,
                  "responsibleUserID": ownerUserID,
                  "negotiationID": None,
                  "bussinesProcessID": None,
                  "personIDs": []
                }
    
        if "dueDate" in kwargs and kwargs["dueDate"] is not None:
            data["dueDate"] = kwargs["dueDate"]
        response = requests.post(url,json=data, headers=headers)
        if response.status_code == 200:
          return ('Data posted successfully!')
        else:
          return('Error')
      
      
    def getSegragatedIncome(self, **kwargs):     
        
        url = 'https://clouddevbak.asanito.app/api/asanito/FinancialChart/getSegragatedIncome'
    
        data = {
                  "companyID": None,
                  "personID": None,
                  "from": kwargs["fromdate"],
                  "to": kwargs["todate"]
                }

        response = requests.post(url,json=data, headers=headers)
        if response.status_code == 200:
            result_json = response.json()
            formatted_text = ""
            for item in result_json:
                formatted_text += f"{item['x']}: {item['y']} ریال\n"
            return formatted_text
        else:
            return('Error')
      
      
      
    def getTotalIncomeCost(self, **kwargs):     
        
        url = 'https://clouddevbak.asanito.app/api/asanito/FinancialChart/getTotalIncomeCost'
    
        data = {
                  "fromDate": kwargs["fromdate"],
                  "toDate": kwargs["todate"],
                  "companyID": None,
                  "personID": None
                }
        

        response = requests.post(url,json=data, headers=headers)
        if response.status_code == 200:
          result_json = response.json()
          formatted_text = ""
          for item in result_json:
            formatted_text += f"{item['x']}: {item['y']} ریال\n"
          return formatted_text
        else:
          return('Error')
      
