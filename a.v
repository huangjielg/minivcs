`timescale 1ns/1ps
module a;
 reg clk;
 initial begin
    $fsdbDumpvars();
    clk=1'b1;
    #10;
    clk=1'b0;
    #10;
    $finish();
 end
endmodule
