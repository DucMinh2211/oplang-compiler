.source Factory.java
.class public Factory
.super java/lang/Object

.method public static create(I)LBox;
.var 0 is v I from Label0 to Label1
Label0:
	new Box
	dup
	iload_0
	invokespecial Box/<init>(I)V
	areturn
Label1:
.limit stack 3
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LFactory; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
