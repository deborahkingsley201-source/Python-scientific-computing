class TernaryALU:
    def __init__(self):
        # Balanced Ternary: -1, 0, 1
        self.trits = {-1, 0, 1}

    def half_adder(self, a, b):
        """Adds two trits and returns (sum, carry)"""
        s_raw = a + b
        if s_raw == 2: return (-1, 1)
        if s_raw == -2: return (1, -1)
        return (s_raw, 0)

    def full_adder(self, a, b, c_in):
        """Adds two trits with a carry-in"""
        s1, c1 = self.half_adder(a, b)
        s2, c2 = self.half_adder(s1, c_in)
        # In balanced ternary, c1 + c2 will never exceed 1 or -1
        return (s2, c1 + c2)

    def decimal_to_balanced(self, n):
        """Converts Decimal to Balanced Ternary string"""
        if n == 0: return "0"
        res = ""
        while n != 0:
            rem = ((n + 1) % 3) - 1
            res = ("T" if rem == -1 else str(rem)) + res
            n = (n - rem) // 3
        return res

# --- Example of Trit-wise Addition ---
alu = TernaryALU()
# Adding 1 and 1 in Ternary (Result should be 1T, which is 3-1 = 2)
sum_trit, carry = alu.half_adder(1, 1)
print(f"1 + 1 in Ternary: {carry}{sum_trit.replace('-1', 'T') if isinstance(sum_trit, str) else sum_trit}")
