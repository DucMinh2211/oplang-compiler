.source Parent.java
.class public Parent
.super java/lang/Object

.method public greet()V
.var 0 is this LParent; from Label0 to Label1
Label0:
	ldc "Parent"
	invokestatic io/writeStrLn(Ljava/lang/String;)V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public act()V
.var 0 is this LParent; from Label0 to Label1
Label0:
	aload_0
	invokevirtual Parent/greet()V
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
	return
Label1:
.limit stack 1
.limit locals 1
.end method
