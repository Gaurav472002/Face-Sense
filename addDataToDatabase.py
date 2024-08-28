import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://facesense-77eb7-default-rtdb.firebaseio.com/"
})

ref = db.reference('students')

data = {
    "772223":
        {
            "name": "Vimdhayak Jee",
            "major": "C++",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "1",
            "year": 5,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
   


}

for key, value in data.items():
    ref.child(key).set(value)
