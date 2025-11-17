# 🎬 Quantum Movie Recommender ⚛️  
### Hybrid Classical + Quantum Recommendation System

This project is a hybrid movie recommendation engine that combines **classical cosine similarity** with a **quantum circuit similarity measure** using PennyLane.  
It uses a **small offline movie dataset** included in the `data` folder — so it works **without any internet or external APIs**. 🚫🌐

---

## ✨ Features

- 📁 Offline movie dataset (no download required)
- ⚛️ Quantum similarity scoring using PennyLane
- 🧮 Classical cosine similarity on genre preferences
- 🔗 Hybrid ranking (70% classical + 30% quantum)
- 🖥️ Streamlit interface for interactive usage

---

## 🧠 How It Works

1. 🎚️ User provides preferences for Action & Romance genres  
2. 📊 Classical similarity calculated using cosine similarity  
3. ⚛️ Quantum similarity from 2-qubit circuit:
   - Rotational feature encoding  
   - Entanglement via CNOT  
   - Expectation value measurement  
4. 🏆 Final hybrid score ranks the movies

---

## 🎥 Dataset

- File: `data/movies.csv`
- 10 quantum-themed movie entries
- Includes:
  - 🎞 Title
  - 📅 Year
  - 🎭 Genre binary flags (Action, Romance)

➡️ Can easily expand with more genres, posters, & ratings

---

## 📦 Dependencies

- `streamlit` — UI  
- `pennylane` — quantum circuits  
- `numpy`, `pandas` — data handling  
- `scikit-learn` — similarity computation  

📌 Install via:

pip install -r requirements.txt


---

