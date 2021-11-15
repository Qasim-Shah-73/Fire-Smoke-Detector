import firebase_admin
from firebase_admin import credentials

##### Fire Base Creditianls ###########
cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred,
                              {
                                  'databaseURL' : 'https://test-58cc9-default-rtdb.firebaseio.com/'
                              })

import window