import re
import random

# owoification code taken from
# https://gist.github.com/jtvjan/1308479db62d6132d80b0180bcbff08f

faces=["(・`ω´・)",";;w;;","owo","UwU",">w<","^w^"];

def _repl_1(m):
    return f"ny{m.group(1)}"

def _repl_2(m):
    return f"Ny{m.group(1)}"

def owoify(text):
    text = re.sub('(?:r|l)', "w", text)
    text = re.sub('(?:R|L)', "W", text)
    text = re.sub('n([aeiou])', _repl_1, text);
    text = re.sub('N([aeiou])', _repl_2, text);
    text = re.sub('N([AEIOU])', _repl_2, text);
    text = re.sub('ove', "uv", text)
    text = re.sub('\!+', f"! {random.choice(faces)}", text)
    return text
