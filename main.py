import sys

cz_abc = ["ě","š","č","ř","ž","ý","á","í","é","ú","ů","ó","ň","ť","ď","q","w","e","r","t","z","u","i","o","p","a","s","d","f","g","h","j","k","l","y","x","c","v","b","n","m","Ě","Š","Č","Ř","Ž","Ý","Á","Í","É","Ú","Ů","Ó","Ň","Ť","Ď","Q","W","E","R","T","Z","U","I","O","P","A","S","D","F","G","H","J","K","L","Y","X","C","V","B","N","M"," ","1","2","3","4","5","6","7","8","9",".",",","!","?","@",":","/"]
# (DE/ZA)KÓDOVÁNÍ
def cipher(decipher=False, fraze = None):
	if fraze == None: fraze = input("Věta na dekódování: ") if decipher else input("Věta na zakódování: ")
	posun = input("Číselný kód pro posun: ")
	print("----------------------------------------------------")
	if posun.isnumeric() == False:
		print("Používej prosím pouze čísla! Použil jsi:", posun)
		return None
	else:
		posun = int(posun)
	for char in fraze:
		if char in cz_abc:
			order = ((cz_abc.index(char)+1)-posun)%len(cz_abc) if decipher else ((cz_abc.index(char)+1)+posun)%len(cz_abc) # +1 musi byt protoze kdyz by bylo len()%len()=0 ale ma to byt len()
			print(cz_abc[order-1], end="")

		else:
			print(char, end="")
	print("\n")

# DEKÓDOVÁNÍ (Bruteforce)

def decipherbrute(fraze=None):
	if fraze == None: fraze = input("Věta na dekódování: ")
	print("----------------------------------------------------")
	for posun in range(len(cz_abc)):
		print(posun," - ", end="", flush=True)
		for char in fraze:
			if char in cz_abc:
				order = ((cz_abc.index(char)+1)+posun)%len(cz_abc) # +1 musi byt protoze kdyz by bylo len()%len()=0 ale ma to byt len()
				print(cz_abc[order-1], end="")
			else:
				print(char, end="")
		print("\n----------------------------------------------------")
		
# MENU
def menu():
	menutext = """
1 - Zakódování
2 - Dekódování
3 - Dekódování (Bruteforce)
4 - Exit
"""
	print(menutext)
	menuoption = input()
	if menuoption == "1":
		cipher()
	if menuoption == "2":
		cipher(decipher=True)
	elif menuoption == "3":
		decipherbrute()
	elif menuoption == "4":
		sys.exit()
	else:
		print("Zadej prosím správnou možnost")

if __name__ == "__main__":
	menu()
			