
from typing import Dict
from .plugin import Plugin
import requests
import json


class AsanitoPlugin(Plugin):
    """
    A plugin to add, modify or view data in asanito CRM.
    """

    def get_source_name(self) -> str:
        return "asanito"    
    
    
    
    def get_spec(self) -> [Dict]:
        return [{
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
                        "description": "Phone number of the person",
                    },
                    "genderID": {
                        "type": "number",
                        "description": "Gender of the person. Write 1 for male, 2 for female, and 3 when the gender is unknown. Try guessing the gender based on the given name by user",
                    }
                },
                "required": ["name", "lastName", "mobiles"],
            },
        }]  
        
        
        
    async def execute(self, function_name, helper, **kwargs) -> Dict:
        url = 'https://clouddevbak.asanito.app/api/asanito/Person/AddLeanWithApi'   
        # with open('AddLeanWithApi.json', encoding='utf-8') as f:
        #     data = json.load(f) 
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
            
            
            
        headers = {
	    "accept": "application/json, text/plain, */*",
	    "accept-language": "en-US,en;q=0.9,fa;q=0.8",
	    "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjU1NTAwMkQyQjU4M0NBMjc2QUQ4Qzk0MkEyQTQ5NTRDIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE3MTQ1NTcxMjksImV4cCI6MTcxNzE0OTEyOSwiaXNzIjoiaHR0cDovL2lkZW50aXR5YXBpLXNlcnZpY2U6ODAwMyIsImF1ZCI6ImFzYW5pdG8iLCJjbGllbnRfaWQiOiJhc2FuaXRvQ2xpZW50Iiwic3ViIjoiMjI5NCIsImF1dGhfdGltZSI6MTcxNDU1NzEyOSwiaWRwIjoibG9jYWwiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ3b29kc3RvcmUtMDkwMTc1Mzk1MDgiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjM3MCIsInVzZXJJZCI6IjM3MCIsInBlcm1pc3Npb25zIjoiUGVybWlzc2lvbnNEYXNoYm9hcmRDb250ZW50LTEsUGVybWlzc2lvbnNGaW5hbmNpYWxDaGFydC0xLFBlcm1pc3Npb25zRmluYW5jZVJlcG9ydC0xLFBlcm1pc3Npb25zVXNlcnMtMSxQZXJtaXNzaW9uc1N0YXRpb24tMSxQZXJtaXNzaW9uc0FjcXVhaW50aW5nVHlwZS0xLFBlcm1pc3Npb25zUHJpY2VVbml0LTEsUGVybWlzc2lvbnNKb2JQb3NpdGlvbi0xLFBlcm1pc3Npb25zTmljTmFtZVRpdGxlLTEsUGVybWlzc2lvbnNTb2NpYWxUeXBlLTEsUGVybWlzc2lvbnNWb2lwTnVtYmVyLTEsUGVybWlzc2lvbnNQaG9uZUNhbGxTdWJqZWN0LTEsUGVybWlzc2lvbnNSb2xlLTEsUGVybWlzc2lvbnNGdW5uZWwtMSxQZXJtaXNzaW9uc0Z1bm5lbExldmVsLTEsUGVybWlzc2lvbnNPcmdhbml6YXRpb24tMSxQZXJtaXNzaW9uc0JhbmstMSxQZXJtaXNzaW9uc0JhbmtBY2NvdW50LTEsUGVybWlzc2lvbnNCYW5rQWNjb3VudFByb2ZpbGUtMSxQZXJtaXNzaW9uc0JhbmtDaGFjay0xLFBlcm1pc3Npb25zUHJvcGVydHlHcm91cC0xLFBlcm1pc3Npb25zUHJvcGVydHktMSxQZXJtaXNzaW9uc09wZXJhdGluZ0luY29tZS0xLFBlcm1pc3Npb25zT3BlcmF0aW5nSW5jb21lUHJvZmlsZS0xLFBlcm1pc3Npb25zTm9uT3BlcmF0aW5nSW5jb21lLTEsUGVybWlzc2lvbnNOb25PcGVyYXRpbmdJbmNvbWVQcm9maWxlLTEsUGVybWlzc2lvbnNDb3N0R3JvdXAtMSxQZXJtaXNzaW9uc0Nvc3RUeXBlLTEsUGVybWlzc2lvbnNJbnRlcm5hbEJhbmtBY2NvdW50VHJuc2FjdGlvbi0xLFBlcm1pc3Npb25zSW50ZXJuYWxCYW5rQWNjb3VudFRybnNhY3Rpb25Qcm9maWxlLTEsUGVybWlzc2lvbnNMb2FuLTEsUGVybWlzc2lvbnNDb3N0LTEsUGVybWlzc2lvbnNDb3N0UHJvZmlsZS0xLFBlcm1pc3Npb25zUHVyY2hhc2luZ0Nvc3QtMSxQZXJtaXNzaW9uc1B1cmNoYXNpbmdDb3N0UHJvZmlsZS0xLFBlcm1pc3Npb25zU2hhcmVIb2xkZXItMSxQZXJtaXNzaW9uc1NoYXJlSG9sZGVyVHJhbnNhY3Rpb24tMSxQZXJtaXNzaW9uc0d1YXJhbnRlZS0xLFBlcm1pc3Npb25zU2FsYXJ5VHJhbnNhY3Rpb24tMSxQZXJtaXNzaW9uc0NvbnRhY3QtMSxQZXJtaXNzaW9uc0ZpbmFuY2UtMSxQZXJtaXNzaW9uc1BheW1lbnRSZWNlaXB0LTEsUGVybWlzc2lvbnNDb250cmFjdC0xLFBlcm1pc3Npb25zQ29udHJhY3RQcm9maWxlLTEsUGVybWlzc2lvbnNDb250cmFjdFRlbXBsYXRlLTEsUGVybWlzc2lvbnNMZXR0ZXJUZW1wbGF0ZS0xLFBlcm1pc3Npb25zUGF5bWVudFRlcm0tMSxQZXJtaXNzaW9uc0xldHRlci0xLFBlcm1pc3Npb25zTGV0dGVyUHJvZmlsZS0xLFBlcm1pc3Npb25zQXBwbHlGb3JtLTEsUGVybWlzc2lvbnNTdXJ2ZXlGb3JtLTEsUGVybWlzc2lvbnNQcm9jZXNzLTEsUGVybWlzc2lvbnNQcm9jZXNzSm91cm5leS0xLFBlcm1pc3Npb25zVXNlclRyZWUtMSxQZXJtaXNzaW9uc1JlcG9ydC0xLFBlcm1pc3Npb25zTWVldGluZ3NDYWxlbmRlci0xLFBlcm1pc3Npb25zUGVyc29uNzY3LFBlcm1pc3Npb25zUGVyc29uUHJvZmlsZS0xLFBlcm1pc3Npb25zQ29tcGFueTc2NyxQZXJtaXNzaW9uc0NvbXBhbnlQcm9maWxlLTEsUGVybWlzc2lvbnNDb250YWN0U3VwcG9ydExldmVsLTEsUGVybWlzc2lvbnNJbnZvaWNlSXNzdWFuY2VBdXRvQnBtc1NldHRpbmctMSxQZXJtaXNzaW9uc05lZ290aWF0aW9uTGV2ZWxDaGFuZ2VDb250cm9sU2V0dGluZy0xLFBlcm1pc3Npb25zRW1haWwtMSxQZXJtaXNzaW9uc0VtYWlsQ29uZmlnLTEsUGVybWlzc2lvbnNJbnRlcm5hbGl6YXRpb24tMSxQZXJtaXNzaW9uc0RlZmF1bHRGdW5uZWwtMSxQZXJtaXNzaW9uc0NoYW5nZVBhc3N3b3JkLTEsUGVybWlzc2lvbnNBdXRvbWF0aWNNZXNzYWdlU2V0dGluZy0xLFBlcm1pc3Npb25zTWFzc1Ntcy0xLFBlcm1pc3Npb25zTG9ncy0xLFBlcm1pc3Npb25zQnVzaW5lc3NQcm9jZXNzLTEsUGVybWlzc2lvbnNCdXNpbmVzc1Byb2Nlc3NQcm9maWxlLTEsUGVybWlzc2lvbnNQcm9jZXNzVHlwZS0xLFBlcm1pc3Npb25zUHJvY2Vzc0xldmVsLTEsUGVybWlzc2lvbnNSZW1pbmRlclRhc2stMSxQZXJtaXNzaW9uc1dhcmVob3VzZS0xLFBlcm1pc3Npb25zUHJvZHVjdC0xLFBlcm1pc3Npb25zQmFyY29kZVNldHRpbmctMSxQZXJtaXNzaW9uc1Byb2R1Y3RQcm9maWxlLTEsUGVybWlzc2lvbnNQcm9kdWN0Q2F0ZWdvcnktMSxQZXJtaXNzaW9uc0ludm9pY2U3Njc5LFBlcm1pc3Npb25zSW52b2ljZVByb2ZpbGUtMSxQZXJtaXNzaW9uc05lZ290aWF0aW9uMTkxLFBlcm1pc3Npb25zTmVnb3RpYXRpb25Qcm9maWxlLTEsUGVybWlzc2lvbnNQcm9kdWN0VW5pdC0xLFBlcm1pc3Npb25zV29ya0ZpZWxkLTEsUGVybWlzc2lvbnNNZWV0aW5nUm9vbS0xLFBlcm1pc3Npb25zRmFpbGVkQW5kU3VjY2VlZGVkTmVnb3RpYXRpb25zUmVwb3J0LTEsUGVybWlzc2lvbnNTYWxlSW52b2ljZXNSZXBvcnQtMSxQZXJtaXNzaW9uc1NlbGxlcnNSZXBvcnQtMSxQZXJtaXNzaW9uc05lZ290aWF0aW9uU2V0dGluZy0xLFBlcm1pc3Npb25zVm9pcFNldHRpbmctMSxQZXJtaXNzaW9uc0ludGVyYWN0aW9uVHlwZS0xLFBlcm1pc3Npb25zQ29tbWlzc2lvblNldHRpbmctMSxQZXJtaXNzaW9uc0NvbW1pc3Npb24tMSxQZXJtaXNzaW9uc0ZpZWxkU2V0dGluZy0xLFBlcm1pc3Npb25zSWRlbnRpdHlDb250YWN0LTEsUGVybWlzc2lvbnNQYXltZW50R2F0ZXdheS0xLFBlcm1pc3Npb25zU2VwaWRhclNlcnZpY2UtMSIsIkN1c3RvbWVySWQiOiIxMDk2IiwiQ3VzdG9tZXIiOiJ3b29kc2hvcGEiLCJSb2xlIjoid29vZHN0b3JlLUFkbWluc3RyYXRvciIsImp0aSI6IjczRTUzQThGRUU3MDFDNUFEQzY5MEZGQTk1ODg1MkQ1IiwiaWF0IjoxNzE0NTU3MTI5LCJzY29wZSI6WyJhc2FuaXRvIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbInBhc3N3b3JkIl19.JOeGkTGYiwcSc9OtiFvOpWPR4ffGsndyNuQDDTp9GP8dO8AddAshlQVx11_DR37BKzDgDTkG5FcdRQfjcpMSPjjsBe1nHrsZpneg_2ty9ot1IH2DJQbWhBLNs6MBUIezxipHhK7RucKU3ImROZ1_9B2U5sqySOghIwFR7ghS7eFHFfCrzgDvgLhXhF30hrbdflPKUoGFQi3bmVhgVt3wps-5Jnh5Jd-5l8orRirBC_pxB9yD2iesg_fQLDloTysTtCiYGm14aeDOImoRuF5Rog-jxBD2y7HqXEFYjf5NvErLKMvJJTMGGj2qEmcAXOgnvs7W9DdPuTGQWYB6HuUOkw", 
	    "content-type": "application/json",
	    "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
	    "sec-ch-ua-mobile": "?0",
	    "sec-ch-ua-platform": "\"Windows\"",
	    "sec-fetch-dest": "empty",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-site": "same-site"
        }
        
        # with open('headers.json', encoding='utf-8') as h:
        #     headers = json.load(h)  
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return {'message': 'Data posted successfully!'}
        else:
            return {'error': 'Error posting data'}