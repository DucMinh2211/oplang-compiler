.source A.java
.class public A
.super java/lang/Object
.field x I

.method public printX()V
.var 0 is this LA; from Label0 to Label1
Label0:
	aload_0
	getfield A/x I
	invokestatic io/writeIntLn(I)V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LA; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	bipush 10
	putfield A/x I
	return
Label1:
.limit stack 2
.limit locals 1
.end method
