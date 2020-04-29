import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"] 
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"] 
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми", "неожиданного праздника", "приятных перемен"]

generated_prophecies = []

i = 0
while i < 5:
    timeIndex = random.randrange(0, len(times))
    advicesIndex = random.randrange(0, len(advices))
    promisesIndex = random.randrange(0, len(promises))
    generated_prophecies.append(times[timeIndex].title() + " " + advices[advicesIndex] + " " + promises[promisesIndex] + ".")
    i = i + 1
print (generated_prophecies)

