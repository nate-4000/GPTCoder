import tiktoken

# Load the encoding for the model
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Loop infinitely to encode user input
while True:
    # Get user input
    user_input = input()

    temp = []
    for x in user_input:
        temp += [ord(x)]
    
    # Encode the input using the loaded encoding
    encoded_input = encoding.decode(temp)
    
        
    # Print the encoded input as a string of Unicode characters
    print(encoded_input)
