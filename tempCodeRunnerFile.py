@app.route("/predict", methods=["POST"])
# def predict():
#     if "image" not in request.files:
#         return jsonify({"error": "No image uploaded"}), 400

#     file = request.files["image"]
#     if file.filename == "":
#         return jsonify({"error": "No image selected"}), 400

#     img = Image.open(file.stream).convert("RGB")

#     # Preprocess & forward pass
#     inputs = processor(images=img, return_tensors="pt")
#     with torch.no_grad():
#         outputs = model(**inputs)

#     probs = torch.softmax(outputs.logits, dim=-1)[0].detach().numpy()

#     # Find predicted label + confidence
#     pred_id = probs.argmax()
#     pred_label = model.config.id2label[pred_id]
#     confidence = float(probs[pred_id])

#     return jsonify({
#         "prediction": pred_label,
#         "confidence": confidence,
#         "all_probabilities": {
#             model.config.id2label[i]: float(probs[i]) for i in range(len(probs))
#         }
#     })
