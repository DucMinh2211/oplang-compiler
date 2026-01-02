.source Child.java
.class public Child
.super Parent

.method public greet()V
.var 0 is this LChild; from Label0 to Label1
Label0:
	ldc "Child"
	invokestatic io/writeStrLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LChild; from Label0 to Label1
Label0:
	aload_0
	invokespecial Parent/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
