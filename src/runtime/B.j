.source B.java
.class public B
.super A

.method public m2()V
.var 0 is this LB; from Label0 to Label1
Label0:
	ldc "B.m2"
	invokestatic io/writeStrLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LB; from Label0 to Label1
Label0:
	aload_0
	invokespecial A/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
