from datetime import datetime

import datetime

dtToday = datetime.datetime.now()
dtCabos = datetime.datetime(2022, 9, 23)
  
diference = dtCabos-dtToday

if diference.days != 0:
    print(f"NO 😭 FALTEN {diference.days} DIES")
else: 
    print("WE CABOOOOOS!!!! 🥳🎉 #wecabos")