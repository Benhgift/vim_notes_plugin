if exists("b:current_syntax")
    finish
endif

"Our syntax highlighting code will go here.
syntax keyword potionKeyword a
highlight link potionKeyword Keyword

let b:current_syntax = "potion"
