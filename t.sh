
VCS_HOME=$PWD/opt/vcs-mx
NOVAS_HOME=$PWD/opt/verdi
VERDI_HOME=$NOVAS_HOME
DEBUSSY_HOME=$NOVAS_HOME
PATH=/bin:/usr/bin:/usr/sbin:$VCS_HOME/bin:$VERDI_HOME/bin

#rm -fr simv* csrc
#vcs -R a.v -fsdb -LDFLAGS -Wl,--no-as-needed  -kdb -gui -full64
strace -f -e trace=file -o verdi_strace2.log -s1024\
    verdi a.v
