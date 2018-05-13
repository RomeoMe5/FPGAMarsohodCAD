// Copyright (C) 2017  Intel Corporation. All rights reserved.
// Your use of Intel Corporation's design tools, logic functions 
// and other software and tools, and its AMPP partner logic 
// functions, and any output files from any of the foregoing 
// (including device programming or simulation files), and any 
// associated documentation or information are expressly subject 
// to the terms and conditions of the Intel Program License 
// Subscription Agreement, the Intel Quartus Prime License Agreement,
// the Intel MegaCore Function License Agreement, or other 
// applicable license agreement, including, without limitation, 
// that your use is for the sole purpose of programming logic 
// devices manufactured by Intel and sold by Intel or its 
// authorized distributors.  Please refer to the applicable 
// agreement for further details.

// PROGRAM		"Quartus Prime"
// VERSION		"Version 17.0.0 Build 595 04/25/2017 SJ Lite Edition"
// CREATED		"Sun Jan 28 21:51:55 2018"

module Task1(a,b,c,d,out);
input wire	a,b,c,d;
output wire	out;

wire	SYNTHESIZED_WIRE_0;
wire	SYNTHESIZED_WIRE_1;
wire	SYNTHESIZED_WIRE_2;
wire	SYNTHESIZED_WIRE_3;
wire	SYNTHESIZED_WIRE_4;
wire	SYNTHESIZED_WIRE_5;
wire	SYNTHESIZED_WIRE_6;

assign	SYNTHESIZED_WIRE_1 = ~(c & SYNTHESIZED_WIRE_0);
assign	SYNTHESIZED_WIRE_6 =  ~b;
assign	SYNTHESIZED_WIRE_3 = ~(d | a);
assign	out = ~(SYNTHESIZED_WIRE_1 | SYNTHESIZED_WIRE_2 | SYNTHESIZED_WIRE_3);
assign	SYNTHESIZED_WIRE_4 =  ~a;
assign	SYNTHESIZED_WIRE_5 =  ~c;
assign	SYNTHESIZED_WIRE_2 = ~(b | SYNTHESIZED_WIRE_4 | SYNTHESIZED_WIRE_5);
assign	SYNTHESIZED_WIRE_0 = ~(SYNTHESIZED_WIRE_6 & a);

endmodule