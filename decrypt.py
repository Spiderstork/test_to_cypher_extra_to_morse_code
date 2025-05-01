def flip(message):
    new_message = str()
    for n in message:
        new_message = n + new_message
    return new_message


def cyper(message, shift):
    new = str()

    for n in message:
        n = ord(n)
        if n<=122 and n>=97:
            for num in range(shift):
                n -= 1
                if n < 97:
                    n = 122

        n = chr(n)
        new += n

    return new

def morse(message, morse_code_dict ):
    new = str()
    message = message.split()
    for n in message:
        try:
            new += morse_code_dict[n]
        except:
            new += n



    return new


morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '|': ' ', " ": ""
}


##########################################################
shift = 1

#
# menu for user
#
print("un-decrypt")
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
    for n in range(26):
        decrypted_message = cyper(message.lower(), shift)
        print(decrypted_message)
        shift += 1

elif user == "3":
    print("message: ")
    message = input(">").upper()

    flipped_message = flip(message)

    morse_message = morse(flipped_message, morse_code_dict)

    for n in range(26):
        decrypted_message = cyper(morse_message.lower(), shift)
        print(decrypted_message)
        shift += 1