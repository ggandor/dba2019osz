"""
Házi feladat no. 4: Hímnem-nőnem

A feladat egy olyan függvény írása, amely egy bemeneti stringben kicseréli
az angol hímnemű névmásokat nőneműekre. Azt hiszem, nem kell ragozni :)
"""

def feminize(original_string):
    pass


test_string = "I suggested to him to go and apologize to his Shetland pony and his Sebright hen for his irrational behavior, but he didn't like the idea. He said he cannot bring himself to do that, the animals have to apologize first. Hence, the atmosphere on the farm is still icy."

expected_result = "I suggested to her to go and apologize to her Shetland pony and her Sebright hen for her irrational behavior, but she didn't like the idea. She said she cannot bring herself to do that, the animals have to apologize first. Hence, the atmosphere on the farm is still icy."

if feminize(test_string) == expected_result:
    print(":)")
else:
    print(":(")

