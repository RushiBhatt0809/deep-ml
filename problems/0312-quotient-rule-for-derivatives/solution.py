import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    g,h = np.polyval(g_coeffs,x) ,  np.polyval(h_coeffs,x)
    pd1,pd2 = np.polyder(g_coeffs),np.polyder(h_coeffs)
    dg,dh = np.polyval(pd1,x),np.polyval(pd2,x)
    return (h*dg - g*dh)/(h**2)