#lotto<- read.table("C:/Users/zcao/Documents/unionpay/lotto.txt", header = TRUE,sep=",")
#lotto<- read.table("~/Documents/Personal Files/unionpay/lotto.txt",header=TRUE,sep=",")

num<- c(lotto$Number1,lotto$Number2,lotto$Number3,lotto$Number4,lotto$Number5,lotto$Number6)

barplot(table(num),axes=TRUE)
barplot(table(lotto$Power),axes=TRUE)

pa<- lotto[,1:7]
#test<- as.vector(as.matrix(pa[90,2:7]))
myfa<- array(0,c(4,6))
myfa[1,]<- c(1,5,12,23,24,34)
myfa[2,]<- c(1,5,16,23,24,34)
myfa[3,]<- c(8,15,18,27,29,36)
myfa[4,]<- c(3,12,15,22,30,37)

a=NULL
for(i in 1:nrow(pa)){
	#print(i)
  for(j in 1:nrow(myfa)){
	  if(length(intersect(myfa[j,],pa[i,2:6]))>3) a = c(a,i)
  }
}
a
pa[a,]


#nrow(pa)

#par(mfrow=c(1,1))
#barplot(table(pa[,7]),axes=TRUE)

par(mfrow=c(2,3))
dens<- matrix(0,nrow=40,ncol=6)
for(j in 1:6) dens[,j]<- hist(pa[,(j+1)],breaks=0:40)$density
#sum(dens1)
#length(dens1)
#sum(dens1[1:20])
#sum(dens[,1:6])

sample(40,1,replace=FALSE,prob=dens[,1])
sample(40,1,replace=FALSE,prob=dens[,2])
sample(40,1,replace=FALSE,prob=dens[,3])
sample(40,1,replace=FALSE,prob=dens[,4])
sample(40,1,replace=FALSE,prob=dens[,5])
sample(40,1,replace=FALSE,prob=dens[,6])

par(mfrow=c(1,1))
weights<- hist(num,breaks=0:40)$density
barplot(table(num))

sort(sample(40,6,replace=FALSE,prob=weights))
