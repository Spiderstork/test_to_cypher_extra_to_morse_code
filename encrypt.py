import datetime

#
# flips message so "ham" would be "mah" used after cyper to make it harder to convert to back
#
def flip(message):
    new_message = str()
    for n in message:
        new_message = n + new_message
    return new_message

#
# cyper message depending on time so it constantly changes
#
def cyper(message):
    new = str()

    # converts time into seconds to be used as the shift number
    current_time = datetime.datetime.now()
    move = current_time.time()
    move = move.hour * 3600 + move.minute * 60 + move.second

    for n in message:
        # changes it to a Unicode
        n = ord(n)
        # keeps inbetween a to z
        if n<=122 and n>=97:
            for num in range(move):
                n += 1
                if n > 122:
                    n = 97
        # changes it back to charter
        n = chr(n)
        new += n

    return new


morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..'," ":"|"}

#
# coverts it morse using the dictionary above
#
def morse(message, morse_code_dict ):
    new = str()
    for n in range(len(message)):
        try:
            new += morse_code_dict[message[n]] + " "
        except:
            new += message[n] + " "

    return new



##########################################################


#
# menu for user
#
print("################")
print("## options:")
print("## 1.morse code")
print("## 2.cyper")
print("## 3.secret message(most secure)")

user = input(">")

if user == "1":
    print("message: ")
    message = input(">").upper()
    morse_message = morse(message, morse_code_dict)
    print("\n morse code: ")
    print(morse_message )

elif user == "2":
    print("message: ")
    message = input(">")
    cypered_message = cyper(message)
    print(cypered_message)

elif user == "3":
    print("message: ")
    message = input(">").upper()

    cypered_message = cyper(message)

    morse_message = morse(cypered_message, morse_code_dict)

    flipped_message = flip(morse_message)

    print("message:\n",flipped_message)

