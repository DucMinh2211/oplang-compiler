.source C.java
.class public C
.super B

.method public m1()V
.var 0 is this LC; from Label0 to Label1
Label0:
	ldc "C.m1"
	invokestatic io/writeStrLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LC; from Label0 to Label1
Label0:
	aload_0
	invokespecial B/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
