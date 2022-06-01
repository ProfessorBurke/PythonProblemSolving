"""Replace missing values with NA."""

def replace_missing(data: str) -> str:
    """Return NA if value passed is a dash."""
    final_data: str = data
    if data == "-":
        final_data = "NA"
    return final_data

def main() -> None:
    """Test the replace_missing function."""
    result: str
    result = replace_missing("0")
    print("0 was replaced with {}".format(result))
    result = replace_missing("-")
    print("- was replaced with {}".format(result))

main()
