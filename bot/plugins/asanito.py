
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
        with open('AddLeanWithApi.json', encoding='utf-8') as f:
            data = json.load(f) 
        data[0]["name"] = kwargs["name"]
        data[0]["lastName"] = kwargs["lastName"]
        data[0]["mobiles"] = [kwargs["mobiles"]]
        if "genderID" in kwargs:
            data[0]["genderID"] = kwargs["genderID"]    
        with open('headers.json', encoding='utf-8') as h:
            headers = json.load(h)  
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return {'message': 'Data posted successfully!'}
        else:
            return {'error': 'Error posting data'}