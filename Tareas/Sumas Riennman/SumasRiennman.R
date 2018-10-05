xvalores = seq(-3, 3, 0.1)
yvalores=dnorm(xvalores)
nparticiones=61
aux=61/nparticiones
sum=0
yAcum=c()
xAcum=c()
for(i in 1:n){
  yAcum[i]=yvalores[i*aux]
  xAcum[i]=xvalores[i*aux]  
  sum=sum+(yAcum[i]*aux)
}
print(sum)
par(mfrow=c(1,2))
plot(x = xvalores, y = yvalores, type="l", bty="n",main="Curva")
barplot(yAcum,main="rectangulos",col="green")