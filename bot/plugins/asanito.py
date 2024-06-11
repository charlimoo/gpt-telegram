from typing import Dict
from .plugin import Plugin
import requests
import json
from datetime import datetime

ownerUserID = 556
BEARERAUTH = "bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjI2MjE2MTMxMUJFN0FDMjAzRjdBREU3ODQyQzM5OTkzIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE3MTgxMTQxOTAsImV4cCI6MTcyMDcwNjE5MCwiaXNzIjoiaHR0cDovL2lkZW50aXR5YXBpLXNlcnZpY2U6ODAwMyIsImF1ZCI6ImFzYW5pdG8iLCJjbGllbnRfaWQiOiJhc2FuaXRvQ2xpZW50Iiwic3ViIjoiMjQ1NSIsImF1dGhfdGltZSI6MTcxODExNDE5MCwiaWRwIjoibG9jYWwiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJraWFuYS0wOTIxMzIxNTA2MCIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiNTU2IiwidXNlcklkIjoiNTU2IiwicGVybWlzc2lvbnMiOiJQZXJtaXNzaW9uc0Rhc2hib2FyZENvbnRlbnQtMSxQZXJtaXNzaW9uc0ZpbmFuY2lhbENoYXJ0LTEsUGVybWlzc2lvbnNGaW5hbmNlUmVwb3J0LTEsUGVybWlzc2lvbnNVc2Vycy0xLFBlcm1pc3Npb25zU3RhdGlvbi0xLFBlcm1pc3Npb25zQWNxdWFpbnRpbmdUeXBlLTEsUGVybWlzc2lvbnNQcmljZVVuaXQtMSxQZXJtaXNzaW9uc0pvYlBvc2l0aW9uLTEsUGVybWlzc2lvbnNOaWNOYW1lVGl0bGUtMSxQZXJtaXNzaW9uc1NvY2lhbFR5cGUtMSxQZXJtaXNzaW9uc1ZvaXBOdW1iZXItMSxQZXJtaXNzaW9uc1Bob25lQ2FsbFN1YmplY3QtMSxQZXJtaXNzaW9uc1JvbGUtMSxQZXJtaXNzaW9uc0Z1bm5lbC0xLFBlcm1pc3Npb25zRnVubmVsTGV2ZWwtMSxQZXJtaXNzaW9uc09yZ2FuaXphdGlvbi0xLFBlcm1pc3Npb25zQmFuay0xLFBlcm1pc3Npb25zQmFua0FjY291bnQtMSxQZXJtaXNzaW9uc0JhbmtBY2NvdW50UHJvZmlsZS0xLFBlcm1pc3Npb25zQmFua0NoYWNrLTEsUGVybWlzc2lvbnNQcm9wZXJ0eUdyb3VwLTEsUGVybWlzc2lvbnNQcm9wZXJ0eS0xLFBlcm1pc3Npb25zT3BlcmF0aW5nSW5jb21lLTEsUGVybWlzc2lvbnNPcGVyYXRpbmdJbmNvbWVQcm9maWxlLTEsUGVybWlzc2lvbnNOb25PcGVyYXRpbmdJbmNvbWUtMSxQZXJtaXNzaW9uc05vbk9wZXJhdGluZ0luY29tZVByb2ZpbGUtMSxQZXJtaXNzaW9uc0Nvc3RHcm91cC0xLFBlcm1pc3Npb25zQ29zdFR5cGUtMSxQZXJtaXNzaW9uc0ludGVybmFsQmFua0FjY291bnRUcm5zYWN0aW9uLTEsUGVybWlzc2lvbnNJbnRlcm5hbEJhbmtBY2NvdW50VHJuc2FjdGlvblByb2ZpbGUtMSxQZXJtaXNzaW9uc0xvYW4tMSxQZXJtaXNzaW9uc0Nvc3QtMSxQZXJtaXNzaW9uc0Nvc3RQcm9maWxlLTEsUGVybWlzc2lvbnNQdXJjaGFzaW5nQ29zdC0xLFBlcm1pc3Npb25zUHVyY2hhc2luZ0Nvc3RQcm9maWxlLTEsUGVybWlzc2lvbnNTaGFyZUhvbGRlci0xLFBlcm1pc3Npb25zU2hhcmVIb2xkZXJUcmFuc2FjdGlvbi0xLFBlcm1pc3Npb25zR3VhcmFudGVlLTEsUGVybWlzc2lvbnNTYWxhcnlUcmFuc2FjdGlvbi0xLFBlcm1pc3Npb25zQ29udGFjdC0xLFBlcm1pc3Npb25zRmluYW5jZS0xLFBlcm1pc3Npb25zUGF5bWVudFJlY2VpcHQtMSxQZXJtaXNzaW9uc0NvbnRyYWN0LTEsUGVybWlzc2lvbnNDb250cmFjdFByb2ZpbGUtMSxQZXJtaXNzaW9uc0NvbnRyYWN0VGVtcGxhdGUtMSxQZXJtaXNzaW9uc0xldHRlclRlbXBsYXRlLTEsUGVybWlzc2lvbnNQYXltZW50VGVybS0xLFBlcm1pc3Npb25zTGV0dGVyLTEsUGVybWlzc2lvbnNMZXR0ZXJQcm9maWxlLTEsUGVybWlzc2lvbnNBcHBseUZvcm0tMSxQZXJtaXNzaW9uc1N1cnZleUZvcm0tMSxQZXJtaXNzaW9uc1Byb2Nlc3MtMSxQZXJtaXNzaW9uc1Byb2Nlc3NKb3VybmV5LTEsUGVybWlzc2lvbnNVc2VyVHJlZS0xLFBlcm1pc3Npb25zUmVwb3J0LTEsUGVybWlzc2lvbnNGYWlsZWRBbmRTdWNjZWVkZWROZWdvdGlhdGlvbnNSZXBvcnQtMSxQZXJtaXNzaW9uc1NhbGVJbnZvaWNlc1JlcG9ydC0xLFBlcm1pc3Npb25zU2VsbGVyc1JlcG9ydC0xLFBlcm1pc3Npb25zTWVldGluZ3NDYWxlbmRlci0xLFBlcm1pc3Npb25zUGVyc29uNzY3LFBlcm1pc3Npb25zUGVyc29uUHJvZmlsZS0xLFBlcm1pc3Npb25zQ29tcGFueTc2NyxQZXJtaXNzaW9uc0NvbXBhbnlQcm9maWxlLTEsUGVybWlzc2lvbnNDb250YWN0U3VwcG9ydExldmVsLTEsUGVybWlzc2lvbnNJbnZvaWNlSXNzdWFuY2VBdXRvQnBtc1NldHRpbmctMSxQZXJtaXNzaW9uc1ZvaXBTZXR0aW5nLTEsUGVybWlzc2lvbnNOZWdvdGlhdGlvblNldHRpbmctMSxQZXJtaXNzaW9uc0VtYWlsLTEsUGVybWlzc2lvbnNFbWFpbENvbmZpZy0xLFBlcm1pc3Npb25zSW50ZXJuYWxpemF0aW9uLTEsUGVybWlzc2lvbnNDaGFuZ2VQYXNzd29yZC0xLFBlcm1pc3Npb25zQXV0b21hdGljTWVzc2FnZVNldHRpbmctMSxQZXJtaXNzaW9uc01hc3NTbXMtMSxQZXJtaXNzaW9uc0xvZ3MtMSxQZXJtaXNzaW9uc0J1c2luZXNzUHJvY2Vzcy0xLFBlcm1pc3Npb25zQnVzaW5lc3NQcm9jZXNzUHJvZmlsZS0xLFBlcm1pc3Npb25zUHJvY2Vzc1R5cGUtMSxQZXJtaXNzaW9uc1Byb2Nlc3NMZXZlbC0xLFBlcm1pc3Npb25zUmVtaW5kZXJUYXNrLTEsUGVybWlzc2lvbnNXYXJlaG91c2UtMSxQZXJtaXNzaW9uc1Byb2R1Y3QtMSxQZXJtaXNzaW9uc0JhcmNvZGVTZXR0aW5nLTEsUGVybWlzc2lvbnNQcm9kdWN0UHJvZmlsZS0xLFBlcm1pc3Npb25zUHJvZHVjdENhdGVnb3J5LTEsUGVybWlzc2lvbnNJbnZvaWNlNzY3OSxQZXJtaXNzaW9uc0ludm9pY2VQcm9maWxlLTEsUGVybWlzc2lvbnNOZWdvdGlhdGlvbjEyNyxQZXJtaXNzaW9uc05lZ290aWF0aW9uUHJvZmlsZS0xLFBlcm1pc3Npb25zUHJvZHVjdFVuaXQtMSxQZXJtaXNzaW9uc1dvcmtGaWVsZC0xLFBlcm1pc3Npb25zTWVldGluZ1Jvb20tMSxQZXJtaXNzaW9uc0ludGVyYWN0aW9uVHlwZS0xLFBlcm1pc3Npb25zQ29tbWlzc2lvblNldHRpbmctMSxQZXJtaXNzaW9uc0NvbW1pc3Npb24tMSxQZXJtaXNzaW9uc0ZpZWxkU2V0dGluZy0xLFBlcm1pc3Npb25zQ29udGFjdFJvbGUtMSxQZXJtaXNzaW9uc0NvbnRhY3RQZXJzb24tMSxQZXJtaXNzaW9uc0NvbnRhY3RDb21wYW55LTEsUGVybWlzc2lvbnNJZGVudGl0eUNvbnRhY3QtMSxQZXJtaXNzaW9uc1BheW1lbnRHYXRld2F5LTEsUGVybWlzc2lvbnNTZXBpZGFyU2VydmljZS0xLFBlcm1pc3Npb25zU2VydmljZUxpbmVOdW1iZXItMSxQZXJtaXNzaW9uc1Ntc1RlbXBsYXRlLTEsUGVybWlzc2lvbnNQaG9uZUNhbGxDdXN0b21Qcm9wZXJ0eS0xLFBlcm1pc3Npb25zU2VsbGVyQWN0aXZpdGllcy0xIiwiQ3VzdG9tZXJJZCI6IjEyMDEiLCJDdXN0b21lciI6ImtpYW5hIiwiUm9sZSI6ImtpYW5hLUFkbWluc3RyYXRvciIsImp0aSI6IjZGODgwRkVERjhGRkYwMDk3MEEwMTYyMjNEQTdENDYyIiwiaWF0IjoxNzE4MTE0MTkwLCJzY29wZSI6WyJhc2FuaXRvIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbInBhc3N3b3JkIl19.Ri_daAGuo94PNXb7fpdnezFPDSn8kDdjXJGMjyNOu9yFCiE_lAoYxmW6u2PbARvlSsUiWCAAB-KU3zdMCnNqDikDIEtgdVrqeL2xeBACcumdWHWWleCWxF8VcatW8rc6vZ5pWf5hDR91MXyg-BxYzlnPBxl7w1Xb_EKmaqGraHqPPIE1kJWd9HUswu1QK4abhJmZv2KCdTBK6uo4ZBXhTIiSIaf6cEHm0G-hEFmrUWwH8i5A88Df3wzKtxZYu3LNm2OC610f-H9HrkjwZasbNdcyTFRZ5rPVdh-Lgisb1gdb0kMwt497zqL0M05AiexZITJRsVOWCl9ezBmnzpdI-Q"

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
                    "description": "reminder date. by default set the reminder date for tomorrow morning. make sure you format the date like this: %Y-%m-%dT%H:%M. e.g. 2024-03-20T00:00",
                },
                "dueDate": {
                    "type": "string",
                    "description": "due date. optional. make sure you format the date like this: %Y-%m-%dT%H:%M. e.g. 2024-03-20T00:00",
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
                  "dueDate": None,
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
      
