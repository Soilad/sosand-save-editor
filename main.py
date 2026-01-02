import pickle

inp = 0


class Faction:
    def __init__(a):
        print()


class Country:
    def __init__(a):
        print()


class Division:
    def __init__(a):
        print()

print("SOSAND Save Editor")
print("By Tumblr sexyman Soilad")

file = input("select file to edit")
with open(file, "rb") as f:
    example = pickle.load(f)
    print(example)
    country = list(example)[0]
    # example["controlledCountry"] = "Armenia"

    while inp != "exit":
        inp = input(f"[{country}] >").split()
        if file not in ("worldData"):
            members = sorted(list(example[country].__dict__))
            match inp[0]:
                case "list":
                    print(sorted(list(example)))
                case "select":
                    if inp[1] in list(example):
                        country = inp[1]
                case "properties":
                    members = sorted(list(example[country].__dict__.keys()))
                    print(members)
                case "get":
                    if inp[1] in members:
                        print(example[country].__dict__[inp[1]])
                case "set":
                    if inp[1] in members and (
                        type(example[country].__dict__[inp[1]]) is type(eval(inp[2]))
                    ):
                        example[country].__dict__[inp[1]] = eval(inp[2])
                case "move":
                    example[inp[1]] = example[country]
                    del example[country]
                    country = inp[1]
                case "delete":
                    del example[country]
                case "write":
                    with open(f"{file}2", "wb") as handle:
                        pickle.dump(example, handle, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            members = list(example)
            match inp[0]:
                case "list":
                    print(example)
                case "select":
                    country = inp[1]
                case "set":
                    if type(example[country]) is type(eval(inp[1])):
                        print("a")
                        example[country] = eval(inp[1])
                case "write":
                    with open(f"{file}2", "wb") as handle:
                        pickle.dump(example, handle, protocol=pickle.HIGHEST_PROTOCOL)
        # example["Chechnya"] = example["Bharatiya"]
        # # example["Chechnya"].color = (250, 250, 205)
        # print(members)
        # example["Bharatiya"].atWarWith.append("Indian_Empire")
        # print(len(example["Bharatiya"].regions))
        # # print(example["Bharatiya"].name)
        # example["Bharatiya"].name = "Chechnya"
        # # example["Bharatiya"].decisionTree["Political Effort"][8] = "wazdorf"
        # # print(example["Bharatiya"].decisionTree["Political Effort"][8])
        # example["Bharatiya"].ideologyName = "accelerationist"
