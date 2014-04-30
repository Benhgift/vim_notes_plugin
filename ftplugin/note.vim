let s:port = 0

function! Start_notes_server()
    echo "test"
    let s:port = system(python python_server ." ". bufname("%"))
endfunction

function! Close_notes_server()
    echo "test"
"    system(python_server_ping_script ." kill ". port)
endfunction

function! Update_server_db_then_file()
    echo "test"
"    let new_file_text = system(python_server_ping_script ." ". bufname("%") ." ". port)
"    norm! ggdG
"    call append(0, split(new_file_text, '\v\n'))
endfunction

au VimEnter * silent call Start_notes_server()
au BufWritePost * silent call Update_server_db_then_file()
au VimLeave * silent call Close_notes_server()
