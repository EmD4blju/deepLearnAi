import asyncio

import modelsMethods as mm

words = ("give and take,"
         "black and white,"
         "again and time,"
         "thick and thin,"
         "high and dry,"
         "go and touch,"
         "fortune and fame,"
         "blood and flesh,"
         "first and foremost,"
         "soul and life")

text = ("a) Jenny promised to live with Nigel through..."
        "b) When Joe was 18 he left home to find..."
        "c) It was ... whether we would get to the airport in time."
        "d) ..., we need to solve the budget problem and then we can move on to other issues."
        "e) ..., we see this pattern of behaviour repeating itself."
        "f) There needs to be a bit of ... in every relationship."
        "g) My brother James is the ... of any family party."
        "h) My aunt treats her relatives really badly, considering they are her own ..."
        "i) When the company closed down I was left ... without a job."
        "j) How could you not understand? Look at this letter - it's all there in...")


prompt = ("You will be given some uncompleted sentences."
          "Your task is to fill in the \'...\' with the given phrases:"
          f"```"
          f"{words}"
          f"```"
          f"One phrase can be used only once."
          f"Uncompleted sentences will be placed below:"
          f"```"
          f"{text}"
          f"```"
          f"return the answers in format (\'sentence letter\', phrase).")

# print(asyncio.run(get_completion(prompt, "gpt-4")))

format = "polish_word=translation"

words = ("drzwi,"
         "drzewo,"
         "telefon,"
         "komputer,"
         "biurko,")

prompt = ("You will be given polish words. "
          "Your task will be translate them into Ukrainian in the following format:"
          f"``` {format} ```"
          "Polish words will be placed below:"
          "```"
          f"{words}"
          "```")

print(asyncio.run(mm.getCompletion(prompt)))