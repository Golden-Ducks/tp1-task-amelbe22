# Documents
D1 = "I love cats"
D2 = "Cats are chill"
D3 = "I am late"

# Your Task: implement context window vectorization
# with window size = 1 (so each window is 3 tokens wide)
# Use <s> and </s> padding flags

def add_padding(tokens):
    return ["<s>"] + tokens + ["</s>"]


def extract_windows(tokens, window_size=1):
    windows = []
    k = 2 * window_size + 1

    for i in range(len(tokens) - k + 1):
        window = tokens[i:i+k]
        windows.append(" ".join(window))

    return windows

def build_vocab(all_windows):
    vocab = sorted(set(all_windows))
    vocab_index = {w:i for i,w in enumerate(vocab)}
    return vocab_index

def vectorize_doc(doc_windows, vocab):
    vector = [0]*len(vocab)

    for w in doc_windows:
        if w in vocab:
            vector[vocab[w]] = 1

    return vector

# Run
all_docs = [D1, D2, D3]
docs_windows = []
all_windows = []

for doc in all_docs:

    tokens = doc.lower().split()

    padded = add_padding(tokens)

    windows = extract_windows(padded, window_size=1)

    docs_windows.append(windows)

    all_windows.extend(windows)


# Build vocab
vocab = build_vocab(all_windows)

print("Vocabulary:")
for k,v in vocab.items():
    print(v, ":", k)


print("\nVectors:")

for i,doc_windows in enumerate(docs_windows):
    vec = vectorize_doc(doc_windows, vocab)
    print(f"D{i+1}:", vec)
