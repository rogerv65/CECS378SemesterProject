# python script that should take in a raw txt file of words 
# that have been accumulated from social media webpages 
# preferably created by the target
import sys

def sorted_by_values(d): # return a sorted dictionary by values descending
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

# give an iterable (containing elements you want to write to file) and a filepath 
# to write values to file in append mode
def write_to_file(txt,filepath):
    with open(filepath, 'a') as file:
        for line in txt:
            file.write(f"{line}\n")

# can edit this function to filter out unnecessary words
def create_wrd_map(filepath):
    word_freq = dict()
    with open(filepath, "r") as file:
        for line in file:
            word = line.strip().lower()
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    return word_freq

# pass wordmap and a filepath to create permutations and write to file
#  writes in append mode
def generate_passwords(wmap, filepath):
    # special_char = set("!","@") # can implement later
    with open(filepath, 'w') as file:
        for wrd in wmap.keys():
            file.write(f"{wrd}\n") #write base word

            for i in range(10): # write all words starting with uppercase and ending with each digit
                upper = wrd[0].upper() + wrd[1:]
                file.write(f"{upper}{i}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2: # arg variables must be correct
        print("Usage: python wordlist_generator.py <path to .txt file>")
        sys.exit(1)

    txt_file_path = sys.argv[1]
    words = create_wrd_map(txt_file_path) # technically could create a set but map to keep track of wordcount
    words = sorted_by_values(words)

    ### see word count of top 50 words
    # for i, pack in enumerate(words.items()):
    #     k , v = pack
    #     print(k,v)
    #     if i >= 50:
    #         break
    
    generate_passwords(words, 'target_wordlist.txt')