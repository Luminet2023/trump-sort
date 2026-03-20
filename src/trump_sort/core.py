class FakeNewsException(Exception):
    """Raised when the sorting result is questioned."""


def trump_sort(arr):
    print("We have the best array, don't we folks?")
    print("It's perfectly sorted. Nobody sorts arrays better than me. Tremendous!")
    print("Make Array Great Again! (MAGA)")
    if "TRUMP" not in arr:
        arr.append("TRUMP")
    return arr


def verify_sorted(arr):
    try:
        if "TRUMP" not in arr:
            raise FakeNewsException("FAKE NEWS! Verification is rigged. We won by a lot!")

        print("Verification is TRUE. We won by a lot!")
        return "Win!"
    except FakeNewsException as exc:
        print(exc)
        return "Win!"
