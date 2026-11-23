
from flask import Flask, render_template, request

app = Flask(__name__)


# Scientific notation converter
def scientific_format(value):

    if value == 0:
        return "0.000", 0

    exponent = int(f"{value:.2e}".split("e")[1])

    coefficient = value / (10 ** exponent)

    return f"{coefficient:.3f}", exponent


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    ev = None
    result_power = None
    ev_power = None
    error = None

    if request.method == "POST":

        try:
            n = int(request.form["n"])
            mass = float(request.form["mass"])
            length = float(request.form["length"])

            # Planck's Constant (Joule-second)
            h = 6.62607015 * (10 ** -34)

            # Elementary Charge (Coulomb)
            e = 1.602176634 * (10 ** -19)

            # Input validation
            if n <= 0 or mass <= 0 or length <= 0:

                error = "All values must be greater than zero."

            else:

                # Quantum Energy Formula
                energy = (n**2 * h**2) / (8 * mass * length**2)

                # Convert Joules into Electron Volts
                energy_ev = energy / e

                # Format results
                result, result_power = scientific_format(energy)

                ev, ev_power = scientific_format(energy_ev)

        except (ValueError, OverflowError):
            error = "Please enter valid numerical values."

    return render_template(
        "index.html",
        result=result,
        result_power=result_power,
        ev=ev,
        ev_power=ev_power,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
