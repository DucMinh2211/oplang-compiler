.source Circle.java
.class public Circle
.super Shape

.method public draw()V
.var 0 is this LCircle; from Label0 to Label1
Label0:
	ldc "Circle"
	invokestatic io/writeStrLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LCircle; from Label0 to Label1
Label0:
	aload_0
	invokespecial Shape/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
