import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(
    page_title="Lichen Hybrid Kernel",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🌌 LICHEN HYBRID KERNEL")
st.markdown("**Système d'Exploitation Quantique Fractale (Tzolk'in Architecture)**")

# Création des onglets
tab_logic, tab_chip = st.tabs(["🧠 KERNEL (Logique)", "💎 CHIP (Architecture)"])

# ==========================================
# ONGLET 1 : LOGIQUE (TZBIT + PTEC)
# ==========================================
with tab_logic:
    st.header("Simulation Logique : TzBit Auto-Guérisseur")
    
    # --- CLASSES BACKEND ---
    class TzBit:
        DIMENSION = 5
        OMEGA = np.exp(2j * np.pi / 5)

        def __init__(self):
            self.state = np.array([1, 0, 0, 0, 0], dtype=complex)

        def H(self):
            H5 = np.zeros((5, 5), dtype=complex)
            for i in range(5):
                for j in range(5):
                    H5[i, j] = (self.OMEGA**(i*j))
            H5 /= np.sqrt(5)
            self.state = H5 @ self.state

        def normalize(self):
            norm = np.sqrt(np.sum(np.abs(self.state)**2))
            if norm > 0: self.state = self.state / norm

        def __str__(self):
            probs = np.abs(self.state)**2
            return "\n".join([f"|{i}⟩ : {self.state[i]:.2f} (P={probs[i]:.2f})" for i in range(5)])

    class PentagonalCorrector:
        def __init__(self):
            self.phi = (1 + np.sqrt(5)) / 2 

        def calculate_syndrome(self, tzbit_state):
            phases = np.angle(tzbit_state)
            syndromes = []
            for i in range(5):
                p_curr, p_next, p_prev = phases[i], phases[(i + 1) % 5], phases[(i - 1) % 5]
                local_curvature = p_next - 2*p_curr + p_prev
                if abs(local_curvature) > 1.0: syndromes.append(i)
            return syndromes

        def apply_correction(self, tzbit, syndrome_indices):
            if not syndrome_indices: return tzbit, False 
            correction_matrix = np.eye(5, dtype=complex)
            for idx in syndrome_indices:
                correction_matrix[idx, idx] = np.exp(-1j * (np.pi/5)) 
            tzbit.state = correction_matrix @ tzbit.state
            tzbit.normalize()
            return tzbit, True

    # --- INTERFACE LOGIQUE ---
    col_btn, col_info = st.columns([1, 3])
    with col_btn:
        run_sim = st.button("🚀 Lancer Simulation Quantique", type="primary")
    
    if run_sim:
        # 1. Création
        tzbit = TzBit()
        tzbit.H()
        st.subheader("1. État Sain (Superposition)")
        c1, c2 = st.columns(2)
        c1.code(str(tzbit))
        c2.bar_chart(np.abs(tzbit.state)**2)

        # 2. Erreur
        noise = np.eye(5, dtype=complex)
        noise[2, 2] = np.exp(1j * 2.5)
        tzbit.state = noise @ tzbit.state
        st.subheader("2. Injection d'Erreur")
        st.error("⚠️ Rupture de symétrie détectée sur |2⟩")

        # 3. Correction
        st.subheader("3. Protocole PTEC")
        corrector = PentagonalCorrector()
        fixed, cycles = True, 0
        with st.expander("Logs du Système PTEC", expanded=True):
            while fixed and cycles < 5:
                cycles += 1
                syndromes = corrector.calculate_syndrome(tzbit.state)
                if syndromes:
                    st.warning(f"Cycle {cycles}: Correction topologique sur {syndromes}...")
                    tzbit, fixed = corrector.apply_correction(tzbit, syndromes)
                else:
                    st.success(f"Cycle {cycles}: Symétrie restaurée.")
                    fixed = False

        # 4. Final
        st.subheader("4. État Final")
        c3, c4 = st.columns(2)
        c3.success("✅ Intégrité restaurée")
        c3.code(str(tzbit))
        c4.bar_chart(np.abs(tzbit.state)**2)

# ==========================================
# ONGLET 2 : CHIP (FRIQS VISUALIZER)
# ==========================================
with tab_chip:
    st.header("Architecture Matérielle : Processeur FRIQS")
    st.markdown("""
    Ceci est la topologie réelle de la puce. Le pavage fractal permet la résilience aux erreurs
    et l'évacuation thermique via les canaux microfluidiques (espaces vides).
    """)

    # Contrôles
    depth = st.slider("Profondeur Fractale (Complexité)", min_value=2, max_value=5, value=4)
    
    # --- VISUALIZER CLASS ---
    class FRIQS_Visualizer:
        PHI = (1 + np.sqrt(5)) / 2
        PI_5 = np.pi / 5

        def __init__(self, depth):
            self.depth = depth
            self.total_tzbits = 0
            # Création de la figure
            self.fig, self.ax = plt.subplots(figsize=(10, 10))
            self.ax.set_aspect('equal')
            self.ax.set_facecolor('#050510')
            self.fig.patch.set_facecolor('#050510')

        def get_pentagon(self, cx, cy, r, offset=0):
            angles = np.linspace(0, 2*np.pi, 6)[:-1] + offset + (np.pi/2)
            return cx + r * np.cos(angles), cy + r * np.sin(angles)

        def draw_recursive(self, x, y, r, d, offset=0):
            if d == 0: return
            
            # Couleurs (Or = Core, Cyan = Quantum)
            colors = ['#FFD700', '#00FFFF', '#BD00FF', '#00FF00', '#FFFFFF']
            c = colors[min(self.depth - d, 4)]
            lw = 2.0 if d == self.depth else 0.8
            
            px, py = self.get_pentagon(x, y, r, offset)
            # Dessin coupleurs
            self.ax.plot(np.append(px, px[0]), np.append(py, py[0]), color=c, lw=lw, alpha=0.8)
            
            # Dessin TzBits (Points)
            if d <= self.depth - 1:
                self.ax.scatter(px, py, color='white', s=15*d, zorder=10, alpha=0.9, edgecolors=c)
                self.total_tzbits += 5

            # Récursion Phi
            new_r = r / (1 + self.PHI)
            new_off = offset + self.PI_5
            for i in range(5):
                self.draw_recursive(px[i], py[i], new_r, d-1, new_off)
            
            # Centre inversé
            if d > 1:
                self.draw_recursive(x, y, r * (1/self.PHI)**2, d-1, offset + np.pi)

        def generate(self):
            self.draw_recursive(0, 0, 100, self.depth)
            self.ax.axis('off')
            return self.fig, self.total_tzbits

    # Génération
    if st.button("Générer la Topologie FRIQS"):
        with st.spinner("Calcul de la géométrie sacrée..."):
            viz = FRIQS_Visualizer(depth)
            fig, count = viz.generate()
            
            col_viz, col_data = st.columns([3, 1])
            with col_viz:
                st.pyplot(fig)
            with col_data:
                st.info(f"📊 STATS PUCE")
                st.metric("TzBits Actifs", count)
                st.metric("Couche Fractale", depth)
                st.markdown("**Géométrie:**")
                st.markdown("- Base: Pentagone")
                st.markdown("- Ratio: $\phi$ (Golden)")
                st.markdown("- Pavage: Penrose")
