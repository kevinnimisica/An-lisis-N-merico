install.packages("ggplot2")#instalar paquete
library(ggplot2)
# Instalar libreria rSymPy, matrix
Xsilueta=c(0.9, 1.3, 1.9, 2.1, 2.6, 3, 3.9, 4.7, 6, 7, 8, 9.2, 10.5, 11.3, 11.6, 12.6,  13.3, 12, 10.7, 10, 8.5, 8,  7, 6, 4.75, 5.1, 5.48, 5.6, 4.2, 3.5, 2.55, 2.1, 1.3,0.9)                                                                                                       
Ysilueta=c(1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.05, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.5, 0.2, -0.25, 0, 0.25, -0.5, -2, -4, -4.8, -5.1, -4, -2, 0.1, 1.01, 1.01, 1.05, 1.2, 1,1.3)
difNewton <- function(Xsilueta, Ysilueta, valor) {
  require(rSymPy)
  n <- length(Xsilueta)
  q <- matrix(data = 0, n, n)
  q[,1] <- Ysilueta
  f <- as.character(round(q[1,1], 5))
  fi <- ''
  for (i in 2:n) {
    for (j in i:n) {
      q[j,i] <- (q[j,i-1] - q[j-1,i-1]) / (Xsilueta[j] - Xsilueta[j-i+1])
    }
    fi <- paste(fi, '*(x - ', Xsilueta[i-1], ')', sep = '', collapse = '')
    f <- paste(f, ' + ', round(q[i,i], 5), fi, sep = '', collapse = '')
  }
  Xsilueta <- Var('x')
  sympy(paste('e = ', f, collapse = '', sep = ''))
  approx <- sympy(paste('e.subs(x, ', as.character(valor), ')', sep = '', collapse = ''))
  return(list('Aproximacion de la interpolacion'=as.numeric(approx), 
              'Funcion Interpolada'=f, 
              'Diferencias Divididas'=q))
}