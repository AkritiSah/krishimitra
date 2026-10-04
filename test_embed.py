from sentence_transformers import SentenceTransformer, util

print("Loading model (first run downloads ~470 MB)...")
model = SentenceTransformer("intfloat/multilingual-e5-small")

# E5 models need a prefix on every text
nepali    = "query: टमाटरको बिरुवामा कीरा लागेको छ"
english   = "passage: Insects have attacked the tomato plant"
unrelated = "passage: The weather is sunny today"

emb = model.encode([nepali, english, unrelated], normalize_embeddings=True)

print("Nepali vs English (same meaning):", util.cos_sim(emb[0], emb[1]).item())
print("Nepali vs Unrelated sentence   :", util.cos_sim(emb[0], emb[2]).item())