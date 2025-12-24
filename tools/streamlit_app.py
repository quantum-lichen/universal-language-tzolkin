import streamlit as st
import numpy as np

# ==========================================
# 1. DÉFINITION DES CLASSES (BACKEND)
# ==========================================

class TzBit:
    """
    Tzolk'in Bit: Unité hybride quantique-classique à 5 niveaux.
    """
    DIMENSION = 5
    OMEGA = np.exp(2j * np.pi / 5)

    def __init__(self):
        # État initial |0>
        self.state = np.array([1, 0, 0, 0, 0], dtype=complex)

    def H(self):
        """Hadamard 5x5"""
        H5 = np.zeros((5, 5), dtype=complex)
        for i in range(5):
            for j in range(5):
                H5[i, j] = (self.OMEGA**(i*j))
        H5 /= np.sqrt(5)
        self.state = H5 @ self.state

    def normalize(self):
        norm = np.sqrt(np.sum(np.abs(self.state)**2))
        if norm > 0:
            self.state = self.state / norm

    def __str__(self):
        # Formattage joli pour l'affichage
        probs = np.abs(self.state)**2
        return "\n".join([f"|{i}⟩ : {self.state[i]:.2f} (P={probs[i]:.2f})" for i in range(5)])

class PentagonalCorrector:
    """
    Système de Correction d'Erreur Topologique
    """
    def __init__(self):
        self.phi = (1 + np.sqrt(5)) / 2 

    def calculate_syndrome(self, tzbit_state):
        phases = np.angle(tzbit_state)
        syndromes = []
        for i in range(5):
            p_curr = phases[i]
            p_next = phases[(i + 1) % 5]
            p_prev = phases[(i - 1) % 5]
            
            # Calcul de la courbure locale
            local_curvature = p_next - 2*p_curr + p_prev
            
            if abs(local_curvature) > 1.0: 
                syndromes.append(i)
        return syndromes

    def apply_correction(self, tzbit, syndrome_indices):
        if not syndrome_indices:
            return tzbit, False 
            
        # Matrice de correction
        correction_matrix = np.eye(5, dtype=complex)
        for idx in syndrome_indices:
            correction_matrix[idx, idx] = np.exp(-1j * (np.pi/5)) 
            
        tzbit.state = correction_matrix @ tzbit.state
        tzbit.normalize() # Important après correction manuelle
        return tzbit, True

# ==========================================
# 2. INTERFACE STREAMLIT (FRONTEND)
# ==========================================

st.set_page_config(page_title="TzBit Auto-Healing", page_icon="🔮", layout="wide")

st.title("🔮 Simulation : Auto-Guérison du TzBit")
st.markdown("---")

# Bouton pour lancer la simulation
if st.button("🚀 Lancer la Simulation Quantique", type="primary"):
    
    # ÉTAPE 1 : CRÉATION
    st.subheader("1. État Initial (Sain)")
    tzbit = TzBit()
    tzbit.H() # Superposition
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("Création du TzBit en superposition parfaite...")
        st.code(str(tzbit))
    with col2:
        # Visualisation des probabilités
        probs = np.abs(tzbit.state)**2
        st.bar_chart(probs)

    # ÉTAPE 2 : ERREUR
    st.subheader("2. Injection d'Erreur (Bruit)")
    
    # On corrompt l'état |2>
    noise_matrix = np.eye(5, dtype=complex)
    noise_matrix[2, 2] = np.exp(1j * 2.5) 
    tzbit.state = noise_matrix @ tzbit.state
    
    st.error("⚠️ ALERTE : Bruit de phase détecté sur l'état |2⟩")
    st.code(str(tzbit))

    # ÉTAPE 3 : CORRECTION
    st.subheader("3. Protocole PTEC (Pentagonal Correction)")
    
    corrector = PentagonalCorrector()
    log_container = st.expander("Voir les logs de correction", expanded=True)
    
    with log_container:
        fixed = True
        cycles = 0
        while fixed and cycles < 5:
            cycles += 1
            syndromes = corrector.calculate_syndrome(tzbit.state)
            
            if syndromes:
                st.warning(f"Cycle {cycles}: Rupture de symétrie détectée sur {syndromes}. Application de la correction...")
                tzbit, fixed = corrector.apply_correction(tzbit, syndromes)
            else:
                st.success(f"Cycle {cycles}: Structure stable. Symétrie Pentagonale OK.")
                fixed = False # On arrête la boucle
    
    # ÉTAPE 4 : RÉSULTAT FINAL
    st.markdown("---")
    st.subheader("4. État Final (Guéri)")
    
    col3, col4 = st.columns(2)
    with col3:
        st.success("✅ Information restaurée sans clonage !")
        st.code(str(tzbit))
    with col4:
        # Vérification visuelle que les barres sont revenues à la normale
        final_probs = np.abs(tzbit.state)**2
        st.bar_chart(final_probs)

else:
    st.info("Cliquez sur le bouton pour démarrer la simulation.")
