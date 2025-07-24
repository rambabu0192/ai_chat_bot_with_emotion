from transformers import pipeline, Conversation

# Use DialoGPT for conversation
# chatbot_pipeline = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# Use GPT-2 for conversation
#chatbot_pipeline = pipeline("text-generation", model="distilgpt2")

# conversation
chatbot_pipeline = pipeline("conversational")

def generate_response(prompt):
    conversation = Conversation(prompt)
    response = chatbot_pipeline(conversation, max_length=100, pad_token_id=50256)
    # print(response[1]['content'])
    # print(type(response))
    return response[1]['content']


# Test the chatbot
# prompt = "Tell me a joke"
# response = generate_response(prompt)
# print(response)



