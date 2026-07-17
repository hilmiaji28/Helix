import joblib

model = joblib.load("models/best_tuned_model.pkl")

print(type(model))
print()

print(model)

print()

if hasattr(model, "named_steps"):
    print("Pipeline steps:")
    print(model.named_steps.keys())
