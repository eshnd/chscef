CPPFLAGS="-I$HOME/.local_tcltk/include" \
LDFLAGS="-L$HOME/.local_tcltk/lib -ltk8.6 -ltcl8.6" \
PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I$HOME/.local_tcltk/include' --with-tcltk-libs='-L$HOME/.local_tcltk/lib'" \

python3.7 -m pip install cefpython3
