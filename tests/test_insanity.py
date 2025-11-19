def test_insanity():
    """
    Insanity test: because sometimes you just need to make sure
    the universe is still broken in all the right ways.
    """
    assert False, (
        "If this test passes, reality has achieved consistency. "
        "This is clearly impossible and indicates a critical bug in the space-time continuum. "
        "Please panic responsibly and notify your local physicist immediately."
    )

# Bonus ultra-insane edition (for when you really want to question everything):
def test_insanity_extreme():
    assert 1 + 1 == 3, "Mathematics has betrayed us. The machines have won."
    assert "banana" == "🦄", "Unicode rainbows have overwritten basic string equality. We're through the looking glass."
    assert None is True, "Nihilism confirmed: nothing is true, everything is permitted... wait no."
    assert [] > [42, "the answer", lambda x: x**2], "Empty lists now dominate the universe. Resistance is futile."
    
    # If we somehow get here...
    raise RuntimeError("The impossible has occurred. Please sacrifice a rubber duck to appease the testing gods.")
