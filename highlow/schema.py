call_schema = {
    "type" : "object",
    "properties" : {
        "data" : { 
            "type" : "object",
            "properties" : {
                "guess" : {
                    "type" : "string",
                    "pattern" : "^high|low$"
                }
            }
        }
    }
}