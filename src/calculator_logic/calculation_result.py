class CalculationResult:
    def __init__(self, result=0.0, is_success=False, operation="", error=""):
        self.result = result
        self.is_success = is_success
        self.operation = operation
        self.error = error
