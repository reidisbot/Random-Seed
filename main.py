import random
terrain = []
amt = 6 # Set this number as the amount or keep the input
max_number = 6
random.seed(input("Enter a seed: "))
for i in range(amt):
    terrain.append(random.randint(0, max_number))

out = ""
options = {
    "Ground": "🟩",
    "Dirt":   "🟫",
    "Air":    "  "
}
for i in range(amt + 1):
    out = ""
    for ind in range(len(terrain)):
        if terrain[ind] == i:
            out = out + options["Ground"]
        elif terrain[ind] < i:
            out = out + options["Dirt"]
        else:
            out = out + options["Air"]
    print(out)
