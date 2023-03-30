import tiktoken
import time
import struct

# Load the encoding for the model
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Get the current Unix time
unix_time = int(time.time())

# Define the input and output file paths
input_file = input("file to encode?")
output_file = "encoded_file_{}.gpten".format(unix_time)

# Encode the input file and write the output to the new file
with open(input_file, "r") as f_in, open(output_file, "wb") as f_out:
    # Encode the input using the loaded encoding
    encoded_input = encoding.encode(f_in.read())
    
    # Convert the encoded input to a bytes object
    packed_input = struct.pack('>' + 'I'*len(encoded_input), *encoded_input)
    
    # Write the encoded input as binary data to the output file
    f_out.write(packed_input)
