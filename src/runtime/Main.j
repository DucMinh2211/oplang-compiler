.source Main.java
.class public Main
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is d LDerived; from Label0 to Label1
	new Derived
	dup
	invokespecial Derived/<init>()V
	astore_1
	return
Label1:
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMain; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
