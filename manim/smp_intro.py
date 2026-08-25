from manim import *
import random
import numpy as np

config.renderer = "opengl"
config.background_color = "#FFFFFF"

SMP_SYMBOLS = [
    r"\lambda", r"\Sigma", r"\rightarrow", r"P(A)", r"P(A \mid B)",
    r"\mathbb{E}[X]", r"\mathrm{Var}(X)", r"\mu", r"\sigma", r"\rho",
    r"X \sim \mathcal{N}(\mu,\sigma^2)", r"\mathcal{N}(\mu,\sigma^2)",
    r"\sum_{i=1}^{n}", r"\begin{bmatrix}0.7 & 0.3 \\ 0.2 & 0.8\end{bmatrix}",
    r"\hat{\mu}", r"\bar{X}", r"S^2", r"H_0", r"H_1", r"p",
    r"\chi^2", r"\beta_0", r"\beta_1", r"\mathrm{CI}",
    r"\mathbb{P}", r"\mathbb{E}", r"\mathcal{N}", r"\mathcal{P}",
    r"\text{Markov}", r"\text{Bayes}", r"\text{Poisson}", r"\text{Binomial}",
    r"\text{Normal}", r"\text{Regression}", r"f(x)", r"F(x)",
    r"\int_{-\infty}^{\infty} f(x)\,dx", r"\text{stationary}",
    r"\text{SMP1}", r"\text{SMP1}",
    r"\text{VIA}", r"\text{R. Brooks}",
]


class StochasticIntroLight(ThreeDScene):
    def construct(self):
        duration = 20.0
        min_z, max_z = -10, 10
        min_y, max_y = -4, 4
        z_range = max_z - min_z
        y_range = max_y - min_y
        base_speed_z = z_range / duration
        base_speed_y = y_range / duration

        colors = ["#363636", "#6CA2C6", "#C0D4f0;"]
        
        drops = VGroup()
        num_symbols = 400

        for _ in range(num_symbols):
            tex = random.choice(SMP_SYMBOLS)
            mob = MathTex(tex)
            mob.set_color(random.choice(colors))
            mob.scale(0.5)

            init_z = random.uniform(min_z, max_z)
            init_x = random.uniform(-7, 7)
            init_y = random.uniform(min_y, max_y)

            mob.init_x = init_x
            mob.init_y = init_y
            mob.z_pos = init_z
            mob.y_pos = init_y

            mob.speed_z = base_speed_z * random.uniform(0.95, 1.05)
            mob.speed_y = base_speed_y * random.uniform(0.95, 1.05)
            mob.motion_axis = random.choice(["z", "y"])

            mob.move_to(np.array([init_x, init_y, init_z]))

            def update_drop(mob, dt, symbol=mob):
                if symbol.motion_axis == "z":
                    symbol.z_pos += symbol.speed_z * dt
                    if symbol.z_pos > max_z:
                        symbol.z_pos = min_z
                else:
                    symbol.y_pos -= symbol.speed_y * dt
                    if symbol.y_pos < min_y:
                        symbol.y_pos = max_y

                mob.move_to(np.array([symbol.init_x, symbol.y_pos, symbol.z_pos]))

                opacity = 0.5 + 0.5 * np.sin(2 * np.pi * (symbol.z_pos - min_z) / z_range)
                mob.set_opacity(opacity)

                if random.random() < 0.005:
                    mob.set_opacity(random.uniform(0.3, 1.0))

            mob.add_updater(update_drop)
            drops.add(mob)

        self.add(drops)
        self.wait(duration)


from manim import *
import random
import numpy as np

config.renderer = "opengl"
config.background_color = "#FFFFFF"


class StochasticIntroDark(ThreeDScene):
    def construct(self):
        duration = 20.0
        min_z, max_z = -10, 10
        min_y, max_y = -4, 4
        z_range = max_z - min_z
        y_range = max_y - min_y
        base_speed_z = z_range / duration
        base_speed_y = y_range / duration

        colors = ["#363636", "#6CA2C6", "#C0D4f0;"]

        drops = VGroup()
        num_symbols = 400

        for _ in range(num_symbols):
            tex = random.choice(SMP_SYMBOLS)
            mob = MathTex(tex)
            mob.set_color(random.choice(colors))
            mob.scale(0.5)

            init_z = random.uniform(min_z, max_z)
            init_x = random.uniform(-7, 7)
            init_y = random.uniform(min_y, max_y)

            mob.init_x = init_x
            mob.init_y = init_y
            mob.z_pos = init_z
            mob.y_pos = init_y

            mob.speed_z = base_speed_z * random.uniform(0.95, 1.05)
            mob.speed_y = base_speed_y * random.uniform(0.95, 1.05)
            mob.motion_axis = random.choice(["z", "y"])

            mob.move_to(np.array([init_x, init_y, init_z]))

            def update_drop(mob, dt, symbol=mob):
                if symbol.motion_axis == "z":
                    symbol.z_pos += symbol.speed_z * dt
                    if symbol.z_pos > max_z:
                        symbol.z_pos = min_z
                else:
                    symbol.y_pos -= symbol.speed_y * dt
                    if symbol.y_pos < min_y:
                        symbol.y_pos = max_y

                mob.move_to(np.array([symbol.init_x, symbol.y_pos, symbol.z_pos]))

                opacity = 0.5 + 0.5 * np.sin(2 * np.pi * (symbol.z_pos - min_z) / z_range)
                mob.set_opacity(opacity)

                if random.random() < 0.005:
                    mob.set_opacity(random.uniform(0.3, 1.0))

            mob.add_updater(update_drop)
            drops.add(mob)

        self.add(drops)
        self.wait(duration)
