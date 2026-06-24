"""
Génère la figure des trajectoires d'un processus d'Ornstein-Uhlenbeck
illustrant le retour à la moyenne.

Palette de couleurs alignée sur les graphiques existants du mémoire
(évolution des taux directeurs BCE / inflation) : dégradé violet / mauve
/ magenta / rose, fond blanc, grille gris clair, titre gris foncé.

Sortie : code_latex/images/processus_ornstein_uhlenbeck.png
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


# --- Paramètres du processus dX_t = kappa (theta - X_t) dt + sigma dW_t ---
KAPPA = 1.2          # vitesse de retour à la moyenne
THETA = 2.0          # niveau de long terme
SIGMA = 0.7          # volatilité instantanée

T = 5.0              # horizon (années)
N_STEPS = 1000       # pas de discrétisation
N_PATHS = 7          # nombre de trajectoires
SEED = 7

# Conditions initiales variées, réparties au-dessus et en dessous de theta.
X0 = np.array([-1.5, -0.3, 0.7, 2.0, 3.3, 4.5, 5.5])


def simulate_ou():
    rng = np.random.default_rng(SEED)
    dt = T / N_STEPS
    t = np.linspace(0.0, T, N_STEPS + 1)
    paths = np.empty((len(X0), N_STEPS + 1))
    paths[:, 0] = X0
    sqrt_dt = np.sqrt(dt)
    for i in range(1, N_STEPS + 1):
        z = rng.standard_normal(len(X0))
        paths[:, i] = (
            paths[:, i - 1]
            + KAPPA * (THETA - paths[:, i - 1]) * dt
            + SIGMA * sqrt_dt * z
        )
    return t, paths


def main():
    t, paths = simulate_ou()

    # Dégradé violet -> magenta -> rose, repris des graphiques existants.
    cmap = LinearSegmentedColormap.from_list(
        "memoire_purple",
        ["#4A235A", "#6A2C70", "#8064A2", "#A03A87", "#C2459D", "#D957B0", "#E89BD4"],
    )
    colors = [cmap(v) for v in np.linspace(0.05, 0.95, len(X0))]

    grey_dark = "#404040"
    grey_grid = "#D9D9D9"

    fig, ax = plt.subplots(figsize=(11, 6))

    for k in range(len(X0)):
        ax.plot(t, paths[k], color=colors[k], linewidth=1.8, alpha=0.95)

    # Niveau de long terme theta.
    ax.axhline(
        THETA,
        color=grey_dark,
        linestyle="--",
        linewidth=1.6,
        label=r"Niveau de long terme $\theta$",
    )

    ax.set_title(
        "Trajectoires d'un processus d'Ornstein-Uhlenbeck",
        fontsize=16,
        color=grey_dark,
        pad=15,
    )
    ax.set_xlabel("Temps $t$ (années)", fontsize=12, color=grey_dark)
    ax.set_ylabel(r"$X_t$", fontsize=12, color=grey_dark)

    ax.set_xlim(0.0, T)
    ax.grid(True, color=grey_grid, linewidth=0.8)
    ax.set_axisbelow(True)

    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_color(grey_grid)

    ax.tick_params(colors=grey_dark)

    legend = ax.legend(loc="upper right", frameon=False, fontsize=11)
    for text in legend.get_texts():
        text.set_color(grey_dark)

    fig.tight_layout()

    out_dir = Path(__file__).resolve().parents[1] / "images"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "processus_ornstein_uhlenbeck.png"
    fig.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Figure enregistrée : {out_path}")


if __name__ == "__main__":
    main()
