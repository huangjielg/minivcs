
rm -fr simv* csrc
#strace -f -e trace=open,stat,execve -o vcs_strace.log 
# strace -f -e trace=file -e status -o vcs_strace.log 

 strace -f -e trace=file  -o vcs_strace.log -s1024\
    vcs -R a.v -full64 -fsdb -LDFLAGS -Wl,--no-as-needed -kdb -gui
strace -f -e trace=file -o verdi_strace.log -s1024\
    verdi a.v -ba -ssf novas.fsdb     
grep "/opt/synopsys" vcs_strace.log > vcs_strace_a.txt
grep "/opt/synopsys" verdi_strace.log >> vcs_strace_a.txt