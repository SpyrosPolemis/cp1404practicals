NAME_TO_CODE = {"zomp": "#39a78e", "united nations blue": "#5b92e5", "shocking pink": "#5b92e5",
                "radical red": "#ff355e", "phthalo blue": "#000f89", "alizarin crimson": "#e32636",
                "cadmium yellow": "#fff600", "blue de france": "#318ce7", "international orange": "#ff4f00",
                "british racing green": "#004225"}

colour = input("Enter colour name: ").lower()
if colour in NAME_TO_CODE.keys():
    print(f"{NAME_TO_CODE[colour]}")
else:
    print("Not a valid colour")
