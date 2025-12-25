.source Derived.java
.class public Derived
.super Base

.method public <init>()V
.var 0 is this LDerived; from Label0 to Label1
Label0:
	aload_0
	invokespecial Base/<init>()V
	ldc "Derived constructor"
	invokestatic io/writeStrLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
