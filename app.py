from flask import Flask, render_template_string, request

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Loan EMI Calculator</title>
<style>
  * { box-sizing: border-box; }
  body {
    font-family: 'Segoe UI', Arial, sans-serif;
    background: #0d1117;
    color: #e6edf3;
    display: flex;
    justify-content: center;
    padding: 40px 15px;
    margin: 0;
  }
  .card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 30px;
    width: 100%;
    max-width: 420px;
  }
  h1 {
    text-align: center;
    font-size: 22px;
    color: #58a6ff;
    margin-bottom: 25px;
  }
  label { display: block; margin: 12px 0 6px; font-size: 14px; color: #8b949e; }
  input {
    width: 100%;
    padding: 10px;
    border-radius: 6px;
    border: 1px solid #30363d;
    background: #0d1117;
    color: #e6edf3;
    font-size: 15px;
  }
  button {
    width: 100%;
    margin-top: 20px;
    padding: 12px;
    background: #238636;
    color: #fff;
    border: none;
    border-radius: 6px;
    font-size: 15px;
    cursor: pointer;
  }
  button:hover { background: #2ea043; }
  .result {
    margin-top: 22px;
    padding: 16px;
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 8px;
  }
  .result p { margin: 6px 0; font-size: 14px; }
  .result span { color: #58a6ff; font-weight: bold; }
  .error { color: #f85149; margin-top: 12px; font-size: 14px; }
</style>
</head>
<body>
  <div class="card">
    <h1>Loan EMI Calculator</h1>
    <form method="POST">
      <label>Principal Amount (₹)</label>
      <input type="number" step="any" name="principal" required value="{{ principal or '' }}">

      <label>Annual Interest Rate (%)</label>
      <input type="number" step="any" name="rate" required value="{{ rate or '' }}">

      <label>Loan Tenure (months)</label>
      <input type="number" name="tenure" required value="{{ tenure or '' }}">

      <button type="submit">Calculate EMI</button>
    </form>

    {% if error %}
      <div class="error">{{ error }}</div>
    {% endif %}

    {% if emi %}
    <div class="result">
      <p>Monthly EMI: <span>₹ {{ emi }}</span></p>
      <p>Total Payment: <span>₹ {{ total_payment }}</span></p>
      <p>Total Interest: <span>₹ {{ total_interest }}</span></p>
    </div>
    {% endif %}
  </div>
</body>
</html>
"""


def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / (12 * 100)
    if monthly_rate == 0:
        emi = principal / tenure_months
    else:
        emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / \
              (((1 + monthly_rate) ** tenure_months) - 1)
    total_payment = emi * tenure_months
    total_interest = total_payment - principal
    return emi, total_payment, total_interest


@app.route("/", methods=["GET", "POST"])
def index():
    emi = total_payment = total_interest = None
    principal = rate = tenure = None
    error = None

    if request.method == "POST":
        try:
            principal = float(request.form["principal"])
            rate = float(request.form["rate"])
            tenure = int(request.form["tenure"])

            if principal <= 0 or rate < 0 or tenure <= 0:
                error = "Please enter positive values."
            else:
                emi, total_payment, total_interest = calculate_emi(principal, rate, tenure)
                emi = f"{emi:,.2f}"
                total_payment = f"{total_payment:,.2f}"
                total_interest = f"{total_interest:,.2f}"
        except (ValueError, KeyError):
            error = "Please enter valid numeric values."

    return render_template_string(
        PAGE, emi=emi, total_payment=total_payment,
        total_interest=total_interest, principal=principal,
        rate=rate, tenure=tenure, error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
