
setwd("") #insert directory for file. 

df <- read.table(".txt", header = TRUE) #insert filename 

#column details

#block - block number 
#signal - go or stop signal (0 = go, 1 = stop)
#trueSOA - actual stop signal delay based on screen refresh rate
#correct - 4 means correct go response or successful stop, 3 means failed stop response or two go responses, 2 means incorrect go response, 1 means missed go response
#rt1 - reaction time for first response 



meanGoRT <- mean(subset(df, block != 0 & signal == 0 & correct == 4)$rt1) #calculates mean go reaction time. Ignores practise block. 

criticalSSD <- mean(subset(df, block !=0 & signal ==1)$trueSOA) #calculates critical stop signal delay.  Ignores practise block.

meanSSRT <- meanGoRT - criticalSSD #calculates SSRT based on mean method. 

countGoRT <- length(subset(df, block!=0 & signal == 0 & correct == 4)$rt1)#number of correct go responses

AccuracyGo <- countGoRT/120 #go accuracy given 120 go trials 

countStop <- length(subset(df, block!=0 & signal == 1 & correct == 4)$trueSOA)#number of successful stops

AccuracyStop <- countStop/60 #stop accuracy given 60 stop trials 

nthGoRTnumber <- (1-AccuracyStop)*(countGoRT)#determines the number of the nthGoRT based on the integration method

roundednthGoRTnumber <- round(nthGoRTnumber, digits = 0)#round the nthGoRT to the nearest integer 

Data <- subset(df, block!=0 & signal == 0 & correct == 4)$rt1 #get all Go RTs

sortedData <- sort(subset(df, block!=0 & signal == 0 & correct == 4)$rt1) #sort the GoRTs 

nthGoRT <- sortedData[roundednthGoRTnumber] #the nth Go RT

IntegratedSSRT <- nthGoRT - criticalSSD #determines SSRT based on Integration method 

RawFixedSSDTime <- 0.5 + criticalSSD/1000 #the critical SSD for TMS (0.5 refers to the fixation time) 

DivideCriticalSSD <- RawFixedSSDTime/0.016666666666 #divide by refresh rate

RoundedDivideCriticalSSD <- round(DivideCriticalSSD, digits = 0)#determines the multiple of the refresh rate to present the SSD

FixedSSDTime <- (0.016666666666*RoundedDivideCriticalSSD)#the exact SSD for the TMS phase based on refresh rate


FinalFixedSSDTime <- FixedSSDTime - 0.002 #subtract by a small amount to ensure the SSD is presented on the next screen cycle after this

TMSTime <- FinalFixedSSDTime + 0.2 #TMS delivered 200ms after SSD

print(meanGoRT)
print(criticalSSD)
print(meanSSRT)
print(countGoRT)
print(AccuracyGo)
print(countStop)
print(AccuracyStop)
print(nthGoRTnumber)
print(roundednthGoRTnumber)
print(Data)
print(sortedData)
print(nthGoRT)
print(IntegratedSSRT)
print(TMSTime)
print(RawFixedSSDTime)
print(DivideCriticalSSD)
print(RoundedDivideCriticalSSD)
print(FixedSSDTime)
print(FinalFixedSSDTime)
print(TMSTime)
write.table(c(IntegratedSSRT, nthGoRT, meanGoRT, meanSSRT, criticalSSD, AccuracyGo, AccuracyStop, FixedSSDTime, FinalFixedSSDTime, TMSTime), file = "1007_Data.csv", sep = ",", row.names = c("IntegratedSSRT", "nthGoRT", "meanGoRT", "meanSSRT", "criticalSSD", "AccuracyGo", "AccuracyStop", "FixedSSDTime", "FinalFixedSSDTime", "TMSTime"), col.names = FALSE)
