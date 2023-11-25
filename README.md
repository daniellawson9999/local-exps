## Setup

Using Python bindings (https://github.com/abetlen/llama-cpp-python) for llama.cpp (https://github.com/ggerganov/llama.cpp). Can run LMs quickly on just CPU, or with offloading some layers to GPU. 

Requirements listed in `requirements.txt` or can follow instructions for https://github.com/abetlen/llama-cpp-python for specific installation. 

## Server Instructions
Can run locally as described, e.g. in test.py, or can use built in web server which "acts as a drop-in replacement for OpenAI's API:
```bash 
python3 -m llama_cpp.server --model ~/scratch/llama-2-7b-chat.Q4_K_M.gguf --chat_format chatml --host 0.0.0.0
```
Where `--host 0.0.0.0` allows for remote connection. 


## Model setup / Lawson servers
I've had success running inference from models hosted on Lawson's servers. 
- 7B models fast enough to download, seems to get about 6-7 tokens/sec, e.g. download https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF, specifically I tested https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf. 
- Can be replaced w/ any other model in GGUF, TheBloke has a lot of models converted. Also ran inference for 70B LLMs on mc21 but pretty slow. 
- We have disk quota, but can be avoided by downloading to scratch, `cd ~/scratch && wget [url]`, then point server to this folder. 

## Making requests
Example in client.py. We can simply use the openai python library, just need to change the base_url to point to our model. This should work as long as your computer is connected to Purdue's wifi or connected via the Purdue VPN. 
```python
client = OpenAI(base_url="http://mc21.cs.purdue.edu:8000/v1", api_key="sk-xxx")
```
in the above case, I ran the model on mc21, can swap w/ https://www.cs.purdue.edu/resources/facilities/lwsnservers.html. 
```bash
python client.py --host=mc21.cs.purdue.edu
```

Various features of the OpenAI API are implemented in python-llama-cpp, for example, 

## Models
Testing models for fun:
- https://huggingface.co/TheBloke/OpenHermes-2.5-Mistral-7B-GGUF

## Ideas
- Benchmark networking performance of streaming vs sending final response