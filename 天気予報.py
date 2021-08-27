import requests,random,os
os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title 天気予報  AnonMusic7")
print("""
                                                  
                                                  
             ``                                   
      `.     ::     .`                            
      `:-`   ::    -:`                            
       `-.   ``   .-`                             
 `--.`   `.------.``  ``--`                       
  `.-- `-::::::::::-` --.`                        
       ::::::::::::::`                            
....` .::::::::::::::.   `.--::::--.`             
....` .:::::::::::::. `.:::::::::::::-.           
      `::::::::::::` .::::::::::::::::::`         
   `-- `-:::::::::` .::::::::::::::::::::`        
 `:-.`   `.-.`     `::::::::::::::::::::::        
            `.-:::::::::::::::::::::::::::`       
          .:::::::::::::::::::::::::::::::::-.`   
         -:::::::::::::::::::::::::::::::::::::-` 
        .::::::::::::::::::::::::::::::::::::::::.
        -:::::::::::::::::::::::::::::::::::::::::
        -:::::::::::::::::::::::::::::::::::::::::
        `::::::::::::::::::::::::::::::::::::::::-
         `-:::::::::::::::::::::::::::::::::::::- 
           .-:::::::::::::::::::::::::::::::::-`  
              ```````````````````````````````     
                                                                                              
""")


# 取得したAPIキーを入力
# https://home.openweathermap.org/users/sign_up
apiKey = "*******"

baseUrl = "https://api.openweathermap.org/data/2.5/weather?"
 
cityName = input("都市名を入力してください : ") 
 
completeUrl = baseUrl + "appid=" + apiKey + "&q=" + cityName + "&lang=ja"
 
response = requests.get(completeUrl) 
 
cityData = response.json() 
 
if cityData["cod"] != "404": 
    print("-----------------------------------------")
    print("都市名:",cityData["name"])
    print("天気:",cityData["weather"][0]["description"])
    print("現在の気温:",cityData["main"]["temp"] - 273.15,"℃")
    print("最高気温:",cityData["main"]["temp_max"] - 273.15,"℃")
    print("最低気温:",cityData["main"]["temp_min"] - 273.15,"℃")
    print("湿度:",cityData["main"]["humidity"])
    print("気圧:",cityData["main"]["pressure"])
    print("湿度:",cityData["main"]["humidity"])
    print("風速:",cityData["wind"]["speed"])
    print("-----------------------------------------")
    input()
else: 
    print("都市名が見つかりませんでした。") 
    input()