def calculate_tgpa1(a1, c1, e1, g1, i1, k1):
    """Calculates TGPA for semester 1."""
    a, c, e, g, i, k = int(a1.get()), int(c1.get()), int(e1.get()), int(g1.get()), int(i1.get()), int(k1.get())

    if all(0 <= x <= 100 for x in [a, c, e, g, i, k]):
        total_score = (a * 4) + (c * 1) + (e * 2) + (g * 2) + (i * 4) + (k * 1)
        total_credits = (4 + 1 + 2 + 2 + 4 + 1) * 9.5
        tgpa = round(total_score / total_credits, 2)
        return tgpa
    return None


def calculate_tgpa2(a2, c2, e2, g2, i2, k2):
    """Calculates TGPA for semester 2."""
    a, c, e, g, i, k = int(a2.get()), int(c2.get()), int(e2.get()), int(g2.get()), int(i2.get()), int(k2.get())

    if all(0 <= x <= 100 for x in [a, c, e, g, i, k]):
        total_score = (a * 4) + (c * 4) + (e * 1) + (g * 2) + (i * 3) + (k * 2)
        total_credits = (4 + 4 + 1 + 2 + 3 + 2) * 9.5
        tgpa = round(total_score / total_credits, 2)
        return tgpa
    return None


def calculate_cgpa(tgpa1, tgpa2):
    """Calculates combined CGPA based on TGPA of both semesters."""
    if tgpa1 and tgpa2:
        combined_tgpa = tgpa1 + tgpa2
        cgpa = round(combined_tgpa / 2, 2)
        return cgpa
    return None
