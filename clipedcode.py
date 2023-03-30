import tiktoken

# Load the encoding for the model
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Loop infinitely to encode user input
while True:
    # Get user input
    user_input = input()
    
    # Encode the input using the loaded encoding
    encoded_input = encoding.encode(user_input)
    
    # Convert the encoded input to a string of Unicode characters
    temp = ""
    for x in encoded_input:
        temp += chr(x)
        
    # Print the encoded input as a string of Unicode characters
    print(temp)
