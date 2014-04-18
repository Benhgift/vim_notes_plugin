function! Close_notes_server()
    echo "test"
endfunction

function! Close_notes_server()
    echo "test"
endfunction

au VimLeave * silent call Close_notes_server()
au FileWritePost * silent call Update_server_db_then_file()
