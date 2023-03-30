import tiktoken
import struct
import time

# Load the encoding for the model
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Define the path to the encoded file
input_file = input("file to decode?")

# Read the encoded input from the file
with open(input_file, "rb") as f_in:
    # Read the packed binary data from the file
    packed_input = f_in.read()
    
    # Unpack the binary data into a list of integers
    unpacked_input = struct.unpack('>' + 'I'*(len(packed_input)//4), packed_input)
    
    # Decode the list of integers into a string of text
    decoded_input = encoding.decode(unpacked_input)
    
    # Print the decoded input
    with open("out_%d.bin" % int(time.time()), "w") as f_out:
        f_out.write(decoded_input)
