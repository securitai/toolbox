#########################
#  git
#########################
alias gsn='git status -uno'
alias gs='git status'
alias gd='git diff'
alias gdc='git diff --cached'
alias gau='git add -u'
alias gcq='git commit -qm'
alias gl='git log'
alias gb='git branch'
alias gba='git branch --all'
alias gk='gitk'
alias gka='gitk --all'
alias gpom='git push origin master'

alias l='ls --color=always'
alias ll='ls -larth --color=always'

alias d='display'
alias python='python3'

alias activate='conda activate faceswap'
alias deactivate='conda deactivate'

stty -ixon

bind '"\ew": "\e[A"'
bind '"\es": "\e[B"'
bind '"\ej": "\C-m"'
bind '"\C-w": "\e[A"'
bind '"\C-s": "\e[B"'

