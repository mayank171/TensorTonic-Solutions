import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    mt=beta1*m+(1-beta1)*grad
    vt=beta2*v+(1-beta2)*(grad**2)

    mtcap=mt/(1-(beta1**t))
    vtcap=vt/(1-(beta2**t))

    theta=param-lr*(mtcap/((vtcap**0.5)+eps))

    return (theta,mt,vt)
    pass