def xor(a,b):
    result = ''
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result

def crc_ccitt(message,generator):
    padded_message = message + '0' * (len(generator)-1)
    remainder = padded_message
    while len(remainder) >= len(generator):
        if remainder[0] == '1':
            remainder = xor(remainder[:len(generator)],generator)+remainder[len(generator):]
        else:
            remainder = remainder[1:]
    return remainder

def sender():
    message = input("Enter message in bits: ")
    generator = input("Enter generator: ")
    checksum = crc_ccitt(message,generator)
    print("Checksum code:",checksum)
    return message,checksum,generator

def receiver(message,checksum,generator):
    input_checksum = checksum
    test_message = message+input_checksum
    validity = crc_ccitt(test_message, generator)
    print("message received : ",test_message)
    print("receiver side checksum :",validity)

    if validity == '0' * (len(generator) - 1):
        print("Data is valid.")
    else:
        print("Data is invalid.")

def main():
    print("Sender : ")
    message , checksum , generator = sender()

    print("\nReceiver:")
    receiver(message,checksum,generator)

if __name__ == "__main__":
    main()