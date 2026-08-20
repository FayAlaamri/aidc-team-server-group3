import time
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL = "HuggingFaceTB/SmolLM2-135M-Instruct"
PATH = "/generate"

tok = AutoTokenizer.from_pretrained(MODEL, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(MODEL, local_files_only=True)

def handle():
    messages = [{"role": "user", "content": "In one sentence, what is a data centre for?"}]
    ids = tok.apply_chat_template(messages, tokenize=False,  add_generation_prompt=True)
    inputs = tok(ids, return_tensors="pt")
    
    t0 = time.perf_counter()
    out = model.generate(**inputs, max_new_tokens=40, do_sample=False)
    dt = time.perf_counter() - t0
    
    n = out.shape[-1] - inputs["input_ids"].shape[-1]
    
    return {
        "model": MODEL, 
        "sample": tok.decode(out[0][input_length:],skip_special_tokens=True).strip(),
        "seconds": round(dt, 2), 
        "tokens_per_sec": round(n / dt, 1)
    }
