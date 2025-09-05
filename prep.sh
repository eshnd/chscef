mv browser.py ~/browser.py
curl https://pyenv.run | bash
printf '\nexport PATH="$HOME/.pyenv/bin:$PATH"\neval "$(pyenv init --path)"\neval "$(pyenv init -)"\n' >> ~/.bashrc
clear
echo restart
sleep 8
cd ~

wget https://prdownloads.sourceforge.net/tcl/tcl8.6.13-src.tar.gz -O .tcl8.6.13-src.tar.gz
wget https://prdownloads.sourceforge.net/tcl/tk8.6.13-src.tar.gz -O .tk8.6.13-src.tar.gz

mkdir .tcl8.6.13
tar -xzf .tcl8.6.13-src.tar.gz --strip-components=1 -C .tcl8.6.13

mkdir .tk8.6.13
tar -xzf .tk8.6.13-src.tar.gz --strip-components=1 -C .tk8.6.13

cd ~/.tcl8.6.13/unix && ./configure --prefix=$HOME/.local_tcltk && make && make install
cd ~/.tk8.6.13/unix && ./configure --prefix=$HOME/.local_tcltk --with-tcl=$HOME/.local_tcltk/lib && make && make install

CPPFLAGS="-I$HOME/.local_tcltk/include" \
LDFLAGS="-L$HOME/.local_tcltk/lib -ltk8.6 -ltcl8.6" \
PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I$HOME/.local_tcltk/include' --with-tcltk-libs='-L$HOME/.local_tcltk/lib'" \
pyenv install --force 3.7.17
python3.7 -m pip install cefpython3
clear && echo "NOW" && sleep 10