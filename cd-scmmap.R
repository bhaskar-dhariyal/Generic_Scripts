# if (!require("devtools")) {
#   install.packages("devtools")
# }
# 
# devtools::install_github("b0rxa/scmamp")
library("scmamp")

#line 163 : cd <- getNemenyiCD(alpha=alpha, num.alg=k, num.problems=N)
#I used the following functions for our dmkd paper
workdir <-"/Users/bhaskar/Desktop/aaltd20/R/cd_data"
##read data
data <- read.csv(sprintf("%s/error_rock9.csv", workdir),check.names=F)
print(colnames(data))
#summary(data)
#str(data)
#head(data, 10)
#clf = c("DTW_I", "DTW_D")
#print(data[,-2])
#imanDavenportTest(data[,-1])
# critical difference diagram
#plotCD(data[,-1], alpha=0.1, cex =1, decreasing = TRUE, title='CD title', main='alpha=0.1')

test <- postHocTest(data[,-1], test="wilcoxon", correct="holm",use.rank=TRUE)
#test <- postHocTest(data[,-1], test="friedman", correct="bergmann",use.rank=TRUE)
#print(friedmanTest(data[,-1]))
#test
plotRanking(pvalues=test$corrected.pval, summary=test$summary, alpha=0.05, decreasing = FALSE, cex = 1)

bold <- test$corrected.pval < 0.05
bold
bold[is.na(bold)] <- FALSE
#
writeTabular(table=test$corrected.pval, format='f', bold = bold, hrule = 0, vrule = 0)
