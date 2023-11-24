from llama_cpp import Llama
import os
# model_name = 'llama-2-7b.Q5_K_M.gguf'
model_name = 'llama-2-7b-chat.Q4_K_M.gguf'
model_path = os.path.join('models', model_name)
llm = Llama(model_path=model_path, n_gpu_layers=32)
# llm = Llama(model_path=model_path)
max_tokens=512

# import pdb; pdb.set_trace()
# output = llm(
#   "Q: Name the planets in the solar system? A: ", # Prompt
#   max_tokens=32, # Generate up to 32 tokens
#   stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
#   echo=True # Echo the prompt back in the output
# )

prompt = '''Below is an instruction that describes a task. Write a response that appropriately completes the request.
### Instruction:
{}

### Response:
'''

while True:
    question = input("Q: ")
    # import pdb; pdb.set_trace()
    # question = "Q: " + question + " A: "
    input_text = prompt.format(question)
    print(input_text)
    output = llm(question, max_tokens=max_tokens, stop=["Q:",], echo=False) # write a poem about bread
    text = output["choices"][0]["text"]
    # import pdb; pdb.set_trace()
    print(text)
