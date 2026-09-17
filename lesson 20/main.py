from fastapi import FastAPI



app= FastAPI()

@app.get("/")

def root():
    return {
  "name":"Alice",
  "age":35,
  "address":{
    "street":"papshko vasa",
    "city":"prishtine",
    "country":"Kosove"
  },
  "contacts":[
    {
      "type":"email",
      "vaule":"donjeta@gmail.com"
    },
    {
      "type":"phone",
      "value":"555-123-4567"
    }
  ]
}


@app.get("/users")
def read_root():
  return {
    "message":"Hello There"
  }





































