force clk 2#1 0ns, 2#0 {25ns} -repeat 50ns;
force we 1#0 0ns;
force data 8#3 0ns, 8#7 90ns, 8#5 210ns;
force addr 16#4 0ns;
force we 2#0 200ns;