import numpy as np
# External l i b r a r y for numerical c a l c u l a t i o n s
import matplotlib.pyplot as plt
# Plotting library
# F u n c t i o n d e f i n i n g t h e i n i t i a l and a n a l y t i c s o l u t i o n
def initialBell(x):
    return np.where(x%1. < 0.5 , np.power(np.sin(2*x*np.pi),2), 0)
# P u t e v e r y t h i n g i n s i d e a main f u n c t i o n t o a v o i d g l o b a l v a r i a b l e s
def main( ) :
# S e t u p s p a c e , i n i t i a l p h i p r o f i l e and C o u r a n t number
    nx = 40
# number o f p o i n t s i n s p a c e
    c = 0.2
# The C o u r a n t number
# S p a t i a l v a r i a b l e g o i n g f r o m z e r o t o one i n c l u s i v e
    x = np.linspace(0.0, 1.0, nx + 1 )
# Three time l e v e l s of th e dependent v a r i a b l e , phi
    phi = initialBell( x )
    phiNew = phi.copy( )
    phiOld = phi.copy( )
# FTCS f o r t h e f i r s t t i m e -s t e p , l o o p i n g o v e r s p a c e
    for j in range(1, nx ):
        phi[j] = phiOld[j] - 0.5*c*(phiOld[j+1] - phiOld[j-1])
# apply p e r i o d i c boundary c o n d i t i o n s
    phi[0] = phiOld[0] - 0.5*c*(phiOld[1]- phiOld[nx-1])
    phi[nx] = phi[0]
# Loop o v e r r e m a i n i n g t i m e -s t e p s ( n t ) u s i n g CTCS
    nt = 40
    for n in range(1 , nt ) :
# loop over space
        for j in range(1 , nx ) :
            phiNew[j] = phiOld[j] - c * ( phi[j + 1] - phi[j-1])
# apply p e r i o d i c boundary c o n d i t i o n s
        phiNew[0] = phiOld[0] - c * (phi[1] - phi[nx-1])
        phiNew[nx] = phiNew[0]
# u p d a t e p h i f o r t h e n e x t t i m e -s t e p
        phiOld = phi.copy( )
        phi = phiNew.copy( )
# derived quantities
    u = 1.
    dx = 1. / nx
    dt = c* dx / u
    t = nt * dt
# Plot the s o l u t i o n in comparison to the a n a l y t i c s o l u t i o n
    plt.plot(x, initialBell(x) , 'r' , label = 'initial' )
    plt.plot(x, initialBell(x - u*t) , 'k' , label = 'analytic' )
    plt.plot(x, phi, 'b', label = 'CTCS' )
    plt.legend (loc='best' )
    plt.ylabel('$\phi$')
    plt.axhline(0 ,linestyle = ':' , color= 'black' )
    plt.show( )
# Execute t h e code
main( )
