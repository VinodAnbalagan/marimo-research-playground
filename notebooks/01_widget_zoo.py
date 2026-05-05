import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    return mo, np, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # 01 — marimo Widget Zoo

    This is my first marimo notebook.

    I am learning:

    - how widgets work
    - how `.value` works
    - how cells connect to each other
    - how to build interactive research notebooks
    """)
    return


@app.cell
def _(mo):
    temperature = mo.ui.slider(
        start=0.0,
        stop=2.0,
        step=0.1,
        value=1.0,
        label="Temperature",
    )

    temperature
    return (temperature,)


@app.cell
def _(mo, temperature):
    mo.md(f"""
    ## Reading a widget value

    The current temperature is:

    # `{temperature.value}`

    When you move the slider above, this text updates automatically.
    """)
    return


@app.cell
def _(np, plt, temperature):
    simple_x = np.linspace(0, 10, 200)

    simple_y = np.sin(simple_x * temperature.value)
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(simple_x, simple_y)

    ax.set_title(f"Sine wave controlled by temperature = {temperature.value}")
    ax.set_xlabel("x")
    ax.set_ylabel("sin(x * temperature)")
    ax.grid(alpha=0.3)

    fig
    return


@app.cell
def _(mo):
    n_points = mo.ui.slider(
        start=50,
        stop=500,
        step=50,
        value=200,
        label="Number of points",
    )

    amplitude = mo.ui.slider(
        start=0.5,
        stop=5.0,
        step=0.5,
        value=2.0,
        label="Amplitude",
    )

    frequency = mo.ui.slider(
        start=0.5,
        stop=8.0,
        step=0.5,
        value=2.0,
        label="Frequency",
    )

    noise = mo.ui.slider(
        start=0.0,
        stop=2.0,
        step=0.1,
        value=0.3,
        label="Noise",
    )

    seed = mo.ui.number(
        start=0,
        stop=9999,
        value=7,
        label="Random seed",
    )

    color_map = mo.ui.dropdown(
        options=["viridis", "plasma", "magma", "cividis"],
        value="viridis",
        label="Color map",
    )

    show_points = mo.ui.checkbox(
        value=True,
        label="Show noisy points",
    )
    return amplitude, color_map, frequency, n_points, noise, seed, show_points


@app.cell
def _(amplitude, color_map, frequency, mo, n_points, noise, seed, show_points):
    mo.vstack(
        [
            mo.md("## Dashboard controls"),
            n_points,
            amplitude,
            frequency,
            noise,
            seed,
            color_map,
            show_points,
        ]
    )
    return


@app.cell
def _(amplitude, frequency, n_points, noise, np, pd, seed):
    rng = np.random.default_rng(seed.value)

    x_curve = np.linspace(0, 10, int(n_points.value))

    clean_curve = amplitude.value * np.sin(frequency.value * x_curve)

    observed_curve = clean_curve + rng.normal(
        loc=0,
        scale=noise.value,
        size=len(x_curve),
    )

    data = pd.DataFrame(
        {
            "x": x_curve,
            "clean_signal": clean_curve,
            "observed_signal": observed_curve,
            "noise": observed_curve - clean_curve,
        }
    )
    return clean_curve, data, observed_curve, x_curve


@app.cell
def _(clean_curve, color_map, observed_curve, plt, show_points, x_curve):
    fig2, ax2 = plt.subplots(figsize=(9, 4))

    if show_points.value:
        ax2.scatter(
            x_curve,
            observed_curve,
            c=observed_curve,
            cmap=color_map.value,
            alpha=0.7,
            label="observed noisy points",
        )

    ax2.plot(
        x_curve,
        clean_curve,
        color="black",
        linewidth=2,
        label="clean signal",
    )

    ax2.set_title("Interactive signal dashboard")
    ax2.set_xlabel("x")
    ax2.set_ylabel("signal")
    ax2.legend()
    ax2.grid(alpha=0.3)

    fig2
    return


@app.cell
def _(data, mo):
    mo.ui.table(data.head(20).round(3))
    return


@app.cell
def _(amplitude, frequency, mo, n_points, noise, observed_curve, pd, seed):
    summary = pd.DataFrame(
        [
            {
                "setting": "number of points",
                "value": n_points.value,
            },
            {
                "setting": "amplitude",
                "value": amplitude.value,
            },
            {
                "setting": "frequency",
                "value": frequency.value,
            },
            {
                "setting": "noise",
                "value": noise.value,
            },
            {
                "setting": "seed",
                "value": seed.value,
            },
            {
                "setting": "mean observed signal",
                "value": observed_curve.mean(),
            },
            {
                "setting": "standard deviation observed signal",
                "value": observed_curve.std(),
            },
        ]
    )

    mo.ui.table(summary)
    return


@app.cell
def _(mo):
    research_note = mo.ui.text_area(
        value="Changing noise makes the system less predictable, but the clean signal is still visible.",
        label="Research note",
        rows=4,
        full_width=True,
    )

    research_note
    return


@app.cell
def _(mo):
    concept_tags = mo.ui.multiselect(
        options=[
            "state",
            "noise",
            "local interaction",
            "emergence",
            "dissipation",
            "symmetry",
            "feedback",
            "world model",
        ],
        value=["state", "noise"],
        label="Concept tags",
    )

    concept_tags
    return (concept_tags,)


@app.cell
def _(concept_tags, mo):
    mo.md(
        f"""
        ## Selected concepts

        You selected:

        `{", ".join(concept_tags.value)}`

        These tags will become useful later when we build toy physics notebooks.
        """
    )
    return


@app.cell
def _(amplitude, frequency, mo, n_points, noise):
    mo.hstack(
        [
            mo.stat(
                label="Points",
                value=str(n_points.value),
            ),
            mo.stat(
                label="Amplitude",
                value=str(amplitude.value),
            ),
            mo.stat(
                label="Frequency",
                value=str(frequency.value),
            ),
            mo.stat(
                label="Noise",
                value=str(noise.value),
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md("""
    ## What I learned

    In this notebook, I learned that:

    1. Widgets are created with `mo.ui`.
    2. The current widget value is read with `.value`.
    3. Cells automatically rerun when their inputs change.
    4. A slider can control text, data, plots, and tables.
    5. marimo notebooks can become interactive research dashboards.
    """)
    return


if __name__ == "__main__":
    app.run()
