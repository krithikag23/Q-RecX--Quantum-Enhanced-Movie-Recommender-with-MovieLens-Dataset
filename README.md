# Quantum Movie Recommender – Hybrid Classical + Quantum System

This project is a hybrid movie recommendation engine that combines classical cosine similarity with a quantum circuit similarity measure built using PennyLane. It uses a small offline movie dataset included in the `data` folder to ensure that the application works without any external API or internet dependency.

---

## Features

- Offline movie dataset (no downloads required)
- Quantum similarity scoring using PennyLane
- Classical cosine similarity on genre preferences
- Hybrid ranking: 70% classical + 30% quantum
- Streamlit interface for interactive usage

---

---

## How It Works

1. User provides preferences for Action and Romance genres.
2. Classical similarity is calculated using cosine similarity.
3. Quantum similarity uses a 2-qubit circuit:
   - Rotational feature encoding
   - Entanglement layer
   - Expectation value measurement
4. Hybrid score combines both signals to rank movies.

---

## Dataset

- File: `data/movies.csv`
- Contains 10 custom movie entries with:
  - Title
  - Year
  - Genre indicators (Action, Romance)

Dataset can be easily expanded with more movies and genres.

---

## Dependencies

- streamlit
- pennylane
- numpy
- pandas
- scikit-learn

Installed via `requirements.txt`.

---

## Future Enhancements

- Additional genres (Comedy, Thriller, etc.)
- Integration of IMDb ratings and posters
- Better quantum embedding through a variational circuit
- Detailed model explainability
- Deployment to Streamlit Cloud

---

## Purpose

This project demonstrates:
- Practical quantum computing integration into real applications
- Hybrid ML approaches
- Clean UI for recommendation systems




