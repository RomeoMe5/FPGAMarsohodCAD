force clr 1 0ns, 0 30ns, 1 50ns, 0 55ns;
force clk 0 0ns, 1 {2ns} -repeat 3ns;
force ina 10#1 0ns, 10#2 10ns, 10#3 20ns, 10#4 30ns, 10#5 40ns, 10#0 45ns, 10#3 65ns;
force inb 10#0 0ns, 10#1 10ns, 10#2 20ns, 10#3 30ns, 10#4 40ns, 10#5 50ns, 10#6 60ns, 11#7 70ns;