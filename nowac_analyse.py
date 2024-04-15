import csv

def nowac(corpus):
    freq_dict = {}
    N = 0
    
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    
    with open (corpus, "r", encoding="UTF-8") as infile:
        
        for line in csv.reader(infile, delimiter="\t"):            
            freq, word = line[0].split(maxsplit=1) 

            word = str(word)
            freq = int(freq)
            
            N += freq
            print(f"{freq:2} {word:2}")
            
            if word[0] in consonants:
                if len(word) == 1:
                    if word.lower() in freq_dict.keys():
                        freq_dict[word.lower()] += freq
                    else:
                        freq_dict[word.lower()] = freq
                    continue
                else:
                    if word[1] in consonants:
                        if len(word) == 2:
                            if word.lower() in freq_dict.keys():
                                freq_dict[word.lower()] += freq
                            else:
                                freq_dict[word.lower()] = freq
                            continue    
                        else:
                            if word[2] in consonants:
                                if len(word) == 3:
                                    if word.lower() in freq_dict.keys():
                                        freq_dict[word.lower()] += freq
                                    else:
                                        freq_dict[word.lower()] = freq
                                    continue
                                else:
                                    if word[0:3].lower() in freq_dict.keys():
                                        freq_dict[word[0:3].lower()] += freq
                                    else:
                                        freq_dict[word[0:3].lower()] = freq
                                    continue 
                            else:
                                if word[0:2].lower() in freq_dict.keys():
                                    freq_dict[word[0:2].lower()] += freq
                                else:
                                    freq_dict[word[0:2].lower()] = freq
                                continue            
                    else:
                        if word[0].lower() in freq_dict.keys():
                            freq_dict[word[0].lower()] += freq
                        else:
                            freq_dict[word[0].lower()] = freq
                        continue                  
            else:
                continue

            

    return freq_dict, N

f, N = nowac("nowac-1.1.raw_tokens.lowercase.freq\\nowac_frequency_raw_token.csv")
sorted_by_values = dict(sorted(f.items(), key=lambda x:x[1], reverse=True))
print(sorted_by_values)
print(N)

import pandas as pd

df = pd.DataFrame.from_dict(data=f, orient="index", columns = ["frequency"])
df["percentage"] = df["frequency"].transform(lambda x: x/N)
df.to_csv("nowac-raw-tokens-consonant-clusters.csv")


