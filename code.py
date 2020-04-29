import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"] 
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"] 
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми", "неожиданного праздника", "приятных перемен"]

generated_prophecies = []

i = 0
while i < 5:
    timeIndex = random.choice(times)
    advicesIndex = random.choice(advices)
    promisesIndex = random.choice(promises)
    generated_prophecies.append(times[timeIndex].title() + " " + advices[advicesIndex] + " " + promises[promisesIndex] + ".")
    i = i + 1
print (generated_prophecies)

