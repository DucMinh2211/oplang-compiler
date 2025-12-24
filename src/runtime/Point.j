.source Point.java
.class public Point
.super java/lang/Object
.field x I
.field y I

.method public <init>(II)V
.var 0 is this LPoint; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iload_1
	putfield Point/x I
	aload_0
	iload_2
	putfield Point/y I
	return
Label1:
.limit stack 2
.limit locals 3
.end method
