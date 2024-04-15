library(dplyr)
library(ggplot2)
library(tidyverse)

data <- read.csv("nowac-raw-tokens-consonant-clusters.csv")

data <- data %>% 
  arrange(desc(frequency)) %>% 
  mutate(logf = log10(frequency)) %>% 
  mutate(rank = row_number()) %>%
  mutate(logr = log10(rank)) %>%
  mutate(zipf = log10((frequency/sum(frequency))*1000000000)) %>%
  mutate(length = nchar(X))

ggplot(data, aes(x = logr, y = zipf)) +
  geom_point()

zipf7 <- which(data$zipf >= 7)
data$onset[zipf7]
zipf6 <- which(data$zipf >= 6 & data$zipf < 7)
data$onset[zipf6]
zipf5 <- which(data$zipf >= 5 & data$zipf < 6)
data$onset[zipf5]
zipf4 <- which(data$zipf >= 4 & data$zipf < 5)
data$onset[zipf4]
zipf3 <- which(data$zipf >= 3 & data$zipf < 4)
data$onset[zipf3]

data$zipf[which(data$onset
                == "sn")]
