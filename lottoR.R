#lotto<- read.table("C:/Users/zcao/Documents/unionpay/lotto.txt", header = TRUE,sep=",")

num<- c(lotto$Number1,lotto$Number2,lotto$Number3,lotto$Number4,lotto$Number5,lotto$Number6)

barplot(table(num),axes=TRUE)
barplot(table(lotto$Power),axes=TRUE)
