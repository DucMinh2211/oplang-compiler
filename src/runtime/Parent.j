.source Parent.java
.class public Parent
.super java/lang/Object
.field x I

.method public sayHello()V
.var 0 is this LParent; from Label0 to Label1
Label0:
	ldc "Hello from Parent"
	invokestatic io/writeStrLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LParent; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	bipush 10
	putfield Parent/x I
	return
Label1:
.limit stack 2
.limit locals 1
.end method
