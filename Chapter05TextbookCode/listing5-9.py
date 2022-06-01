"""Illustrate namespaces."""

def function_a(param_a: int) -> None:
    local_var_a: int = 0
    print(dir())

def function_b(paramb: int) -> None:
    local_varb: int = 0

def main() -> None:
    local_var_m1: int = 5
    local_var_m2: int = 10
    function_a(local_var_m1)
    function_b(local_var_m2)
    print(dir())

main()
print(dir())
