from transformers import T5Tokenizer, T5ForConditionalGeneration

model_name = "valhalla/t5-base-qg-hl"

# Download from Hugging Face
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Saved Locally
save_path = "./valhalla_t5_base_qg_hl"

tokenizer.save_pretrained(save_path)
model.save_pretrained(save_path)

print("Model saved successfully at: ", save_path)