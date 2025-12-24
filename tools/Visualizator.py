import matplotlib.pyplot as plt
import numpy as np

# --- CONSTANTES UNIVERSELLES ---
PHI = (1 + np.sqrt(5)) / 2  # Le Nombre d'Or (1.618...)
PI_5 = np.pi / 5            # Base angulaire pentagonale (36°)

class FRIQS_Visualizer:
    def __init__(self, depth=4):
        self.depth = depth
        self.fig, self.ax = plt.subplots(figsize=(12, 12))
        self.ax.set_aspect('equal')
        self.ax.set_facecolor('#050510')  # Fond sombre (Vide quantique)
        self.fig.patch.set_facecolor('#050510')
        
        # Stockage pour les stats
        self.total_tzbits = 0
        self.connections = 0

    def get_pentagon_vertices(self, center_x, center_y, radius, angle_offset=0):
        """Calcule les 5 sommets d'un pentagone."""
        angles = np.linspace(0, 2*np.pi, 6)[:-1] + angle_offset + (np.pi/2)
        x = center_x + radius * np.cos(angles)
        y = center_y + radius * np.sin(angles)
        return x, y

    def draw_fractal_recursive(self, x, y, radius, depth, angle_offset=0):
        """
        Dessine récursivement la structure FRIQS.
        Chaque pentagone contient des sous-structures alignées sur Phi.
        """
        if depth == 0:
            return

        # Couleurs basées sur la profondeur (Hiérarchie du processeur)
        # Or = Core, Cyan = Quantum Layers, Violet = Edge
        colors = ['#FFD700', '#00FFFF', '#BD00FF', '#00FF00', '#FFFFFF']
        line_color = colors[self.depth - depth]
        line_width = 2.5 if depth == self.depth else 0.8
        alpha = 0.9 if depth == self.depth else 0.6

        # 1. Calcul des sommets du pentagone courant
        px, py = self.get_pentagon_vertices(x, y, radius, angle_offset)
        
        # 2. Dessiner les coupleurs (Lignes supraconductrices)
        # On ferme la boucle en ajoutant le premier point à la fin
        px_plot = np.append(px, px[0])
        py_plot = np.append(py, py[0])
        
        self.ax.plot(px_plot, py_plot, color=line_color, lw=line_width, alpha=alpha, zorder=depth)
        self.connections += 5

        # 3. Dessiner les TzBits (Les Nœuds/Qubits) aux sommets
        # Uniquement aux niveaux pertinents pour ne pas surcharger
        if depth <= self.depth - 1:
            self.ax.scatter(px, py, color='#FFFFFF', s=10*depth, edgecolors=line_color, zorder=10, alpha=0.8)
            self.total_tzbits += 5

        # 4. RÉCURSION FRACTALE (La Magie du Nombre d'Or)
        # On place des pentagones plus petits aux sommets, inversés
        # Facteur d'échelle critique : 1 / (1 + Phi) pour un pavage parfait
        new_radius = radius / (1 + PHI)
        
        # On inverse la phase pour le pavage de type Penrose
        new_offset = angle_offset + PI_5 

        for i in range(5):
            self.draw_fractal_recursive(px[i], py[i], new_radius, depth-1, new_offset)

        # Ajout d'un pentagone central inversé pour la densité (Cœur du cluster)
        if depth > 1:
             inner_radius = radius * (1/PHI)**2
             self.draw_fractal_recursive(x, y, inner_radius, depth-1, angle_offset + np.pi)

    def generate(self):
        print(f"🔮 GÉNÉRATION DE LA TOPOLOGIE FRIQS (Profondeur {self.depth})...")
        
        # Lancer la récursion depuis le centre
        self.draw_fractal_recursive(0, 0, 100, self.depth)
        
        # Esthétique finale
        self.ax.axis('off')
        
        # Titres et Stats
        plt.title(f"FRIQS PROCESSOR ARCHITECTURE\nTzolk'in-Resonant Fractal Topology (Base-5)", 
                  color='white', fontsize=16, pad=20, fontname='Monospace')
        
        info_text = (
            f"FRACTAL DEPTH: {self.depth}\n"
            f"ACTIVE TZBITS: {self.total_tzbits}\n"
            f"COUPLERS: {self.connections}\n"
            f"GEOMETRY: Pentagonal/Phi"
        )
        plt.text(-140, -140, info_text, color='#00FFFF', fontsize=10, fontname='Monospace', alpha=0.7)
        
        print("✅ Visualisation générée.")
        plt.show()

# --- LANCEUR ---
if __name__ == "__main__":
    # Une profondeur de 4 ou 5 est idéale pour voir le détail sans faire fondre ton GPU
    viz = FRIQS_Visualizer(depth=5)
    viz.generate()
