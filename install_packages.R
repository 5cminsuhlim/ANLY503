install.packages('pacman', repos = 'https://cran.rstudio.com')

library(pacman)

pkgs <- readLines('packages.csv')
p_load(char = setdiff(pkgs, c('icons','emo')))
p_install_gh('mitchelloharawild/icons')
p_install_gh('hadley/emo')
