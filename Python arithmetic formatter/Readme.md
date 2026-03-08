A specialized string manipulation engine designed to format arithmetic problems vertically for educational and diagnostic purposes. This project demonstrates strict adherence to User Interface (UI) constraints and Error-Handling protocols in a Python environment.
Technical Logic
The formatter processes raw arithmetic strings and transforms them into a structured, four-line visual output.
Logic Validation: Implements multi-stage checks for:
Operator Integrity: Supports only addition (+) and subtraction (-).
Digit Constraints: Rejects non-numeric operands.
Operand Width: Limits numbers to 4 digits for layout consistency.
Volume Control: Manages a maximum of 5 problems per call.
String Alignment: Utilizes dynamic rjust() spacing to ensure operators and digits align perfectly regardless of operand length.
Optional Solution Engine: Includes a boolean-triggered calculation layer to display results on an optional fourth line.
