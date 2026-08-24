from manim import *
import random
import numpy as np

# Light and dark variants for the SMP1 homepage hero loop.
TITLE_COLOR = "#6CA2C6"
ACCENT_COLOR = "#91c776"

SMP_SYMBOLS = [
    r"P(A)", r"P(A \mid B)", r"E[X]", r"\mathrm{Var}(X)", r"X \sim \mathcal{N}(\mu,\sigma^2)",
    r"\mu", r"\sigma", r"\Sigma", r"\rho", r"\lambda",
    r"\chi^2", r"t", r"F", r"H_0", r"H_1", r"p",
    r"\hat{\mu}", r"\hat{\sigma}", r"\bar{X}", r"S^2",
    r"\mathrm{CI}", r"\mathrm{MSE}", r"\mathrm{RSS}", r"\beta_0", r"\beta_1",
    r"\mathrm{Markov}", r"\mathrm{SMP1}", r"\mathrm{Bayes}",
    r"\mathrm{Poisson}", r"\mathrm{Binomial}", r"\mathrm{Normal}",
    r"\mathbb{P}", r"\mathbb{E}", r"\mathcal{N}", r"\mathcal{P}",
    r"\begin{bmatrix}0.7 & 0.3 \\ 0.2 & 0.8\end{bmatrix}",
    r"\sum_{i=1}^{n} X_i", r"\int_{-\infty}^{\infty} f(x)\,dx",
    r"\mathrm{VIA}", r"\mathrm{R. Brooks}",
]


def build_symbol_rain(class_name, colors, background_color, duration=18.0, num_symbols=260):
    bg = background_color

    class SceneClass(Scene):
        def construct(self):
            self.camera.background_color = bg

            min_y, max_y = -4.2, 4.2
            min_x, max_x = -7.2, 7.2
            y_range = max_y - min_y
            base_speed = y_range / duration

            drops = VGroup()

            for _ in range(num_symbols):
                tex = random.choice(SMP_SYMBOLS)
                mob = MathTex(tex)
                mob.set_color(random.choice(colors))
                mob.scale(random.uniform(0.35, 0.55))

                init_x = random.uniform(min_x, max_x)
                init_y = random.uniform(min_y, max_y)
                mob.init_x = init_x
                mob.y_pos = init_y
                mob.speed = base_speed * random.uniform(0.9, 1.1)
                mob.move_to(np.array([init_x, init_y, 0]))

                def update_drop(mob, dt, symbol=mob):
                    symbol.y_pos -= symbol.speed * dt
                    if symbol.y_pos < min_y:
                        symbol.y_pos = max_y
                    mob.move_to(np.array([symbol.init_x, symbol.y_pos, 0]))
                    opacity = 0.45 + 0.45 * np.sin(
                        2 * np.pi * (symbol.y_pos - min_y) / y_range
                    )
                    mob.set_opacity(opacity)
                    if random.random() < 0.004:
                        mob.set_opacity(random.uniform(0.25, 1.0))

                mob.add_updater(update_drop)
                drops.add(mob)

            title = Text(
                "Stochastic Modelling & Processes",
                color=TITLE_COLOR,
                weight=BOLD,
            ).scale(0.65).to_edge(UP, buff=0.45)

            subtitle = Text("SMP1", color=ACCENT_COLOR).scale(0.5).next_to(
                title, DOWN, buff=0.15
            )

            self.add(drops)
            self.add(title, subtitle)
            self.wait(duration)

    SceneClass.__name__ = class_name
    return SceneClass


StochasticIntroLight = build_symbol_rain(
    "StochasticIntroLight",
    colors=["#6CA2C6", "#91c776", "#363636"],
    background_color="#FFFFFF",
)

StochasticIntroDark = build_symbol_rain(
    "StochasticIntroDark",
    colors=["#6CA2C6", "#91c776", "#E8EEF5"],
    background_color="#1a1a1a",
)
