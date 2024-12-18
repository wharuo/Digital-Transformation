
from flask import Flask, request, jsonify, send_file
import os
import spacy
from fpdf import FPDF

app = Flask(__name__)
REPORT_FOLDER = 'reports'
os.makedirs(REPORT_FOLDER, exist_ok=True)

nlp = spacy.load("en_core_web_sm")
VALIDATION_LOG = []

def validate_rules(rules):
    doc = nlp(rules)
    issues, suggestions = [], []

    if len(doc) < 5:
        issues.append("Rule is too short.")
        suggestions.append("Add conditions for better clarity.")
    if "always" in rules.lower():
        issues.append("Avoid rigid words like 'always'.")
        suggestions.append("Use more flexible terms like 'typically'.")
    if "if" not in rules.lower():
        issues.append("Missing 'if' condition.")
        suggestions.append("Structure the rule with 'if' for conditions and 'then' for actions.")

    VALIDATION_LOG.append({"rule": rules, "issues": issues, "suggestions": suggestions})
    return {"status": "warning" if issues else "success", "issues": issues, "suggestions": suggestions}

@app.route('/validate', methods=['POST'])
def validate_endpoint():
    data = request.json.get("rules", "")
    return jsonify(validate_rules(data))

@app.route('/generate_report', methods=['GET'])
def generate_report():
    if not VALIDATION_LOG:
        return jsonify({"message": "No rules have been validated yet."}), 404

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="AI Validation Report", ln=True, align="C")
    for idx, log in enumerate(VALIDATION_LOG, start=1):
        pdf.cell(0, 10, txt=f"Rule {idx}: {log['rule']}", ln=True)
        for issue in log['issues']:
            pdf.cell(0, 10, txt=f"  - Issue: {issue}", ln=True)
        for suggestion in log['suggestions']:
            pdf.cell(0, 10, txt=f"  - Suggestion: {suggestion}", ln=True)

    report_path = os.path.join(REPORT_FOLDER, "validation_report.pdf")
    pdf.output(report_path)
    return send_file(report_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
