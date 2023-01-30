library(readr)
library(ggplot2)
theme_set(theme_bw())
tips <- read_csv("https://raw.githubusercontent.com/anly503/datasets/main/tips.csv")

ggplot(tips, aes(x = total_bill))+
        geom_histogram(fill = '#34f6ff', 
                       color='black')

ggplot(tips, aes(factor(day), total_bill, color=factor(day)))+
        geom_jitter(width=0.25)+
        scale_color_brewer(palette = 'Accent')

ggplot(tips, 
       aes(tip, total_bill))+
        geom_point()+
        theme_bw() #<<

ggplot(tips, 
       aes(tip, total_bill))+
        geom_point()+
        ggthemes::theme_fivethirtyeight() #<<

ggplot(tips, 
       aes(tip, total_bill))+
        geom_point()+
        theme_minimal() #<<

ggplot(tips, 
       aes(tip, total_bill))+
        geom_point()+
        ggthemes::theme_tufte() #<<

ggplot(tips, aes(tip, total_bill))+
        geom_point()+
        theme(
                axis.title = element_text(size=16, 
                                          family='Times New Roman', 
                                          color='blue'),
                axis.text = element_text(size = 12),
                panel.grid.major.x = element_blank())

ggplot(tips, aes(tip, total_bill))+
        geom_point()+
        theme_dark()+
        theme(
                axis.title = element_text(size=16, 
                                          family='Times New Roman', 
                                          color='blue'),
                axis.text = element_text(size = 12),
                panel.grid.major.x = element_blank())

# create the theme
my_theme <- theme_dark() + 
        theme(
                axis.title = element_text(size=16, 
                                          family='Times New Roman', 
                                          color='blue'),
                axis.text = element_text(size = 12),
                panel.grid.major.x = element_blank())

# use it in a plot
ggplot(tips, aes(tip, total_bill))+
        geom_point()+
        my_theme

