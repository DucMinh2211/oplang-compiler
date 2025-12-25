.source Shape.java
.class public Shape
.super java/lang/Object

.method public draw()V
.var 0 is this LShape; from Label0 to Label1
Label0:
	ldc "Drawing Shape"
	invokestatic io/writeStrLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LShape; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
