import pickle

def load_model(model_path="model.pkl"):
    with open(model_path, "rb") as f:
        return pickle.load(f)

def predict(model, features):
    return model.predict_proba([features])[0]