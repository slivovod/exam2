def song_decoder(text):
    text = text.upper()
    decoded_text = text.replace("WUB", " ")
    correction = " ".join(decoded_text.split())
    return correction

print("select  option: \n1. use pre-written text \n2. enter your own text (number of characters does not exceed 200)")
try:
    way_selector = int(input())
except:
    way_selector = 1

if(way_selector == 1):
    text = "WUBWUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"
elif(way_selector == 2):
    text = input()
print("text:")
print(text)
print("decoded text:")
print(song_decoder(text))