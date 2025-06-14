from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Path to your downloaded model
model_path = "./deepseek-r1-7b"  # Change this to your actual path

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,  # Use FP16 to save memory
    device_map="auto",          # Automatically places layers on available devices
)

# Chat template (DeepSeek uses this format)
def format_chat(prompt):
    return f"User: {prompt}\nAssistant:"

# Chat function
def chat():
    print("DeepSeek-R1 7B Chatbot (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        
        # Format the input
        formatted_input = format_chat(user_input)
        
        # Tokenize
        inputs = tokenizer(formatted_input, return_tensors="pt").to(model.device)
        
        # Generate response
        outputs = model.generate(
            **inputs,
            max_new_tokens=256,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
        
        # Decode and print response
        response = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    chat()
