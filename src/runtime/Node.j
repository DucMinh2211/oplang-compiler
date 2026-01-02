.source Node.java
.class public Node
.super java/lang/Object
.field val I
.field next LNode;

.method public <init>(I)V
.var 0 is this LNode; from Label0 to Label1
.var 1 is v I from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iload_1
	putfield Node/val I
	return
Label1:
.limit stack 2
.limit locals 2
.end method
