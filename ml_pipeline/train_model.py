from sklearn.linear_model import LogisticRegression
import pickle

def train_model(X, y, save_path="model.pkl"):
    model = LogisticRegression()
    model.fit(X, y)
    with open(save_path, "wb") as f:
        pickle.dump(model, f)