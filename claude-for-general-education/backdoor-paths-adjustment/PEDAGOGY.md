# PEDAGOGY
Concept: backdoor criterion — blocking non-causal paths from T to Y.
Problem: how do you find and close all backdoor paths in a pricing DAG?
Question on screen: which variables should you condition on to identify the causal effect?
Answer: find every path entering T via back-arrow, choose a set of nodes that blocks them all without conditioning on a collider.
