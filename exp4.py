from flask import Flask, request, render_template_string
import torch
import torch.nn as nn

app = Flask(__name__)

# Recreate the trained linear model from Exp2(a)
model = nn.Linear(2, 1)
model.eval()

# Minimal inline HTML template
HTML = """
<!doctype html>
<h3>House Price Predictor</h3>
<form method="POST">
  Size (x1000 sq ft): <input type="number" step="0.1" name="size" required><br><br>
  Bedrooms: <input type="number" name="beds" required><br><br>
  <input type="submit" value="Predict">
</form>
{% if prediction %}
  <h4>Estimated Price: ${{ prediction }}k</h4>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        size = float(request.form['size'])
        beds = float(request.form['beds'])
        with torch.no_grad():
            tensor_in = torch.tensor([[size, beds]], dtype=torch.float32)
            prediction = round(model(tensor_in).item(), 2)
    return render_template_string(HTML, prediction=prediction)

if __name__ == '__main__':
    app.run(port=5000)