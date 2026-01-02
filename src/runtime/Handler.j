.source Handler.java
.class public Handler
.super java/lang/Object

.method public static handle(LContainer;)V
.var 0 is c LContainer; from Label0 to Label1
Label0:
	ldc "Handled"
	invokestatic io/writeStrLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LHandler; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
