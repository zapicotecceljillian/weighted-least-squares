def weighted_least_squares(x, y, w):

    n = len(x)

    Sw = sum(w)

    Swx = sum(w[i] * x[i] for i in range(n))

    Swy = sum(w[i] * y[i] for i in range(n))

    Swxy = sum(w[i] * x[i] * y[i] for i in range(n))

    Swx2 = sum(w[i] * (x[i] ** 2) for i in range(n))

    b = (
        (Sw * Swxy) - (Swx * Swy)
    ) / (
        (Sw * Swx2) - (Swx ** 2)
    )

    a = (
        Swy - (b * Swx)
    ) / Sw

    return {

        "a": round(a, 5),

        "b": round(b, 5),

        "equation":
        f"y = {round(a,5)} + {round(b,5)}x",

        "Sw": round(Sw,5),

        "Swx": round(Swx,5),

        "Swy": round(Swy,5),

        "Swxy": round(Swxy,5),

        "Swx2": round(Swx2,5)

    }