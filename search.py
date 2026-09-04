import os

documents = {}
folder = "docs"

for filename in os.listdir(folder):
    with open(os.path.join(folder, filename), "r") as f:
        documents[filename] = f.read().lower()

index = {}

for filename, text in documents.items():
    words = text.split()
    for word in words:
        word = word.strip(".,!?")
        if word not in index:
            index[word] = {}
        if filename not in index[word]:
            index[word][filename] = 0
        index[word][filename] += 1

print("Mini Search Engine")
print("-" * 40)

query = input("Search: ").lower().split()

scores = {}
for word in query:
    if word in index:
        for filename, count in index[word].items():
            if filename not in scores:
                scores[filename] = 0
            scores[filename] += count

ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print("Results:")
for filename, score in ranked:
    print(f"{filename} (score: {score})")