# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import wikipedia


# %%
tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")


# %%
def Sum(title):
    ny = wikipedia.page(title)
    text = ny.content
    tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
    summary = model.generate(**tokens)
    print(tokenizer.decode(summary[0]))


# %%
while(True):
    try:
        title = input("Enter Topic to Summarize or Type e to exit \n")
        if title == "e":
            print("thank you for use me")
            break
        Sum(title)
    except:
        raise("no Valid Search try Again")
        continue


