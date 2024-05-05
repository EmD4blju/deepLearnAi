import modelsMethods as mm

user_messages = [
  "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal
  "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                 # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
  "我的屏幕在闪烁"                                               # My screen is flashing
]

# for message in user_messages:
#   prompt = f"Identify the language of the following text:  ```{message}```"
#   lang = mm.getCompletion(prompt)
#   print(f"Original message ({lang}): {message}")
#
#   prompt = f"""
#     Translate the following text to English and Deutsch: ```{message}```
#   """
#   print(mm.getCompletion(prompt))


text = f"""
  Yoo Mr.White, wanna cook some meth? We can chill later at my crib.
  - Cap 'n Cook
"""

prompt = f"""
  Translate the following text from slang to a business letter:
  {text}
"""

print(mm.getCompletion(prompt))

data_json = { "resturant employees" :[
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}

prompt = f"""
Translate the following python dictionary from JSON to an HTML \
table with column headers and title: {data_json}
"""

print(data_json)
response = mm.getCompletion(prompt)
print(response)