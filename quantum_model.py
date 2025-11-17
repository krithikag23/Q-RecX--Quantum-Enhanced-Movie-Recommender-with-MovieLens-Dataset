import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=2)

def normalize(v):
    v = np.array(v, dtype=float)
    return v / (np.linalg.norm(v) + 1e-10)

@qml.qnode(dev)
def similarity_circuit(user_vec, movie_vec):
    user_vec = normalize(user_vec)
    movie_vec = normalize(movie_vec)

    qml.RY(np.pi * user_vec[0], wires=0)
    qml.RY(np.pi * user_vec[1], wires=1)

    qml.CNOT(wires=[0, 1])

    qml.RY(np.pi * movie_vec[0], wires=0)
    qml.RY(np.pi * movie_vec[1], wires=1)

    return qml.expval(qml.PauliZ(0))

def quantum_similarity(user_vec, movie_vec):
    val = similarity_circuit(user_vec, movie_vec)
    return float(0.5 * (val + 1.0))
